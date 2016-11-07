import webPage
from bs4 import BeautifulSoup

class SatysfakcjaPage(webPage.WebPage):

    webPageUrl = 'http://www.satysfakcja.pl/'

    def GetWebPageData(self):
       soup = BeautifulSoup(self.html, 'html.parser')
       hotShotDiv = soup.select("#hotShot")[0]
       hotShotSoup = BeautifulSoup(str(hotShotDiv),'html.parser')

       productName = hotShotSoup.select(".product-name")[0].text

       oldPrice = hotShotSoup.select(".old-price")[0].text
       oldPrice = webPage.GetPriceFromString(oldPrice)

       newPrice = hotShotSoup.select(".new-price")[0].text
       newPrice = webPage.GetPriceFromString(newPrice)

       productUrl = self.webUrl

       imgUrl = hotShotSoup.select(".img-responsive")[0]
       imgUrl = imgUrl.get('src')
       print(imgUrl)
        