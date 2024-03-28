import json

class  StoreItem:
    def __init__(self, name, price, link = None, img = None, origin = None,):
        self.name = name
        self.price = price
        self.link = link
        self.img = img
        self.origin = origin

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return str(self)
