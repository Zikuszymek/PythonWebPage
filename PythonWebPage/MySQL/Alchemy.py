from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def ConnectToDB():

	Base = automap_base()
	dbAdress = 'mysql+pymysql://ziku_hotshot:moniqe21@ziku.ayz.pl:3306/ziku_hotshot'
	engine = create_engine(dbAdress,echo=True)

	Base.prepare(engine, reflect=True)

	WebPages = Base.classes.web_pages
	WebPagesCategory = Base.classes.web_page_category
	HotShotList = Base.classes.hot_shot_list

