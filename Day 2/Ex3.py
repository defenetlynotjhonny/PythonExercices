"""""
- What's for dinner today? In the fridge, there are two
types of meat-based foods: hotdogs and steaks. What
do they have in common? Create the Meat class and
its 2 child classes. Let's not forget about vegetables!
You have carrots, tomatoes, and peppers. Once again,
create the parent class Vegetable and its 3 child
classes. Enjoy your meal!


"""

class Meat:
    def  __init__(self,amount,cookingtime):
       self.amount = amount
       self.cookingtime = cookingtime
       
    def cook(self):
        while self.cookingtime > 0:
            self.cookingtime = self.cookingtime - 1
       
       
class Steak(Meat):
    def __init__(self,cutgrade):
        self.cutgrade = cutgrade
        
        
class HotDog(Meat):
    def __init__(self):
        pass
    
    
class Veggies:
    def  __init__(self,amount,cookingtime):
            self.amount = amount
            self.cookingtime = cookingtime
       
    def cook(self):
        while self.cookingtime > 0:
            self.cookingtime = self.cookingtime - 1
            
class Carrots(Veggies):
    def  __init__(self):
        pass
    
class Tomatoes(Veggies):
    def  __init__(self):
        pass
    
class Peppers(Veggies):
    def  __init__(self):
        pass
    
    