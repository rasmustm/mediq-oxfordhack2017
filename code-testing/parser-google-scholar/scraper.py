from lxml import html
import requests

import pickle



urls = [
        "https://www.health.harvard.edu/medical-dictionary-of-health-terms/a-through-c",
"https://www.health.harvard.edu/medical-dictionary-of-health-terms/d-through-i",
"https://www.health.harvard.edu/medical-dictionary-of-health-terms/j-through-p",
"https://www.health.harvard.edu/medical-dictionary-of-health-terms/q-through-z"
    ]
nameSet=[]

for i in range(4):
    page = requests.get(urls[i])
    tree = html.fromstring(page.content)
    nameSet.extend(tree.xpath('//p/strong/text()')[1:])

#print(nameSet)

for i in range(len(nameSet)):
    nameSet[i]=nameSet[i][:-2]

#print(nameSet)

with open('dict', 'wb') as fp:
    pickle.dump(nameSet, fp)

