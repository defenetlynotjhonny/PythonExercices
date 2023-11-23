"""""
At a fruit shop, there are six different types of fruit,
each with a limited stock. When a user buys one or
more fruits, the stock quantity is updated.
Subsequently, the user receives a notification if they
cannot purchase a specific fruit. (Utilize instances of
the "fruit" class)

"""

class Fruit:
    def  __init__(self,stock=10,price=1):
        self.stock = stock
        
    def sell(self,quantity):
        if self.stock - quantity >= 0:
            self.stock = self.stock - quantity
        else:
            print("We don't have that much in stock")
        
    def __str__(self):
        print(f"Stock left: {str(self.stock)}")
        
        
class Kiwi(Fruit):
    
        pass
    
class Banana(Fruit):
    
        pass
    
class Apple(Fruit):
    
        pass

class Pear(Fruit):
    
        pass
    
class Grapes(Fruit):
    
        pass

class PassionFruit(Fruit):
    
        pass

    
instance = Grapes(2)


print(instance.stock)
instance.sell(2)
print(instance.stock)