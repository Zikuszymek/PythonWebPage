import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class KomputronikPage(WebPage.WebPages):

	webPageUrl = 'http://www.komputronik.pl/'

	def __init__(self):
		WebPage.WebPages.__init__(self, KomputronikPage.webPageUrl)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			self.productUrl = soup.select("#occasion0 .name")[0].get("href")
			hotShotSoup = WebPage.GetParsedSoupFromURL(self.productUrl)

			self.productName = hotShotSoup.select(".name")[0].text

			self.oldPrice = hotShotSoup.select(".oldPrice")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".innerPriceValue")[0].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.imgUrl = "http:" + hotShotSoup.select(".newFullView .photo img")[0].get("src")

		except Exception as ex:
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"

		oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
		list = (oneElement,)
		return list