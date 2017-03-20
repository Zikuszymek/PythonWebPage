import WebPages.WebPages as WebPage
import MySQL.DatabaseManager as DatabaseManager
from bs4 import BeautifulSoup

class ProlinePage(WebPage.WebPages):
	imgUrlPrevix = "https://proline.pl"

	def __init__(self):
		WebPage.WebPages.__init__(self, DatabaseManager.prolineURL)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select("#headshot")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv.encode('utf-8')),'html.parser')

			self.productName = hotShotSoup.select("a")[1].text
			self.productName = WebPage.GetNameFromString(self.productName)

			tableInfo = hotShotSoup.select("#karta")
			tableInfo = BeautifulSoup(str(tableInfo),'html.parser')

			self.oldPrice = tableInfo.select("tr > td > b")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = tableInfo.select("tr > td > b")[1].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.productUrl = hotShotSoup.select(".fotka")[0].get("href")

			self.imgUrl = ProlinePage.imgUrlPrevix + hotShotSoup.select(".fotka img")[0].get("src")

		except Exception as ex:
			print("error")
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"

		oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
		list = (oneElement,)
		return list