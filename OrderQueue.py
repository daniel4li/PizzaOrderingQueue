from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class QueueEmptyException(Exception):
    def __init__(self, says = "No orders to remove"):
        self.says = says
    
class OrderQueue:
    def __init__ (self): 
        self.heaplist = [PizzaOrder(0)]
        self.current = 0
    
    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i].getTime() < self.heaplist[i // 2].getTime():
                temp = self.heaplist[i // 2].getTime()
                self.heaplist[i // 2].setTime(self.heaplist[i].getTime())
                self.heaplist[i].setTime(temp)
            i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.current:
            m = self.minChild(i)
            if self.heaplist[i].getTime() > self.heaplist[m].getTime():
                temp = self.heaplist[i].getTime()
                self.heaplist[i].setTime(self.heaplist[m].getTime())
                self.heaplist[m].setTime(temp)
            i = m

    def minChild(self,i):
        if i * 2 + 1 > self.current:
            return i * 2
        else:
            if self.heaplist[i*2].getTime() < self.heaplist[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def addOrder(self,a):
        self.heaplist.append(a)
        self.current = self.current + 1
        self.percUp(self.current)
    
    def processNextOrder(self):
        if len(self.heaplist) < 2:
            raise QueueEmptyException
        val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.current]
        self.current = self.current - 1
        self.heaplist.pop()
        self.percDown(1)
        return val.getOrderDescription()

print("Testing pizza order")
bh = OrderQueue()
cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)
cp1 = CustomPizza("M")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("M", "Carne-more")
order2 = PizzaOrder(113000) #12:30:00PM
order2.addPizza(cp1)
order2.addPizza(sp1)
bh.addOrder(order)
bh.addOrder(order2)
print(bh.processNextOrder())
print(bh.processNextOrder())
