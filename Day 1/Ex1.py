"""""
Develop a straightforward calculator with functions.
Present a menu on the screen featuring the four
primary operations. Subsequently, users can input
their choice and two numerical values. After
displaying the result, users can view the menu
again and repeat the process until they type end.'
"""

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def askforexit():
    result = 0
    print("Would you like to exit? (Y/N)")
    userinput = input(":")
    if userinput == "Y":
        return True
    elif userinput == "N":
        return False
    return result


def runCalc():
    done = False
    exit = False
    result = "Not possible try again."
    print("Hi I am a calculator.\n")
    counter = 0
    
   
    
    
    if exit == True:
        return result
        
    if counter < 1:
        print("Please enter an operation you would like to perform.")
            
    else:
        print("Invalid operator Try again:\n")
            
    print("PLease choose a valid operation you want to perform:\n \t-Addition(1)\n \t-Subtraction(2)\n \t-Multiplication(3)\n \t-Division(4)")
    operation = int(input("\n -:_" ))
    leftside = float(input("\n Enter the first number: "))
    rightside = float(input("\n Enter the second number:"))
    counter = 0
        
        
        
    if operation == 1:
        print(f"{leftside}  +   {rightside} = {add(leftside,rightside)}")
        exit = askforexit()
            
        done = True
    elif operation == 2:
        print(f"{leftside}  -   {rightside} = {subtract(leftside,rightside)}")
        exit = askforexit()
            
        done = True
    elif operation == 3:
        print(f"{leftside}  *   {rightside} = {multiply(leftside,rightside)}")
        exit = askforexit()
            
        done = True
    elif operation == 4:
        print(f"{leftside}  /   {rightside} = {divide(leftside,rightside)}")
        exit = askforexit()
            
        done = True
    else:
        counter = counter + 1
            
        exit = askforexit()
    if exit == True:
        return "Exit succesful."
    else:
        runCalc() 
        

runCalc()