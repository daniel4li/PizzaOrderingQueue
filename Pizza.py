class Pizza:
    sizes = {
        "S" == "Small"
        "M" == "Medium"
        "L" == "Large"

    }
    def __init__ (self, size = "", price = 0.0):
        self.price = price
        self.size = size
    
    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        self.price = price
    
    def getSize(self):
        return str(self.size)
    
    def setSize(self, size):
        self.size = size
