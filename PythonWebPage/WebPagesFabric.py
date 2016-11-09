import WebPages.XKomPage as XkomPage
import WebPages.AltoPage as AltoPage
import WebPages.ProlinePage as ProlinePage
import WebPages.MorelePage as MorelePage
import WebPages.KomputronikPage as KomputronikPage
import WebPages.HelionPage as HelionPage
import WebPages.IBoodPage as IBoodPage
import WebPages.MallPage as MallPage
import WebPages

xkom = "x-kom"
alto = "alto"
komputronik = "komputronik"
proline = "proline"
morele = "morele"
helion = "helion"
mall = "mall"
ibood = "ibood"
onepress = "one press"
sensus = "sensus"
septem = "septem"

def RetuNewHotShots(selectedPage):

	if selectedPage == xkom:
		hotShotsCollection = WebPages.XKomPage.XkomPage()
	elif selectedPage == alto:
		hotShotsCollection = WebPages.AltoPage.AltoPage()
	elif selectedPage == komputronik:
		hotShotsCollection = WebPages.KomputronikPage.KomputronikPage()
	elif selectedPage == proline:
		hotShotsCollection = WebPages.ProlinePage.ProlinePage()
	elif selectedPage == morele:
		hotShotsCollection = WebPages.MorelePage.MorelePage()
	elif selectedPage == helion:
		hotShotsCollection = WebPages.HelionPage.HelionPage()
	elif selectedPage == mall:
		hotShotsCollection = WebPages.MallPage.MallPage()
	elif selectedPage == ibood:
		hotShotsCollection = WebPages.IBoodPage.IBoodPage()
	elif selectedPage == onepress:
		hotShotsCollection = WebPages.OnePressPage.OnePressPage()
	elif selectedPage == sensus:
		hotShotsCollection = WebPages.SensusPage.SensusPage()
	elif selectedPage == septem:
		hotShotsCollection = WebPages.SeptemPage.SeptemPage()
	
	if hotShotsCollection != None:
		return hotShotsCollection.GetWebPageData()
