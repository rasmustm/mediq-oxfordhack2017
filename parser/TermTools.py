from pymongo import MongoClient
from mendeley import Mendeley
import os, sys, yaml
import json
from urllib.request import urlopen

class TermTools:
	@staticmethod
	def mergeWords(termFrequency, correlationThreshold=0.5):
		# takes a dictinary of terms with corresponding frequency
		# and then merges those with a high enough correlation
	
		client = MongoClient('localhost', 27017) db = client.test_database
		correlationCollection = db.correlation
		
		def insertCorrelation(term1, term2, correlation):
			l = sorted([term1, term2])
			entry = {
				"keyword1": l[0],
				"keyword2": l[1],
				"correlation": correlation}
	
			correlationCollection.insert_one(entry)
		
		def getCorrelation(term1, term2):
			# gets correlation betweem two search term by
			# comparing how many results they share

			l = sorted([term1, term2])
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
	
				if (correlation == None):
					term1_dois = TermTools.crossrefQuery(term1)
					term2_dois = TermTools.crossrefQuery(term2)
	
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
		# returns a list of DOIs based on some text query

		cleanResults = []

		url = "https://api.crossref.org/works?query=" + query + "&rows=100"
		with urlopen(url) as u:
			data = json.loads(u.read().decode())
			
			for e in data["message"]["items"]:
				cleanResults.append(e["DOI"])

		return cleanResults

	@staticmethod
	def getWordCount(string):
		# counts frequency of each word in a string and returns
		# a dictionary with frequency
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

	@staticmethod
	def dois2articles(configLocation, doisAndValues):
		# takes the location of the config file for mendeley, and a 
		# dictionary with DOIs and their respective values 
		# and returns a dictionary with DOIs as keys and 
		# abstracts, titles and more in a dict as values

		if os.path.isfile(configLocation):
			with open(configLocation) as f:
				config = yaml.load(f)

		mendeley = Mendeley(config["clientId"], config["clientSecret"])
		session = mendeley.start_client_credentials_flow().authenticate()

		dois = doisAndValues.keys()
		doisAndInfo = {}

		for doi in dois:
			try:
				info = session.catalog.by_identifier(doi=doi, view="stats")

				doisAndInfo[doi] = {
					"title": info.title,
					"abstract": info.abstract,
					"link": info.link,
					"keywords": info.keywords,
					"year": info.year
				}
			except Exception as e:
				pass
			
		return doisAndInfo
	
	@staticmethod
	def removeWords(dictionaryLocation, listOfWords):
		dictionaryWords = open(dictionaryLocation).read().split()

		for word in listOfWords:
			if word not in dictionaryWords:
				listOfWords.remove(word)

		return listOfWords
