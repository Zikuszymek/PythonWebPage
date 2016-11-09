import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class OnePressPage(WebPage.WebPages):

	webPageUrl = 'https://www.mall.pl/'

	def __init__(self):
		WebPage.WebPages.__init__(self, IBoodPage.webPageUrl)

	def GetWebPageData(self):

		hotShotPageList = (OnePressPage.webPageUrl)
		list = []

		for webPageElement in hotShotPageList:
			try:
				soup = WebPage.GetParsedSoupFromURL(webPageElement)
				hotShotDiv = soup.select(".primary-offer")[0]
				hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

				self.productName = hotShotSoup.select("span")[0].text

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