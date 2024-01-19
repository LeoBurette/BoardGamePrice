import agent
from bs4 import BeautifulSoup

ESPRITJEU_BASE_URL = "https://www.espritjeu.com/"

def decode(strin):
    return strin.replace('\n', '')

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = ESPRITJEU_BASE_URL + "dhtml/resultat_recherche.php?keywords=" + encode(item)
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    liste = list(soup.find(attrs={"class" : "jq-products-list"}).find_all('div', attrs={"class": "product_box"}))

    items_name = []
    items_price = []

    for item in liste:
        items_name.append(decode(item.find(attrs={'class' : "bp_designation"}).find('a').get_text()))
        price = item.find(attrs={'class' : "bp_prix"}).find_all('div')[0].get_text()
        items_price.append(decode(price))
    
    return {items_name[i]: items_price[i] for i in range(len(items_name))}
