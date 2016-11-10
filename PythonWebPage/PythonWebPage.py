import MySQL.AllWebPages as AllWebPages
import WebPagesFabric



listOfAllPages = [WebPagesFabric.xkom, WebPagesFabric.alto, WebPagesFabric.komputronik, WebPagesFabric.morele,
				  WebPagesFabric.proline, WebPagesFabric.helion, WebPagesFabric.onepress, WebPagesFabric.sensus,
				  WebPagesFabric.septem, WebPagesFabric.ibood, WebPagesFabric.mall]

dbManager = AllWebPages.DatabaseManager()
#dbManager.AddAllWebPages()
for webpage in listOfAllPages:
	print("sprawdzanie - " + webpage)
	resultlist = WebPagesFabric.RetuNewHotShots(webpage)
	if resultlist != None:
		dbhotShotList = dbManager.GetAllRecordsFromWebPage(webpage)
		if not dbhotShotList.count() > 0:
			print("nie ma wpisów")
			for hotshot in resultlist:
				dbManager.AddNewHotShot(webpage, hotshot["productName"].encode('utf-8'),hotshot["oldPrice"],hotshot["newPrice"],hotshot["productUrl"],hotshot["imgUrl"])
		else:
			print("nie ma")
		#for hotshot in resultlist:
			#print(hotshot["productName"].encode('utf-8'))
			#print(hotshot["oldPrice"])
			#print(hotshot["newPrice"])
			#print(hotshot["productUrl"])
			#print(hotshot["imgUrl"])