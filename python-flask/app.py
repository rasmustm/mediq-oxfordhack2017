from flask import Flask, render_template, url_for, request, redirect
from mendeley import Mendeley, resources
import os, sys

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
		termFrequency = TermTools.mergeWords(termFrequency)
		valuesAndDOIs= TermTools.valueFunction(termFrequency)

		queryResults = valuesAndDOIs
	return render_template("index.html", queryResults=queryResults) 
@app.route("/test")
def test():
	return "test"
