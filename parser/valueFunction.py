from crossrefQuery import crossrefQuery

def valueFunction(termFrequency):
	# takes a dictionary of terms and their respective
	# frequency and returns a dictionary of DOIs and their
	# value

	doiValue = {}
	masterDOIList = []
	
	for term, frequency in termFrequency.items():
		keyDOIList = crossrefQuery(term)

		for x in range(0, frequency):
			masterDOIList.append(keyDOIList)

	for doi in Set(masterDOIList):
		if doi in doiValue:
			doiValue[doi] = 1
		else:
			doiValue[doi] +=1

	return doiValue
