from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/release")
def release():
    return render_template("release.html")

@app.route("/pre_sale")
def pre_sale():
    return render_template("pre-sale.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/contate")
def contate():
    return render_template("contate.html")
    
if __name__ == "__main__":
    app.run(debug=True)