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
        for i in self.pizzas:
            c = i.getPizzaDetails() + "\n" + "----" + "\n"
            b += c
            d = 0 + i.self.price 
        e = "TOTAL ORDER PRICE: " + d + "\n" + "******" + "\n"
        return a + b + e

cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)

print (order.getOrderDescription())


        
