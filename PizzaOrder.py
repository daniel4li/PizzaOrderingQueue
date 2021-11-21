from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time): 
        self.time = time 
        self.pizzas = []

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
    
    def addPizza(self, pizza): 
        self.pizzas.append(pizza)
    
    def getOrderDescription(self):  
        a = "******" + "\n" + "Order Time: " + str(self.time) 
        b = "\n"
        counter = 0
        for i in self.pizzas:
            c = i.getPizzaDetails() + "\n" + "----" + "\n"
            b += c
            counter = counter + i.getPrice()
        
        e = "TOTAL ORDER PRICE: $" +  str("{0:.2f}".format(counter, 2)) + "\n" + "******" + "\n"
        return a + b + e




        
