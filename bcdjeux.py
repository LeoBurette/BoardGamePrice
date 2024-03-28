import agent
from bs4 import BeautifulSoup
from StoreItem import StoreItem

BCDJEUX_BASE_URL = "https://www.bcd-jeux.fr/"

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = BCDJEUX_BASE_URL + "recherche?search_query=" + encode(item)
    html_doc = agent.getHtml(url)
    soup = BeautifulSoup(html_doc, 'html.parser')

    allTags = soup.find_all(attrs={"class" : "products"})
    checkSomething = None
    for tag in allTags:
        if 'owl-carousel' not in tag.attrs['class']:
            checkSomething = tag

    if checkSomething == None:
        return {}

    liste = list(checkSomething.find_all('article', attrs={"class": "product-miniature"}))

    itemList = []

    for item in liste:
        ingclikable = item.find('a', attrs={'class' : "thumbnail"})
        
        itemList.append(StoreItem(
            item.find('h2', attrs={'class' : "product-title"}).find('a').get_text(), 
            item.find('span', attrs={"class" : "price"}).get_text(),
            ingclikable['href'],
            ingclikable.find('img')['data-src'],
            "BCDJeux")
        )
    
    return itemList
