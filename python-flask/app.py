from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		print("query:", request.form["query"])
		return redirect(url_for("index"))
	return render_template("index.html") 
@app.route("/test")
def test():
	return "test"
