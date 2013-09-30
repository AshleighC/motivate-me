from flask import Flask, render_template, request
from quotes import get_quote

app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_index()
  else:
    return render_quote(request.form)

""" NEW STUFF, NOT DONE YET """
@app.route("/quote/", methods=["GET", "POST"])
def quote():
  if request.method == "GET":
    # TODO(ashleigh): Check for query string parameters
    pass
  else:
    return render_quote(request.form)

@app.route("/<index>", methods=["GET", "POST"])
def show_quote(index):
  if request.method == "GET":
    return render_index(index)
  else:
    return render_quote(request.form, index)

def render_index(index=""):
  action = "/quote/%s" % index
  return render_template("index.html", action=action)

def render_quote(form, index=None):
  return render_template("quote.html",
      color=form["color"], name=form["name"].title(), task=form["task"],
      quote=get_quote(form["task"], index))

