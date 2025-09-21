import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
import os

api_key = os.environ.get("API_KEY")

app = Flask(__name__)
bootstrap = Bootstrap5(app=app)



@app.route("/", methods=["GET","POST"])
def home():
    search_key = request.form.get("enter")
    if search_key:
        return redirect(url_for("search",search_value=search_key))
    parameter = {
        "apiKey": api_key,
        "language": "en",
    }
    response = requests.get("https://newsapi.org/v2/top-headlines", params=parameter)
    lis = response.json()["articles"]
    return render_template("home.html",articles=lis, title="Todays Top News")

@app.route("/<search_value>",methods=["GET","POST"])
def search(search_value):
    search_key = request.form.get("enter")
    if search_key:
       return redirect(url_for("search", search_value=search_key))
    parameter = {
        "apiKey": api_key,
        "q": search_value
    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameter)
    lis = response.json()["articles"]
    return render_template("home.html", articles=lis, title=search_value)

if __name__ == "__main__":
    app.run(debug=True)