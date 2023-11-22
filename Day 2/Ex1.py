"""""
Develop a program for library management. Ensure
to create a "book" class encompassing all the
fundamental properties and methods.

"""

def add(a,*b):
    result = a
    
    for i in range(len(b)):
        result = result + b[i] 
        
    return result

def multiply(a,*b):
    result = a
    for i in range(len(b)):
        result = result * b[i] 
        
    return result

def divide(a,*b):
    result = a
    for i in range(len(b)):
        result = result // b[i]
        
    return result


def UserChoice(operationcounter):
    choice = 0
    if operationcounter == 0:
        print("+++++++++++++++++ \t Hi I am a calculator. \t +++++++++++++++++")
    print("You can perform: -Addition(1)\n -Subtraction\n -")
    print("Pleas")
    
    
    return choice