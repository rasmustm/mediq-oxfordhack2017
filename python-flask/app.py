from flask import Flask, render_template, url_for, request, redirect
from mendeley import Mendeley, resources

# # Registering for Mendeley API
# mendeley = Mendeley(4968, client_secret="YTjaHusKfWLU7tSk")
# auth = mendeley.start_client_credentials_flow()
# session = auth.authenticate()

# Create flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(queryResults = None):
	if request.method == "POST":
		print("query:", request.form["query"])
		query = request.form["query"]
		
		# # Search for relevant articles
		# rawQueryResults = resources.catalog.Catalog.search(query).iter()

		queryResults = "query"
	return render_template("index.html", queryResults=queryResults) 
@app.route("/test")
def test():
	return "test"
