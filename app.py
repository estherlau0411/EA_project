from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
   return render_template("index.html")

@app.route("/")
@app.route("/movie")
def movie():
   return render_template("movie.html")