from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

def ConnectToDB():
	dbAdress = "mysql+pymysql://ziku_hotshot:moniqe21@ziku.ayz.pl:3306"
	engine = create_engine(dbAdress)
	connection = engine.connect()
	result = connection.execute("SELECT * FROM ziku_hotshot.web_pages")
	for row in result:
		print(row)