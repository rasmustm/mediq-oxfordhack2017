from crossrefQuery import crossrefQuery

# creates a dictionary mapping DOI -> value for each term

term1 = "depression"
a1 = 3

term1_results = crossrefQuery(term1)
term1_dictionary = {}

for entry in term1_results:
	term1_dictionary[entry[0] : a1 ]
