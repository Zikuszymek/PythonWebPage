import MySQL.AllWebPages as AllWebPages
import WebPagesFabric



listOfAllPages = [WebPagesFabric.xkom, WebPagesFabric.alto, WebPagesFabric.komputronik, WebPagesFabric.morele,
				  WebPagesFabric.proline, WebPagesFabric.helion, WebPagesFabric.onepress, WebPagesFabric.sensus,
				  WebPagesFabric.septem, WebPagesFabric.ibood, WebPagesFabric.mall]

dbManager = AllWebPages.DatabaseManager()
#dbManager.AddAllWebPages()
for webpage in listOfAllPages:
	resultlist = WebPagesFabric.RetuNewHotShots(webpage)
	if resultlist != None:
		dbhotShotList = dbManager.GetAllRecordsFromWebPage(webpage)
		if dbhotShotList.count() > 0:
			for hotshot in resultlist:

		else:
			print("nie ma")
		#for hotshot in resultlist:
			#print(hotshot["productName"].encode('utf-8'))
			#print(hotshot["oldPrice"])
			#print(hotshot["newPrice"])
			#print(hotshot["productUrl"])
			#print(hotshot["imgUrl"])