import WebPages.WebPages as WebPage
from bs4 import BeautifulSoup

class ProlinePage(WebPage.WebPages):

	webPageUrl = 'https://proline.pl/'

	def __init__(self):
		WebPage.WebPages.__init__(self, ProlinePage.webPageUrl)

	def GetWebPageData(self):
		#try:
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select("#headshot")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv.encode('utf-8')),'html.parser')

			print(hotShotDiv.encode('utf-8'))
			self.productName = hotShotSoup.select(".a")[1].text

			#self.oldPrice = hotShotSoup.select(".old-price")[0].text
			#self.oldPrice = webPage.GetPriceFromString(self.oldPrice)

			#self.newPrice = hotShotSoup.select(".new-price")[0].text
			#self.newPrice = webPage.GetPriceFromString(self.newPrice)

			#self.productUrl = self.webUrl

			#self.imgUrl = hotShotSoup.select(".img-responsive")[0]
			#self.imgUrl = self.imgUrl.get('src')

		#except Exception as ex:
			#print("error")
			#self.oldPrice = "0"
			#self.newPrice = "0"
			#self.productName = "-"
			#self.productUrl = "-"
			#self.imgUrl = "-"