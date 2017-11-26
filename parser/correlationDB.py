from pymongo import MongoClient
from crossrefQuery import crossrefQuery

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
				term1_dois = crossrefQuery(term1)
				term2_dois = crossrefQuery(term2)
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
