class item():
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def getitemname(self):
        return self.name

    def setitemname(self, name):
        self.name=name

    def getitemprice(self):
        return self.price

    def setitemprice(self, price):
        self.price=price
    
    def __str__(self):
        return self.name + ' ' + self.price
