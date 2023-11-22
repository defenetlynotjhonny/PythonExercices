"""""
Implement a login process where users enter the
    correct username and password initially. Following
    this, they can choose to log out or modify the
    password with a new one as many times as
    desired. Password modification is only allowed
    when logged in. Upon logging out, users can
    choose to log in again, considering whether the
    password has been modified.
"""

def initialprompt():
    username = input("Username: ")
    password = input("Password:")
    return [username, password]



def login():
    data = initialprompt()
    usern = data[0]
    pw = data[1]
    done = True
    loggedin = False
    userchoice = -1
    while done != False:
        if loggedin == False or userchoice == 0:
            print("Enter the username to log in:")
            inputusern = input()
            print("Enter the password")
            inputpw = input()
            loggedin = True
        
        
        if usern != inputusern or pw != inputpw:
            print("Wrong Password or Username, please try again")
            userchoice = 0
            
        if usern == inputusern and pw == inputpw:
            loggendin = True
            print("Login successful. How would you like to proceed: \n")
            print("Change Password-(1)\n")
            print("Logout -(2)\n")
            print("Exit - (3)")
            userchoice = int(input("New Password: "))
            
        if userchoice == 3:
            print("Exiting...")
            return "Exited"
        
        elif userchoice == 2:
            loggedin = False
            
        elif userchoice == 1 and loggedin == True:
            print("What should the new password be?")
            pw = input()
        
        
        
    
    return True

login()