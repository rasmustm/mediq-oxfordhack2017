from habanero import Crossref

cr = Crossref()

x = cr.works(query="ecology")

# print(x)

for e in x["message"]["items"]:
	if e["type"] == "book-chapter":
		print(e["title"])
		print(e["DOI"])

# for e in x["message"]:
# 	print(e)
# 
# 
# for e in x["message"]["items"]:
# 	print(e)
