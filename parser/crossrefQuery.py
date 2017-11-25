from habanero import Crossref

def crossrefQuery(query):
	# returns a list of DOIs

	cr = Crossref()
	queryResults = cr.works(query=query)

	cleanResults = []	

	for e in queryResults["message"]["items"]:
		cleanResults.append(e["DOI"])

	return cleanResults
