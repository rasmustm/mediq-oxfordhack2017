from urllib.request import urlopen
import json

url = "https://api.crossref.org/works?query=cancer&rows=10"

with urlopen(url) as u:
	data = json.loads(u.read().decode())

	for e in data["message"]["items"]:
		print(e["publisher"])

