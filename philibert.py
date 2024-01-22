from StoreItem import StoreItem
import agent
from bs4 import BeautifulSoup

PHILIBERT_BASE_URL = "https://www.philibertnet.com/fr/"

def encode(strin):
    return strin.replace(' ', '+')

# def decode(strin):
#     return strin.replace(u'\xa0', ' ')

def getBestSellers():
    html_doc = agent.getHtml(PHILIBERT_BASE_URL)

    soup = BeautifulSoup(html_doc, 'html.parser')

    bestsellers = soup.find(attrs={'id':'blockbestsellers'})
    bestsellers_items = bestsellers.find_all(attrs={"class" : "s_title_block"})

    name = list(map(lambda a: a.find('a')['title'], bestsellers_items))

    return name

def search(item):
    url = PHILIBERT_BASE_URL + "recherche?search_query="+ encode(item) +"&submit_search="
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "product_list"})
    if(checkSomething == None):
        return {}
    
    itemList = []

    liste = list(checkSomething.find_all('li', attrs={"class": "ajax_block_product"}))

    for item in liste:
        product_img_link = item.find('a', attrs={"class", "product_img_link"})

        itemList.append(StoreItem(
            item.find(attrs={'class' : "s_title_block"}).find('a')["title"],
            item.find(attrs={'class' : "price"}).get_text(),
            product_img_link['href'],
            product_img_link.find('img')['src'])
        )

    return itemList