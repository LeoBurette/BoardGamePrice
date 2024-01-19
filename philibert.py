import agent
from bs4 import BeautifulSoup

PHILIBERT_BASE_URL = "https://www.philibertnet.com/fr/"

def encode(strin):
    return strin.replace(' ', '+')

def decode(strin):
    return strin.replace(u'\xa0', ' ')

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

    liste = list(soup.find(attrs={"class" : "product_list"}).find_all('li', attrs={"class": "ajax_block_product"}))

    items_name = list(map(lambda a : decode(a.find(attrs={'class' : "s_title_block"}).find('a')["title"]), liste))
    items_price = list(map(lambda a : a.find(attrs={'class' : "price"}).get_text(), liste))

    return {items_name[i]: items_price[i] for i in range(len(items_name))}