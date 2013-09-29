from json import loads
from random import randint
from re import compile, sub

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

def get_index(index, max_index):
  return int(index) if index_valid(index, max_index) else randint(0, max_index)

def format_regex(word):
  return compile("\\b%ss?\\b" % word)

def correct_case(word, task):
  return task.title() if word.istitle() else task.lower()

def replace_words(quote, words, task):
  for word in words:
    quote = sub(format_regex(word), correct_case(word, task), quote)
  return quote

def get_quote(task, index):
  quotes = read_json("data/quotes.json")
  max_index = len(quotes) - 1
  index = get_index(index, max_index)
  words = read_json("data/words.json")[index]
  quote = quotes[index]
  quote["quote"] = replace_words(quote["quote"], words, task)
  return quote

