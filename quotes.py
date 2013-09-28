from json import loads
from random import randint

def get_random_quote():
  data = loads(open("data/quotes.json").read())
  return data[randint(0, len(data) - 1)]

