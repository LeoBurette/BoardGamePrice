from StoreItem import StoreItem
import agent
from bs4 import BeautifulSoup
import re, json

PLAYIN_BASE_URL = "https://www.play-in.com/"

# def decode(strin):
#     return strin.replace(u'\xa0', ' ')

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

    items_list = []

    for item in liste:
        container_img = item.find('div', attrs={"class" : "container_img_product"})
        items_list.append(StoreItem(
            item.find(attrs={'class' : "name_product"}).get_text(),
            item.find(attrs={'class' : "price_product"}).get_text(),
            PLAYIN_BASE_URL + container_img.find('a')['href'],
            PLAYIN_BASE_URL + container_img.find('img')['src']
        ))
    
    return items_list
