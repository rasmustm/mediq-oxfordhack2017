from habanero import Crossref

def crossrefQuery(query):
	# takes a word, then searches and returns a 2-D list with each DOI and title

	cr = Crossref()
	queryResults = cr.works(query=query)

	cleanResults = []	

	for e in queryResults["message"]["items"]:
		cleanResults.append([e["title"][0], e["DOI"]])

	return cleanResults
