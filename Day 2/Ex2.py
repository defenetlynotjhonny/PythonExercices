"""""
 In an animal shop, you'll find dogs, cats, rabbits,
and birds. Create a class for each type of animal.

"""

class Animal:
    def __init__(self,quantity,price,available=False):
        self.quantity = quantity
        if self.quantity > 0:
            self.available = True
        self.price = price
        
    def sell(self):
        if self.available == True:
            self.quantity = self.quantity - 1
            
            
class Dogs(Animal):
    def __init__(self):
        pass
    
    def bark(self):
        print("Woof")
        
class Cat(Animal):
    def __init__(self):
        pass
    
    def miau(self):
        print("Miau")
        
class Bird(Animal):
    def __init__(self):
        pass
    
    def birsound(self):
        print("Birsounds")
        
        
class Rabbit(Animal):
    def __init__(self):
        pass
    
    def rabitnoise(self):
        print("Rabbitnoise")