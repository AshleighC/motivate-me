from json import loads, dumps

def print_quote(quote):
  print '"' + quote["quote"] + '"'
  print "   - " + quote["author"]

def get_word():
  return raw_input(">> ")

def get_quote_words(quote):
  print_quote(quote)
  words = []
  word = get_word()
  while word != "":
    words.append(word)
    word = get_word()
  return words

def get_word_list():
  data = loads(open("quotes.json").read())
  wordlist = []
  print
  for quote in data:
    wordlist.append(get_quote_words(quote))
    print
  return wordlist

json = open("words.json", "w")
json.write(dumps(get_word_list()))
json.close()
