import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class HelionPage(WebPage.WebPages):

	webPageUrl = 'http://helion.pl/'

	def __init__(self):
		WebPage.WebPages.__init__(self, HelionPage.webPageUrl)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			self.productUrl = soup.select(".promotion-book a")[0].get("href")
			hotShotSoup = WebPage.GetParsedSoupFromURL(self.productUrl)

			self.productName = hotShotSoup.select(".book-details h1")[0].text

			self.oldPrice = hotShotSoup.select(".book-type-price del")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".book-type-price ins")[0].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.imgUrl = hotShotSoup.select(".book-details .cover-col img")[0].get("src")

		except Exception as ex:
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"