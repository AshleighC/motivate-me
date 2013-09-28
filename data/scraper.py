# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from json import dumps
from urllib import urlopen

def get_quote_details(text):
  index = text.rfind(u"–")
  return {"quote": text[:index - 1], "author": text[index + 1:]}

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

