import agent, unicodedata
from StoreItem import StoreItem
from bs4 import BeautifulSoup

LUDUM_BASE_URL = "https://www.ludum.fr/"

# def customDecode(strin: str):
#     tmp = strin.encode('utf8')
#     return tmp.replace(u'\xa0', ' ')

def customEncode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = LUDUM_BASE_URL + "rechercher?s=" + customEncode(item)
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "product_list"})
    if(checkSomething == None):
        return {}

    liste = list(checkSomething.find_all('li', attrs={"class": "product_item"}))

    itemList = []

    for item in liste:
        price = item.find(attrs={'itemprop' : "price"}).get_text()
        if item.find(attrs={'class' : 'product-price-and-shipping'}).find('img') != None:
            price += " IN SALE"

        a_thumbnail = item.find('a', attrs={"class", "product-thumbnail"})

        itemList.append(StoreItem(
            item.find(attrs={'class' : "product-title"}).find('a').get_text(),
            price,
            a_thumbnail["href"],
            a_thumbnail.find('img')['src'])
        )
    
    return itemList
