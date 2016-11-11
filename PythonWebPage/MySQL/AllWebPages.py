from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, query, Query
from sqlalchemy import create_engine
import datetime


xkom = 'x-kom'
alto = 'alto'
komputronik = 'komputronik'
proline = 'proline'
morele = 'morele'
helion = 'helion'
mall = 'mall'
ibood = 'ibood'
onepress = 'one press'
sensus = 'sensus'
septem = 'septem'

xkomURL = 'http://www.x-kom.pl/'
altoURL = 'http://www.al.to/'
komputronikURL = 'http://www.komputronik.pl/'
prolineURL = 'https://proline.pl/'
moreleURL = 'https://www.morele.net/'
helionURL = 'http://helion.pl/'
mallURL = 'https://www.mall.pl/'
iboodURL = 'http://www.ibood.com/pl/pl/'
onepressURL = 'http://onepress.pl/'
sensusURL = 'http://sensus.pl/'
septemURL = 'http://septem.pl/'

categoryElectonics = 'electronics'
categoryBooks = 'books'
categoryOther = 'other'

categoryList = [categoryElectonics,categoryBooks,categoryOther]

class DatabaseManager():

	def __init__(self):
		Base = automap_base()
		dbAdress = 'mysql+pymysql://ziku_hotshot:moniqe21@ziku.ayz.pl:3306/ziku_hotshot?charset=utf8'
		engine = create_engine(dbAdress,echo=False)

		Base.prepare(engine, reflect=True)

		self.WebPages = Base.classes.web_pages
		self.WebPagesCategory = Base.classes.web_page_category
		self.HotShotList = Base.classes.hot_shot_list

		self.session = Session(engine)

	def GetAllRecordsFromWebPage(self, webPage):
		webPage = self.session.query(self.WebPages).filter(self.WebPages.name_web_page == webPage)
		hotShots = self.session.query(self.HotShotList).filter(self.HotShotList.web_page_id == webPage[0].id_web_page)
		return hotShots

	def AddNewHotShot(self, webPage, productName, oldPrice, newPrice, productURL, imgUrl):
		time = datetime.datetime.now()
		webPage = self.session.query(self.WebPages).filter(self.WebPages.name_web_page == webPage)
		self.session.add(self.HotShotList(product_name = productName, old_price = oldPrice, new_price = newPrice,
					web_page_id = webPage[0].id_web_page, product_url = productURL, img_url = imgUrl, last_check = time))
		self.session.commit()
		self.session.flush()

	def UpgradeExistingHotShot(self, hotShotId, webPage, productName, oldPrice, newPrice, productURL, imgUrl):
		time = datetime.datetime.now()
		webPage = self.session.query(self.WebPages).filter(self.WebPages.name_web_page == webPage)
		self.session.merge(self.HotShotList(id_hot_shot = hotShotId, product_name = productName, old_price = oldPrice, new_price = newPrice,
					web_page_id = webPage[0].id_web_page, product_url = productURL, img_url = imgUrl, last_check = time))
		self.session.commit()
		self.session.flush()

	def IfWebPageDoesNotExistCreate(self, pageName,pageURL,isActive,category):
		q = self.session.query(self.WebPages).filter(self.WebPages.name_web_page == pageName)
		category = self.session.query(self.WebPagesCategory).filter(self.WebPagesCategory.category_type == category)
		if not q.count() > 0:
			print("adding new web page - " + pageName)
			self.session.add(self.WebPages(name_web_page = pageName,url_web_page = pageURL, is_active_page = isActive, web_page_category = category[0].idweb_page_category ))
			self.session.commit()
			self.session.flush()

		else:
			print("this web page - " + pageName + " - already exists")

	def CreateCategoryIfDoesNotExist(self, category):
		q = self.session.query(self.WebPagesCategory).filter(self.WebPagesCategory.category_type == category)
		if not q.count() > 0:
			print("adding new category - " + category)
			self.session.add(self.WebPagesCategory(category_type = category))
			self.session.commit()
			self.session.flush()

		else:
			print("this category - " + category + " - already exists")

	def AddAllCategories(self):
		for category in categoryList:
			self.CreateCategoryIfDoesNotExist(category)

	def AddAllWebPages(self):
		self.IfWebPageDoesNotExistCreate(xkom,xkomURL,True,categoryElectonics)
		self.IfWebPageDoesNotExistCreate(alto, altoURL, True, categoryOther)
		self.IfWebPageDoesNotExistCreate(morele, moreleURL, True, categoryElectonics)
		self.IfWebPageDoesNotExistCreate(proline, prolineURL, True, categoryElectonics)
		self.IfWebPageDoesNotExistCreate(komputronik, komputronikURL, True, categoryElectonics)
		self.IfWebPageDoesNotExistCreate(mall, mallURL, True, categoryOther)
		self.IfWebPageDoesNotExistCreate(ibood, iboodURL, True, categoryOther)
		self.IfWebPageDoesNotExistCreate(onepress, onepressURL, True, categoryBooks)
		self.IfWebPageDoesNotExistCreate(helion, helionURL, True, categoryBooks)
		self.IfWebPageDoesNotExistCreate(sensus, sensusURL, True, categoryBooks)
		self.IfWebPageDoesNotExistCreate(septem, septem, True, categoryBooks)
