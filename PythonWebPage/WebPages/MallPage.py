import WebPages.WebPages as WebPage
import MySQL.AllWebPages as AllWebPages
from bs4 import BeautifulSoup

class MallPage(WebPage.WebPages):

	def __init__(self):
		WebPage.WebPages.__init__(self, AllWebPages.mallURL)

	def GetWebPageData(self):

			list = []
		
			soup = BeautifulSoup(self.html, 'html.parser')
			hotShotDiv = soup.select(".deal-wrapper")[0]
			hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

			productList = hotShotSoup.select('.deal-item')

			for element in productList:
				soupElement = BeautifulSoup(str(element),'html.parser')
				
				if soupElement.find('a'):
					try:
						self.productName = soupElement.select('a')[1].text

						self.oldPrice = soupElement.select("del")[0].text
						self.oldPrice = WebPage.GetPriceFromString(self.oldPrice)

						self.newPrice = soupElement.select(".deal-price")[0].text
						self.newPrice = WebPage.GetPriceFromString(self.newPrice)
	
						self.productUrl = 'https://www.mall.pl' + soupElement.select('a')[1].get('href')

						self.imgUrl = soupElement.select('a img')[0].get('data-src')

					except Exception as ex:
						self.oldPrice = "0"
						self.newPrice = "0"
						self.productName = "-"
						self.productUrl = "-"
						self.imgUrl = "-"

					oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
					list.append(oneElement)

			return list