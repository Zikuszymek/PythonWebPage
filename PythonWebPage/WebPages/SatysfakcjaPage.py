import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class SatysfakcjaPage(WebPage.WebPages):

	webPageUrl = 'http://www.al.to/'

	def __init__(self):
		WebPage.WebPages.__init__(self, SatysfakcjaPage.webPageUrl)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select("#hotShot")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

			self.productName = hotShotSoup.select(".product-name")[0].text

			self.oldPrice = hotShotSoup.select(".old-price")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".new-price")[0].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.productUrl = self.webUrl

			self.imgUrl = hotShotSoup.select(".img-responsive")[0]
			self.imgUrl = self.imgUrl.get('src')

		except Exception as ex:
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"
        