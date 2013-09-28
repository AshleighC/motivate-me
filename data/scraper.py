# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from json import dumps
from unicodedata import normalize
from urllib import urlopen

def unicode_to_ascii(text):
  return normalize("NFKD", text).encode("ascii", "ignore")

def get_quote_details(text):
  index = text.rfind(u"–")
  quote = unicode_to_ascii(text[:index - 1])
  author = unicode_to_ascii(text[index + 1:])
  return {"quote": quote, "author": author}

def get_quotes():
  url = "http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/"
  soup = BeautifulSoup(urlopen(url).read())
  quotes = []
  for li in soup.find("ol").find_all("li"):
    quotes.append(get_quote_details(li.get_text()))
  return quotes

json = open("quotes.json", "w")
json.write(dumps(get_quotes()))
json.close()

