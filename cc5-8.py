def main():
    #Program: Make a list of five or more usernames. Imagine you are writing code that will print a greeting to each user.
    usernameList = ["Anne", "Chris", "Kelly", "Jake", "Rainn"]
    userEntry = input("Please enter your username: ")
    hasPrinted = False
    
    if usernameList: #list name in an if statement will be True if list has at least one element
        if userEntry == "admin":
            print("Welcome Admin, would you like to see a status report?")
            hasPrinted = True
    
        for i in usernameList:
            if userEntry == i:
                print("Welcome user " + i)
                hasPrinted = True
                
        if hasPrinted == False:
            print("Error, entered username could not be found in our database. Please retry.") 
    else:
        print("We need to find some users, the list is empty!")
    
main() 