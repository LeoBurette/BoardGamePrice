from StoreItem import StoreItem
import agent, unicodedata
from bs4 import BeautifulSoup

ULTRA_JEUX_BASE_URL = "https://www.ultrajeux.com/"

def decode(strin: str):
    return strin.strip().split(' ', 1)[1]

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = ULTRA_JEUX_BASE_URL + "search3.php?text=" + encode(item) + "&submit=Ok"
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "search"})
    if checkSomething == None:
        return {}
    
    liste = list(checkSomething.find_all('div', attrs={"class": "contenu_block_produit_all"}))

    items_list = []
    for item in liste:
        img_container = item.find('p', attrs={"class": "image"})
        items_list.append(StoreItem(
            decode(item.find("p", attrs={"class": "titre"}).find('a')['title']),
            item.find('span', attrs={"class": "prix"}).get_text(),
            ULTRA_JEUX_BASE_URL + img_container.find('a')['href'],
            img_container.find('img', attrs={"class", "produit_scan"})['src'],
            "UltraJeux"
        ))
    
    return items_list
