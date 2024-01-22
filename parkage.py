from StoreItem import StoreItem
import agent, unicodedata
from bs4 import BeautifulSoup

PARKAGE_JEUX_BASE_URL = "https://www.parkage.com/"

def encode(strin):
    return strin.replace(' ', '+')

def decodeName(item):
    baseName = item.get_text()
    svg = item.find('svg')
    if(svg == None):
        return baseName
    title = svg.find('title')
    return baseName.replace(title.get_text(), ' ')

def search(item):
    url = PARKAGE_JEUX_BASE_URL + "fr/recherche/?text=" + encode(item) 
    html_doc = agent.getClientRenderHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "MuiGrid2-root MuiGrid2-direction-xs-row MuiGrid2-grid-xs-12 MuiGrid2-grid-sm-12 MuiGrid2-grid-md-9 css-1qwdei6"})
    if checkSomething == None:
        return {}
    
    liste = list(checkSomething.find_all('div', attrs={"class": "MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 css-byz040"}))

    items_list = []
    for item in liste:
        items_list.append(StoreItem(
            decodeName(item.find("p", attrs={"class": "MuiTypography-root MuiTypography-body1 css-1gh66tq"})),
            item.find('span', attrs={"class": "MuiTypography-productPrice"}).get_text(),
            PARKAGE_JEUX_BASE_URL + item.find('a', attrs={"class": "MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineNone css-19mvujq"})['href'],
            item.find('img')['src']
        ))
    
    return items_list
