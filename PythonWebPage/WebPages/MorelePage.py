import WebPages.WebPages as WebPage
import MySQL.AllWebPages as AllWebPages
from bs4 import BeautifulSoup

class MorelePage(WebPage.WebPages):

	def __init__(self):
		WebPage.WebPages.__init__(self, AllWebPages.moreleURL)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select(".promotion-product")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

			self.productName = hotShotSoup.select(".product-name a")[0].text

			self.oldPrice = hotShotSoup.select(".product-price span")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".product-price span")[1].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)
		
			self.productUrl = hotShotSoup.select(".product-name a")[0].get("href")

			productpage = WebPage.GetParsedSoupFromURL(self.productUrl)
			self.imgUrl = productpage.select("#light_gallery img")[0].get("src")

		except Exception as ex:
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"

		oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
		list = (oneElement,)
		return list