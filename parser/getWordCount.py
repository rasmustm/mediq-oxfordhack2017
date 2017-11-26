def getWordCount(string):
	stringArray = string.split()

	termFrequency = {}

	for word in Set(stringArray):
		if word in termFrequency:
			termFrequency[word] += 1
		else:
			termFrequency[word] = 1

	return termFrequency
