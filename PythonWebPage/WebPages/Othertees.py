import WebPages.WebPages as WebPage
import MySQL.DatabaseManager as DatabaseManager
import re
from bs4 import BeautifulSoup


class OtherteesPage(WebPage.WebPages):

	def __init__(self):
		WebPage.WebPages.__init__(self, DatabaseManager.otherteesURL)

	def GetWebPageData(self):

		emptyElement = WebPage.CreateSingleDictionary("-","0","0","-","-")
		list = []
		list.append(emptyElement)
		list.append(emptyElement)
		list.append(emptyElement)
		list.append(emptyElement)

		soup = WebPage.GetParsedSoupForOthertees()
		#Referer http://www.othertees.com/?lang=pl
		specialList = soup.findAll('div', id=re.compile('^design-\d+$'))

		for indexOf, othertee in enumerate(specialList):
			try:
				hotShotSoup = BeautifulSoup(str(othertee),'html.parser')
				#print(hotShotSoup)

				self.productName = hotShotSoup.select(".product-options h4")[0].text
				self.productName = WebPage.GetNameFromString(self.productName)


				przez = "przez"
				if przez in self.productName:
					index = self.productName.find(przez)
					if index >= 0:
						self.productName = self.productName[0:index]

				self.oldPrice = "0"

				self.newPrice = hotShotSoup.select(".product-price span")[0].text
				dot = "."
				if dot in self.newPrice:
					index = self.newPrice.find(dot)
					if index >= 0:
						self.newPrice = self.newPrice[0:index]

				self.newPrice = WebPage.GetPriceFromString(self.newPrice)
		
				self.productUrl = AllWebPages.otherteesURL

				self.imgUrl = 'http://www.othertees.com' + hotShotSoup.select("img")[0].get("src")

			except Exception as ex:
				self.oldPrice = "0"
				self.newPrice = "0"
				self.productName = "-"
				self.productUrl = "-"
				self.imgUrl = "-"

			oneElement = WebPage.CreateSingleDictionary(self.productName, self.oldPrice, self.newPrice, self.imgUrl, self.productUrl)
			list[indexOf] = oneElement

		return list