import WebPages.XKomPage as XkomPage
import WebPages.AltoPage as AltoPage
import WebPages.ProlinePage as ProlinePage
import WebPages.MorelePage as MorelePage
import WebPages.KomputronikPage as KomputronikPage
import WebPages.HelionPage as HelionPage
import WebPages.IBoodPage as IBoodPage
import WebPages.MallPage as MallPage
import WebPages.OnePressPage as OnePressPage
import WebPages.SensusPage as SensusPage
import WebPages.SeptemPage as SeptemPage
import WebPages.Othertees as Othertees
import MySQL.DatabaseManager as Pages
import WebPages

def RetuNewHotShots(selectedPage):

	if selectedPage == Pages.xkom:
		hotShotsCollection = WebPages.XKomPage.XkomPage()
	elif selectedPage == Pages.alto:
		hotShotsCollection = WebPages.AltoPage.AltoPage()
	elif selectedPage == Pages.komputronik:
		hotShotsCollection = WebPages.KomputronikPage.KomputronikPage()
	elif selectedPage == Pages.proline:
		hotShotsCollection = WebPages.ProlinePage.ProlinePage()
	elif selectedPage == Pages.morele:
		hotShotsCollection = WebPages.MorelePage.MorelePage()
	elif selectedPage == Pages.helion:
		hotShotsCollection = WebPages.HelionPage.HelionPage()
	elif selectedPage == Pages.mall:
		hotShotsCollection = WebPages.MallPage.MallPage()
	elif selectedPage == Pages.ibood:
		hotShotsCollection = WebPages.IBoodPage.IBoodPage()
	elif selectedPage == Pages.onepress:
		hotShotsCollection = WebPages.OnePressPage.OnePressPage()
	elif selectedPage == Pages.sensus:
		hotShotsCollection = WebPages.SensusPage.SensusPage()
	elif selectedPage == Pages.septem:
		hotShotsCollection = WebPages.SeptemPage.SeptemPage()
	elif selectedPage == Pages.othertees:
		hotShotsCollection = WebPages.Othertees.OtherteesPage()
	
	if hotShotsCollection != None:
		return hotShotsCollection.GetWebPageData()
