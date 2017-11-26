from flask import Flask, render_template, url_for, request, redirect, jsonify, Response
from mendeley import Mendeley, resources
import os, sys
import collections
import json

# Importing class of functions for interacting with input
modulePath = "../parser"
sys.path.append(os.path.abspath(modulePath))
from TermTools import TermTools

# Create flask application
app = Flask(__name__)

@app.route("/")
def index():
	return app.send_static_file('index.html')

@app.route("/test")
def test():
	return "a"

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

@app.route("/api", methods=["GET", "POST"])
def api(queryResults = None):
	print(request.method)
	if request.method == "POST":
		print("bbbbbb")
		print("query:", request.data)
		query = request.data.decode("utf-8")
		print("bbbbbc")
	
		termFrequency = TermTools.getWordCount(query)		
		print("bbbbbd")
		wordsToRemove = \
		TermTools.removeWords("../code-testing/formatted_dictionary", list(termFrequency.keys()))
		print(termFrequency)
		#termFrequency = TermTools.mergeWords(termFrequency)
		print("bbbbbf")
		valuesAndDois = TermTools.valueFunction(termFrequency)
		print("bbbbbg")
		doisAndInfo = TermTools.dois2articles("../config/config.yml.rasmus", valuesAndDois)
		print("bbbbbh")
		queryResults = doisAndInfo
		print(queryResults)
		# Reduce size of dictionary s.t. only ten entries are
		# displayed
		for key in list(doisAndInfo.keys())[3:]:
			del doisAndInfo[key]
		print(doisAndInfo)
	
	return json.dumps(doisAndInfo)
