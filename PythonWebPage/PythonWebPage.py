import MySQL.Alchemy as Alchemy
import WebPagesFabric

resultlist = WebPagesFabric.RetuNewHotShots(WebPagesFabric.mall)
if resultlist != None:
	for hotshot in resultlist:
		print(hotshot["productName"].encode('utf-8'))
		print(hotshot["oldPrice"])
		print(hotshot["newPrice"])
		print(hotshot["productUrl"])
		print(hotshot["imgUrl"])