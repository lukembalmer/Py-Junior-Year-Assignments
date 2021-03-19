#Luke Balmer 3/19/21 Per. 3

#Question 1: 
#Loop- D
#Input- A 
#Decision- B
#Process- C

#Question 2a:
#1- I = 32, J = 20
#2- I = 32, J = 20, R = 12
#3- I = 20, J = 12, R = 12
#2b- I = 20, J = 12, R = 8
#3b- I = 12, J = 8, R = 8
#2c- I = 12, J = 8, R = 4
#3c- I = 8, J = 4, R = 4
#2d- I = 8, J = 4, R = 0
#3d- I = 8, J = 4, R = 0
#4- print(j)
#5

#Question 2b:
#When the two inputs are 0 and 32, 32 is assigned to I and 0 is assigned to J.
#Step 2 of the algorithm attempt to divide I and J, thereby trying to divide 32 by 0.
#This causes a divide by zero error, and breaks the algorithm.
#We can modify the algorithm to include in step 1, if J is 0, display "Divide by zero error" and ask user again for different input.

#Question 3:
def multByAdd():
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    total = 0

    for i in range(b):
        total += a
    print(total)

#Question 4: 
def changeToPennies():
    q = int(input("Input the number of quarters: "))
    d = int(input("Input the number of dimes: "))
    n = int(input("Input the number of nickels: "))
    p = int(input("Input the number of pennies: "))
    total = (25 * q) + (10 * d) + (5 * n) + (1 * p)
    print(total, "is the equivalent number of pennies.")

#Question 5:
def estimateSpace():
    charactersPerWord = 5
    wordsPerPage = 300
    pagesPerInch = 300
    inchesPerFoot = 12

    x = 5000000000
    spaceReq = (x * charactersPerWord * wordsPerPage * pagesPerInch) / inchesPerFoot
    print("The total linear space required, in feet, to hold 5 billion characters is:")
    print(spaceReq)
