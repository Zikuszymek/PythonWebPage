import MySQL.AllWebPages as AllWebPages
import WebPagesFabric


#listOfAllPages = [AllWebPages.xkom, AllWebPages.alto, AllWebPages.komputronik, AllWebPages.morele,
#				  AllWebPages.proline, AllWebPages.helion, AllWebPages.onepress, AllWebPages.sensus,
#				  AllWebPages.septem, AllWebPages.ibood, AllWebPages.mall]
listOfAllPages = [AllWebPages.othertees,]

dbManager = AllWebPages.DatabaseManager()
for webpage in listOfAllPages:
	print("\nchecking - " + webpage)
	resultlist = WebPagesFabric.RetuNewHotShots(webpage)
	if resultlist != None:
		dbhotShotList = dbManager.GetAllRecordsFromWebPage(webpage)
		if not dbhotShotList.count() > 0:
			print("no db records")
			for hotshot in resultlist:
				print("adding record for - " + webpage)
				dbManager.AddNewHotShot(webpage, hotshot["productName"],hotshot["oldPrice"],hotshot["newPrice"],hotshot["productUrl"],hotshot["imgUrl"])
		else:
			print("db records exist")
			for index, hotshot in enumerate(resultlist):
				print("upgrade record for - " + webpage)
				hotShotIndex = dbhotShotList[index].id_hot_shot
				dbManager.UpgradeExistingHotShot(hotShotIndex, webpage, hotshot["productName"],hotshot["oldPrice"],hotshot["newPrice"],hotshot["productUrl"],hotshot["imgUrl"])