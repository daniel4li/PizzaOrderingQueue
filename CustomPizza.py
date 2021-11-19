from Pizza import Pizza

class CustomPizza(Pizza):
   
    def __init__ (self,size):
        self.size = size
        if size == "S": 
            self.price = 8.00
        elif size == "M":
            self.price = 10.00
        else:
            self.price = 12.00
    topping = []
    def addTopping(self, topping):
        self.topping.append(topping)
        if self.size == "S": 
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        else:
            self.price += 1.00

    def getPizzaDetails(self):
        return "CUSTOM PIZZA" + "\n" + "Size: " + str(self.size) + "\n" + "Toppings: " + "\n" + 

    