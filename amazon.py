import agent
from bs4 import BeautifulSoup
from StoreItem import StoreItem

AMAZON_BASE_URL = "https://www.amazon.fr/"

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = AMAZON_BASE_URL + "s?k="+ encode(item) + "&i=toys" 
    html_doc = agent.getHtml(url)
    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find_all(attrs={"class" : "puis-card-container"})

    if checkSomething == None:
        return {}

    liste = list(checkSomething[0:20])

    itemList = []

    for item in liste:
        ingclikable = item.find('a', attrs={'class' : "a-link-normal"})
        priceSection = item.find('div', attrs={"data-cy": "price-recipe"})
        price = priceSection.find('span', attrs={"class" : "a-price"})
        if price != None:
            itemList.append(StoreItem(
                item.find('div', attrs={'data-cy' : "title-recipe"}).find('h2').find('a').find('span').get_text(), 
                price.find('span',  attrs={"class": "a-offscreen"}).get_text(),
                AMAZON_BASE_URL + ingclikable['href'],
                item.find('img', attrs={"class": "s-image"})['src'],
                "Amazon")
            )
    
    return itemList
