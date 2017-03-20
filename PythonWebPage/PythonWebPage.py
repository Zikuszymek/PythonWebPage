import MySQL.DatabaseManager as DatabaseManager
import WebPagesFabric


listOfAllPages = [DatabaseManager.xkom, DatabaseManager.alto, DatabaseManager.komputronik, DatabaseManager.morele,
				  DatabaseManager.proline, DatabaseManager.helion, DatabaseManager.onepress, DatabaseManager.sensus,
				  DatabaseManager.septem, DatabaseManager.ibood, DatabaseManager.mall, DatabaseManager.othertees]

dbManager = DatabaseManager.DatabaseManager()
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