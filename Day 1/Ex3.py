
"""""
Establish a restaurant menu using functions. In a
separate module, create three functions: the first to
display a list of dishes, the second to select a dish,
and the third to request the bill. In the main
program, input the list of dishes using the keyboard.
Then, call these functions in an endless loop while
soliciting the bill.

"""

from menu import displaydishes , billing , selectdish



done = False




def fillMenu():
    menuitems = []
    done = False
    while done == False:
        item = input("Give me a dish you want to order: ")
        exit = input("Would that be all?")
        menuitems.append(item)
        
        if exit == "Y":
            done = True
            
    return menuitems



menu = fillMenu()
while done == False:
    tab = selectdish(menu)
    print("Would you like to order more?")
    nextround = input()
    if nextround == "N":
        print(f"Thanks for dining with us. \n Your total is {billing(tab)}")
        done = True
    
    
    

