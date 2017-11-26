from lxml import html
import requests

keywords=["ablation", "b"]
params=" ".join(keywords)
url = "https://scholar.google.com/scholar?q=+"+params+"+site%3Aelsevier.com"

articles=[]

page = requests.get(url)
tree = html.fromstring(page.content)
print(tree.xpath('//div/h3/a/text()'))


