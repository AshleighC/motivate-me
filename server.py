from flask import Flask, render_template, request
from quotes import get_random_quote

app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    name = request.form["name"]
    quote = get_random_quote()
    return render_template("quote.html", name=name, quote=quote)

