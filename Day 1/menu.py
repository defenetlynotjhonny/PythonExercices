from random import randrange

def displaydishes(*dishes):
    for i in range(len(dishes[0])):
        print(f"{i}. {dishes[0][i]}")
    
    return dishes

def selectdish(dishes):
    selected = []
    print("Choose a dish:")
    displaydishes(dishes)  
    done = False
    while done == False:
        userchoice = int(input("What can I bring you:"))
        if userchoice >= 0 and userchoice < len(dishes):
            selected.append(dishes[userchoice])
            repeat = input("Would you like something additionally? (Y/N)")
            
        if repeat == "N":
            done = True
            
    print("You have selected:")
    displaydishes(dishes)        
    return selected
        
def billing(dishes):
    #assuming every dish costs 20 units of currency
    total = len(dishes) * 20
    return total 
        

