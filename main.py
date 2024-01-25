import philibert, ludum, playin, espritjeu, typer, ultrajeux, ludikboutik, parkage, ludifolie
from itertools import groupby, combinations
from StoreItem import StoreItem
from collections import Counter

WEBSITES = [
    {"name" : "Philibert", "agent": philibert}, 
    {"name" : "Ludum", "agent": ludum},
    {"name": "PlayIn", "agent": playin},
    {"name": "Parkage", "agent": parkage},
    {"name": "EspritJeu", "agent": espritjeu},
    {"name": "UltraJeux", "agent": ultrajeux},
    {"name": "LudiFolie", "agent": ludifolie},
    {"name": "LudikBoutik", "agent": ludikboutik}
]

def search_print_everywhere(item):
    for site in WEBSITES:
        print(site["name"])
        current = site["agent"].search(item)
        print(current)
        print("")

def getRatio(a,b):
    stripJunk = str.maketrans("","","- ")
    a = a.lower().translate(stripJunk)
    b = b.lower().translate(stripJunk)
    total  = len(a)+len(b)
    counts = (Counter(a)-Counter(b))+(Counter(b)-Counter(a))
    return 100 - 100 * sum(counts.values()) / total

def generateTab(item: str):
    def addOrigin(item: StoreItem, site):
        item.origin = site
        return item
    
    tab = []
    i = 0
    for site in WEBSITES:
        i = i + 1
        print(str(i) + '/' + str(len(WEBSITES)))
        current = site["agent"].search(item)
        current = list(map(lambda a : addOrigin(a, site['name']), current))
        tab = tab + current
    return tab

def groupeur(tab):
    treshold = 90
    minGroupSize = 1

    paired = { c:{c} for c in tab}
    for a,b in combinations(tab,2):
        if getRatio(a.name, b.name) < treshold: continue
        paired[a].add(b)
        paired[b].add(a)
    
    groups    = list()
    ungrouped = set(tab)
    while ungrouped:
        bestGroup = {}
        for item in ungrouped:
            g = paired[item] & ungrouped
            for c in g.copy():
                g &= paired[c] 
            if len(g) > len(bestGroup):
                bestGroup = g
        if len(bestGroup) < minGroupSize : break  
        ungrouped -= bestGroup
        groups.append(list(bestGroup))
    return groups

app = typer.Typer()

@app.command()
def search(item: str, store: str = None):
    if store:
        print(list(filter(lambda site : site['name'] == store, WEBSITES))[0]['agent'].search(item))
    else:
        search_print_everywhere(item)

@app.command()
def compare(item: str):
    tab = generateTab(item)
    tab = groupeur(tab)
    for group in tab:
        print('\033[1m  \n'+ group[0].name + '\033[0m')
        print('\n'.join(map(str,group)))

@app.command()
def hello():
    print(f"Hello leo")
    
if __name__ == "__main__":
    app()