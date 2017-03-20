import WebPages.WebPages as WebPage
import MySQL.DatabaseManager as DatabaseManager
from bs4 import BeautifulSoup

class OnePressPage(WebPage.WebPages):

	def __init__(self):
		WebPage.WebPages.__init__(self, DatabaseManager.onepressURL)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			self.productUrl = soup.select(".box-promotion .cover a")[0].get("href")
			hotShotSoup = WebPage.GetParsedSoupFromURL(self.productUrl)

			self.productName = hotShotSoup.select(".book_title span")[0].text
			self.productName = WebPage.GetNameFromString(self.productName)

			self.oldPrice = hotShotSoup.select(".price del")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".price span")[0].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.imgUrl = hotShotSoup.select(".book_info img")[1].get("src")

		except Exception as ex:
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"

		oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
		list = (oneElement,)
		return list