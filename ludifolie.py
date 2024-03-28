from StoreItem import StoreItem
import agent, unicodedata
from bs4 import BeautifulSoup

LUDIFOLIE_JEUX_BASE_URL = "https://www.ludifolie.com/"

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = LUDIFOLIE_JEUX_BASE_URL + "recherche?controller=search&s=" + encode(item) 
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "products row"})
    if checkSomething == None:
        return {}
    
    liste = list(checkSomething.find_all('li', attrs={"class": "product-miniature"}))

    items_list = []
    for item in liste:
        nameWrapper = item.find("h3", attrs={"class": "product-title"})
        items_list.append(StoreItem(
            nameWrapper.get_text(),
            item.find('div', attrs={"class": "product-price-and-shipping"}).find(attrs={"class" : "price"}).get_text(),
            nameWrapper.find('a')['href'],
            item.find('a', attrs={"class": "thumbnail product-thumbnail"}).find('img')['data-full-size-image-url'],
            "Ludifolie"
        ))
    
    return items_list
