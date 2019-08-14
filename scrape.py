import requests
import json

from bs4 import BeautifulSoup

class Scraper:

	def __init__(self):
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.link = 'http://www.theofficelife.com/business-jargon-dictionary-{}.html'
		self.words = {}

	def scrape(self):
		for letter in self.alphabet:
			print(f'On Letter: {letter}')
			self._scrape(self.link.format(letter))
		json.dump(self.words, open('data.json', 'w'))

	def _scrape(self, link):
		soup = BeautifulSoup(requests.get(link).text, 'lxml')
		words = soup.select('table.dictionary > tr')
		for word in words:
			if 'adsbygoogle' not in str(word):
				self.words[word.td.b.text] = word.select('td')[1].text

Scraper().scrape()
