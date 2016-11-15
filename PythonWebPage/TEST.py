import MySQL.AllWebPages as AllWebPages
import WebPagesFabric
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, query, Query
from sqlalchemy import create_engine
import datetime



listOfAllPages = [AllWebPages.xkom, AllWebPages.alto, AllWebPages.komputronik, AllWebPages.morele,
				  AllWebPages.proline, AllWebPages.helion, AllWebPages.onepress, AllWebPages.sensus,
				  AllWebPages.septem, AllWebPages.ibood, AllWebPages.mall]

Base = automap_base()
dbAdress = 'mysql+pymysql://ziku_hotshot:moniqe21@localhost:3306/ziku_hotshot?charset=utf8'
engine = create_engine(dbAdress,echo=False)

Base.prepare(engine, reflect=True)

#WebPages = Base.classes.web_pages
#WebPagesCategory = Base.classes.web_page_category
#HotShotList = Base.classes.hot_shot_list

#session = Session(engine)

for webpage in listOfAllPages:
	print("\nchecking - " + webpage)
	resultlist = WebPagesFabric.RetuNewHotShots(webpage)
	if resultlist != None:
		for hotshot in resultlist:
			print(hotshot["productName"])
			print(hotshot["oldPrice"])
			print(hotshot["newPrice"])
			print(hotshot["productUrl"])
			print(hotshot["imgUrl"])


