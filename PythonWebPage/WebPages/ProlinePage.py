import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class ProlinePage(WebPage.WebPages):

	webPageUrl = 'https://proline.pl/'
	imgUrlPrevix = "https://proline.pl/pic/"

	def __init__(self):
		WebPage.WebPages.__init__(self, ProlinePage.webPageUrl)

	def GetWebPageData(self):
		try:
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select("#headshot")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv.encode('utf-8')),'html.parser')

			self.productName = hotShotSoup.select("a")[1].text

			tableInfo = hotShotSoup.select("#karta")
			tableInfo = BeautifulSoup(str(tableInfo),'html.parser')

			self.oldPrice = tableInfo.select("tr > td > b")[0].text
			self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

			self.newPrice = tableInfo.select("tr > td > b")[1].text
			self.newPrice = WebPage.GetPriceFromString(self.newPrice)

			self.productUrl = hotShotSoup.select(".fotka")[0].get("href")

			self.imgUrl = imgUrlPrevix + hotShotSoup.select(".fotka img")[0].get("src")

		except Exception as ex:
			print("error")
			self.oldPrice = "0"
			self.newPrice = "0"
			self.productName = "-"
			self.productUrl = "-"
			self.imgUrl = "-"