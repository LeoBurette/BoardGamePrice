import agent, unicodedata
from bs4 import BeautifulSoup

LUDUM_BASE_URL = "https://www.ludum.fr/"

def decode(strin):
    return strin.replace(u'\xa0', ' ')

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = LUDUM_BASE_URL + "rechercher?s=" + encode(item)
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "product_list"})
    if(checkSomething == None):
        return {}

    liste = list(checkSomething.find_all('li', attrs={"class": "product_item"}))

    items_name = []
    items_price = []

    for item in liste:
        items_name.append(decode(item.find(attrs={'class' : "product-title"}).find('a').get_text()))
        price = item.find(attrs={'itemprop' : "price"}).get_text()
        if item.find(attrs={'class' : 'product-price-and-shipping'}).find('img') != None:
            price += " IN SALE"
        items_price.append(decode(price))
    
    return {items_name[i]: items_price[i] for i in range(len(items_name))}
