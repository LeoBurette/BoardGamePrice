import agent
from bs4 import BeautifulSoup
from StoreItem import StoreItem

ESPRITJEU_BASE_URL = "https://www.espritjeu.com/"

# def decode(strin):
#     return strin.replace('\n', '')

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = ESPRITJEU_BASE_URL + "dhtml/resultat_recherche.php?keywords=" + encode(item)
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "jq-products-list"})
    if checkSomething == None:
        return {}

    liste = list(checkSomething.find_all('div', attrs={"class": "product_box"}))

    itemList = []

    for item in liste:
        price = item.find(attrs={'class' : "bp_prix"}).find_all('div')[0].get_text()
        
        itemList.append(StoreItem(
            item.find(attrs={'class' : "bp_designation"}).find('a').get_text(), 
            price,
            item.find('a')['href'],
            item.find('img')['data-lazy'],
            "EspritJeu")
        )
    
    return itemList
