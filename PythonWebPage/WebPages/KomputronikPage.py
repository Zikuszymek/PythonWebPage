import WebPages.WebPages as WebPage
import MySQL.DatabaseManager as DatabaseManager
from bs4 import BeautifulSoup

class KomputronikPage(WebPage.WebPages):

	def __init__(self):
		WebPage.WebPages.__init__(self, DatabaseManager.komputronikURL)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')

			print("dupa")
			#print(soup)
			textowo = soup.select(".content")[0]
			print (textowo.encode("utf-8"))

			print("dupa po")

			self.productUrl = soup.select("#occasion0 .name")[0].get("href")
			hotShotSoup = WebPage.GetParsedSoupFromURL(self.productUrl)

			self.productName = hotShotSoup.select(".name")[0].text
			self.productName = WebPage.GetNameFromString(self.productName)

			self.oldPrice = hotShotSoup.select(".oldPrice")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = hotShotSoup.select(".innerPriceValue")[0].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.imgUrl = "http:" + hotShotSoup.select(".newFullView .photo img")[0].get("src")

		except Exception as ex:

			print(ex)
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"

		oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
		list = (oneElement,)
		return list