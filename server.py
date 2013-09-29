from flask import Flask, render_template, request
from quotes import get_random_quote
from json import dumps

app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    color = request.form["color"]
    name = request.form["name"]
    task = request.form["task"]
    quote = get_random_quote(task)
    return render_template("quote.html", color=color, name=name, task=task, quote=quote)

