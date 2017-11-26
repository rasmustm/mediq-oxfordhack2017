from flask import Flask, render_template, url_for, request, redirect
from mendeley import Mendeley, resources
import os, sys
import collections

# Importing class of functions for interacting with input
modulePath = "../parser"
sys.path.append(os.path.abspath(modulePath))
from TermTools import TermTools

# Create flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(queryResults = None):
	if request.method == "POST":
		print("query:", request.form["query"])
		query = request.form["query"]

		termFrequency = TermTools.getWordCount(query)

		wordsToRemove = \
		TermTools.wordsToRemove("../code-testing/formatted_dictionary", list(termFrequency.keys()))

		print(wordsToRemove)

		for word in wordsToRemove:
			del termFrequency[word]
			
		print(list(termFrequency.keys()))

		termFrequency = TermTools.mergeWords(termFrequency)
		valuesAndDois = TermTools.valueFunction(termFrequency)
		doisAndInfo = TermTools.dois2articles("../config/config.yml.rasmus", valuesAndDois)

		queryResults = doisAndInfo

		# Remove all entries that do not have an abstract
		removeValues = []
		for key, value in queryResults.items():
			if value["abstract"] == None:
				removeValues.append(key)

		for key in removeValues:
			del queryResults[key]
		# Reduce size of dictionary s.t. only ten entries are
		# displayed
		for key in list(queryResults.keys())[11:]:
			del queryResults[key]

	return render_template("index.html", queryResults=queryResults, async_mode=socketio.async_mode) 

@app.route("/test")
def test():
	return "test"
