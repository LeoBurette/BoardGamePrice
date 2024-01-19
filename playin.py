import unicodedata
import agent
from bs4 import BeautifulSoup
import re, json

PLAYIN_BASE_URL = "https://www.play-in.com/"

def decode(strin):
    return strin.replace(u'\xa0', ' ')

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    # JS populated html
    url = PLAYIN_BASE_URL + "recherche/result.php?s="+encode(item)
    html_doc = agent.getClientRenderHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    boardgames = soup.find('div', attrs={"class": "container_showhide container_family filterCategory filterFamily", "data-family" : 5})
    if(boardgames == None):
        return {}
    
    boardGamePart = boardgames.find("div", attrs={"class" : "bloc"})

    liste = list(boardGamePart.find_all('div', attrs={"class": "list_product_full"}))

    items_name = []
    items_price = []

    for item in liste:
        items_name.append(decode(item.find(attrs={'class' : "name_product"}).get_text()))
        price = item.find(attrs={'class' : "price_product"}).get_text()
        items_price.append(decode(price))
    
    return {items_name[i]: items_price[i] for i in range(len(items_name))}
