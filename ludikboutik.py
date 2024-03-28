from StoreItem import StoreItem
import agent, unicodedata
from bs4 import BeautifulSoup

LUDIKBOUTIK_JEUX_BASE_URL = "https://www.ludikboutik.fr/"

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = LUDIKBOUTIK_JEUX_BASE_URL + "search.php?search=" + encode(item) 
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "content-products mode-boutique"})
    if checkSomething == None:
        return {}
    
    liste = list(checkSomething.find_all('div', attrs={"class": "produits"}))

    items_list = []
    for item in liste:
        img_container = item.find('div', attrs={"class": "productImageWrap"})
        items_list.append(StoreItem(
            item.find("a", attrs={"class": "nomprod_link"}).get_text(),
            item.find('span', attrs={"class": "impact_price"}).get_text(),
            LUDIKBOUTIK_JEUX_BASE_URL + img_container.find('a')['href'],
            LUDIKBOUTIK_JEUX_BASE_URL + img_container.find('img')['src'],
            "LudikBoutik"
        ))
    
    return items_list
