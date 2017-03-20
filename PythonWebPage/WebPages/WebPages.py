from bs4 import BeautifulSoup
import urllib.request
import re

class WebPages(object):

	def __init__(self, webUrl):
		self.oldPrice = "0"
		self.newPrice = "0"
		self.productName = "-"
		self.productUrl = "-"
		self.imgUrl = "-"
		self.webUrl = webUrl
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		headers={'User-Agent':user_agent,} 
		req = urllib.request.Request(webUrl,None,headers)
		self.requestReceived = urllib.request.urlopen(req)
		self.html = self.requestReceived.read()
		#print(requestReceived.getheader('Set-Cookie'))


	def GetWebPageData(self):
		raise NotImplementedError("Subclass must implement GetWebPageData method")

	def PritDetails(self):
		print("old price: " + self.oldPrice)
		print("new price: " + self.newPrice)
		print("product name: " + self.productName)
		print("product url: " + self.productUrl)
		print("image url: " + self.imgUrl)

def GetParsedSoupFromURL(providedURL):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,} 
	req = urllib.request.Request(providedURL,None,headers)
	html = urllib.request.urlopen(req).read()
	return BeautifulSoup(html, 'html.parser')

def GetParsedSoupForOthertees():
	reference = 'http://www.othertees.com/?lang=pl'
	providedURL = 'http://www.othertees.com/checkout/currency/pln/'
	cookies = 'PHPSESSID=dupadupacycli123212; sugesterChatToken10804=4q55a01c58o85iz2aaapip; ip10804=178.37.15.26; OtherTeesUserCountryCode=pl'
	languages = 'pl,en-US;q=0.7,en;q=0.3'

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,'Cookie': cookies, 'Referer': reference} 
	req = urllib.request.Request(providedURL,None,headers)
	requestReceived = urllib.request.urlopen(req)
	html = requestReceived.read()
	return BeautifulSoup(html, 'html.parser')

def GetNameFromString(nameString):
	nameString = nameString.replace("\n","").strip();
	return nameString

def GetPriceFromString(priceString):

	firstChar = 'z'
	secondChar = ','
	if firstChar in priceString:
		index = priceString.find(firstChar)
		if index >= 0:
			priceString = priceString[0:index - 1]

	if secondChar in priceString:
		index = priceString.find(secondChar)
		if index >= 0:
			priceString = priceString[0:index]

	priceString = priceString.replace("\\s+","")
	priceString = priceString.replace(".","")
	priceString = priceString.replace(" ","")
	priceString = re.sub(r'\s+','',priceString)
	print(priceString)

	return priceString

def CreateSingleDictionary(productName, oldPrice, newPrice, imgUrl, productUrl):
	dictionary = {'productName' : productName , 'oldPrice' : oldPrice , 'newPrice' : newPrice , 'imgUrl' : imgUrl , 'productUrl' : productUrl}
	return dictionary

