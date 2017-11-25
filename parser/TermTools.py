from pymongo import MongoClient
from habanero import Crossref

class TermTools:
	@staticmethod
	def mergeWords(termFrequency, correlationThreshold=0.5):
		# takes a dictinary of terms with corresponding frequency
		# and then merges those with a high enough correlation
	
		client = MongoClient('localhost', 27017)
		db = client.test_database
		correlationCollection = db.correlation
		
		def insertCorrelation(term1, term2, correlation):
				l = sorted([term1, term2])
				entry = {
						"keyword1": l[0],
						"keyword2": l[1],
						"correlation": correlation}
	
				correlationCollection.insert_one(entry)
		
		def getCorrelation(term1, term2):
				l=sorted([term1, term2])
				entry= correlationCollection.find_one(
						{"keyword1": l[0],"keyword2": l[1]})
				if( entry == None):
						return None
				return entry["correlation"]
	
	
		def average(a, b):
			return (a + b) / 2
		
		terms = list(termFrequency.keys())
		
		for i in range(len(terms)):
			for j in range(i+1, len(terms)):
				term1 = terms[i]
				term2 = terms[j]
	
				correlation = getCorrelation(term1, term2)
				print(correlation)
	
				if (correlation == None):
					term1_dois = TermTools.crossrefQuery(term1)
					term2_dois = TermTools.crossrefQuery(term2)
					print(term1, term2)
					print(term1_dois)
					print(term2_dois)
					print("---")
	
					correlation = len(set(term1_dois).intersection(term2_dois)) \
						/ (max(len(term1_dois), len(term2_dois)) + 0.0) 
	
					insertCorrelation(term1, term2, correlation)
	
				if(correlation >= correlationThreshold):
					compoundTerm = term1 + " " + term2
					termFrequency[compoundTerm] = average(termFrequency[term1], termFrequency[term2])
						
					del termFrequency[term1]
					del termFrequency[term2]
	
		return termFrequency
	
	@staticmethod
	def crossrefQuery(query):
		# returns a list of DOIs
	
		cr = Crossref()
		queryResults = cr.works(query=query)
	
		cleanResults = []	
	
		for e in queryResults["message"]["items"]:
			cleanResults.append(e["DOI"])
	
		return cleanResults

	@staticmethod
	def getWordCount(string):
		stringArray = string.split()
	
		termFrequency = {}
	
		for word in set(stringArray):
			if word in termFrequency:
				termFrequency[word] += 1
			else:
				termFrequency[word] = 1
	
		return termFrequency

	@staticmethod
	def valueFunction(termFrequency):
		# takes a dictionary of terms and their respective
		# frequency and returns a dictionary of DOIs and their
		# value
	
		doiValue = {}
		masterDOIList = []
		
		for term, frequency in termFrequency.items():
			keyDOIList = TermTools.crossrefQuery(term)
	
			for x in range(0, frequency):
				for doi in keyDOIList:
					masterDOIList.append(doi)
	
		for doi in set(masterDOIList):
			if doi not in doiValue:
				doiValue[doi] = 1
			else:
				doiValue[doi] +=1
	
		return doiValue
