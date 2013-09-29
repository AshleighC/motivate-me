from json import loads
from random import randint
from re import compile, sub

# ----- STUFF FOR TESTING, REMOVE LATER -----

def print_quote(quote):
  print '"' + quote["quote"] + '"'
  print "   - " + quote["author"]

def print_all_quotes(task):
  quotes = read_json("data/quotes.json")
  for index in range(len(quotes) - 1):
    words = read_json("data/words.json")[index]
    quote = quotes[index]
    quote["quote"] = replace_words(quote["quote"], words, task)
    print "(%d)" % index
    print_quote(quote)
    print

# ----- END TESTING STUFF -----

def read_json(path):
  f = open(path)
  data = loads(f.read())
  f.close()
  return data

def index_valid(index, max_index):
  try:
    index = int(index)
    return (index >= 0) and (index <= max_index)
  except:
    return False

def random_index(max_index):
  return randint(0, max_index)

def format_regex(word):
  regex = compile("\\b%ss?\\b" % word)
  return regex

def correct_case(word, task):
  return task.title() if word.istitle() else task.lower()

def replace_words(quote, words, task):
  for word in words:
    quote = sub(format_regex(word), correct_case(word, task), quote)
  return quote

def get_quote(task, index):
  quotes = read_json("data/quotes.json")
  max_index = len(quotes) - 1
  index = int(index) if index_valid(index, max_index) else random_index(max_index)
  words = read_json("data/words.json")[index]
  quote = quotes[index]
  quote["quote"] = replace_words(quote["quote"], words, task)
  return quote

