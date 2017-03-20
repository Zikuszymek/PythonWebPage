import WebPages.WebPages as WebPage
import MySQL.DatabaseManager as DatabaseManager
from bs4 import BeautifulSoup

class IBoodPage(WebPage.WebPages):

	webPageUrl = DatabaseManager.iboodURL
	webPageUrl2 = 'http://www.ibood.com/home-living-pl/pl/'
	webPageUrl3 = 'http://www.ibood.com/sports-fashion-pl/pl/'
	webPAgeUrl4	= 'http://www.ibood.com/extra-pl/pl/'

	def __init__(self):
		WebPage.WebPages.__init__(self, IBoodPage.webPageUrl)

	def GetWebPageData(self):

		hotShotPageList = (IBoodPage.webPageUrl, IBoodPage.webPageUrl2, IBoodPage.webPageUrl3, IBoodPage.webPAgeUrl4)
		list = []

		for webPageElement in hotShotPageList:
			try:
				soup = WebPage.GetParsedSoupFromURL(webPageElement)
				hotShotDiv = soup.select(".primary-offer")[0]
				hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

				self.productName = hotShotSoup.select("span")[0].text
				self.productName = WebPage.GetNameFromString(self.productName)

				self.oldPrice = hotShotSoup.select(".old-price span")[1].text
				self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

				self.newPrice = hotShotSoup.select(".new-price")[0].text
				self.newPrice = WebPage.GetPriceFromString(self.newPrice)
		
				self.productUrl = webPageElement

				self.imgUrl = 'http:' + hotShotSoup.select(".offer-img a img")[0].get("src")

			except Exception as ex:
				self.oldPrice = "0"
				self.newPrice = "0"
				self.productName = "-"
				self.productUrl = "-"
				self.imgUrl = "-"

			oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
			list.append(oneElement)

		return list