import agent, unicodedata
from bs4 import BeautifulSoup

ULTRA_JEUX_BASE_URL = "https://www.ultrajeux.com/"

def decode(strin: str):
    return strin.strip().split(' ', 1)[1]

def encode(strin):
    return strin.replace(' ', '+')

def search(item):
    url = ULTRA_JEUX_BASE_URL + "search3.php?text=" + encode(item) + "&submit=Ok"
    html_doc = agent.getHtml(url)

    soup = BeautifulSoup(html_doc, 'html.parser')

    checkSomething = soup.find(attrs={"class" : "search"})
    if checkSomething == None:
        return {}
    
    liste = list(checkSomething.find_all('div', attrs={"class": "contenu_block_produit_all"}))

    items_name = []
    items_price = []

    for item in liste:
        items_name.append(decode(item.find("p", {"class": "titre"}).find('a')['title']))
        price = item.find('span', {"class": "prix"}).get_text()
        items_price.append(price)
    
    return {items_name[i]: items_price[i] for i in range(len(items_name))}
