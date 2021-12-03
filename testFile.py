from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import *
def test_custompizzadescription():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    Price: $8.00\n"

    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: L\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ sausage\n\
    Price: $14.00\n"

def test_specialtypizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
    "SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n"

def test_orderdescription():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
    "******\n\
    Order Time: 123000\n\
    CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ sausage\n\
    Price: $9.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $21.00\n\
    ******\n"

