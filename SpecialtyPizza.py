from Pizza import Pizza

class SpecialtyPizza(Pizza):
    
    def __init__(self,size,name):
        self.size = size
        self.name = name
        if self.size == "S":
            self.price = 12.00
        elif self.size == "M":
            self.price = 14.00
        else:
            self.price = 16.00 

    def getPizzaDetails(self):
        a = "SPECIALTY PIZZA" + "\n" + "Size: " + str(self.size) + "\n"
        b = "Name: " + str(self.name) + "\n"
        c = "Price: $" + str("{0:.2f}".format(self.price, 2)) + "\n"
        return a + b + c

sp1 = SpecialtyPizza("S", "Carne-more")
print (sp1.getPizzaDetails())