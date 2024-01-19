import philibert, ludum, playin, espritjeu, typer, ultrajeux
from itertools import groupby

WEBSITES = [
    {"name" : "Philibert", "agent": philibert}, 
    {"name" : "Ludum", "agent": ludum}, 
    {"name": "Play In", "agent": playin},
    {"name": "EspritJeu", "agent": espritjeu},
    {"name": "Ultra Jeux", "agent": ultrajeux}
]

def search_everywhere(item):
    values = []
    for site in WEBSITES:
        print(site["name"])
        current = site["agent"].search(item)
        print(current)
        values.append({"site" : site['name'], "value" : current})
        print("")
    return values

def generateTab(item: str):
    tab = []
    for site in WEBSITES:
        current = site["agent"].search(item)
        for game in current:
            tab.append({"site": site["name"], "name": game, "price": current[game]})
    return tab

app = typer.Typer()

@app.command()
def search(item: str, store: str = None):
    if store:
        print(list(filter(lambda site : site['name'] == store, WEBSITES))[0]['agent'].search(item))
    else:
        search_everywhere(item)

@app.command()
def compare(item: str):
    tab = generateTab(item)
    def key_func(t):
        return t['name']

    tab = sorted(tab, key=key_func)
    for key, value in groupby(tab, key_func):
        print('\033[1m  \n'+ key + '\033[0m')
        print('\n'.join(map(str, list(value))))

@app.command()
def hello():
    print(f"Hello leo")
    
if __name__ == "__main__":
    app()