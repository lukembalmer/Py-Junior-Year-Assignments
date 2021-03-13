#sudoku solver
import time
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def setup():
    global grid
    print("Sudoku Solver By Luke Balmer")
    print("Would you like to input your beginning sudoku values by editing a text file(faster) or within the terminal(slower)?")
    inputChoice = "Error"
    inputChoice = str(input("To enter values by file, enter File. To enter values manually, enter Manual: "))
    if inputChoice == "File" or inputChoice == "File.":
        fname = "sudokugrid.txt"
        infile = open(fname, "r")
        l = infile.readlines() #l is list of lines from sudokugrid.txt
        gridFromFile = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(len(l)):
            for j in range(len(l)):
                gridFromFile[i][j] = l[i][j]
            gridFromFile[i] = list(map(int, gridFromFile[i])) #map sends each iterable from gridFromFile[i] to the int() function, then returns to list to be assigned to a row of gridFromFile
            print(gridFromFile[i])

        if int(input("Enter 1 if the above grid is accurate, enter 0 to restart program: ")) == 1:
            for i in range(len(l)):
                grid[i] = gridFromFile[i]
        else:
            quit()
        
    elif inputChoice == "Manual" or inputChoice == "Manual.":
        cont = True
        complete = False
        while(complete == False):
            print("Input of beginning values will now commence.")
            
            while(cont == True):
                valY = int(input("What row is your value in? ")) - 1
                valX = int(input("What column is your value in? ")) - 1
                value = int(input("What is your value? "))
                grid[valY][valX] = value
                cont = int(input("Value confirmed. Enter 1 to continue entering values or enter 0 to stop: "))
            
            for i in range(9):
                print(grid[i])
            complete = int(input("Enter 1 if the above grid is accurate, enter 0 if it is not: "))
            if complete == True:
                print("Solving...")
            else:
                print("Restarting input process: ")
    else:
        print("Error, restart required. Only enter given phrases.")
        time.sleep(3)
        quit()


    

def possible(y, x, n):
    global grid
    for i in range(0,9): #checks if testing number(n) is in row
        if grid[y][i] == n:
            return False
        
    for i in range(0,9):#checks if n is in column
        if grid[i][x] == n:
            return False

    x0 = (x//3) * 3 #uses floor division to group row into 3 squares
    y0 = (y//3) * 3 #uses floor division to group column into 3 squares

    for i in range(0,3):#checks if n is in native square
        for j in range(0,3):
            if grid[y0+ i][x0 + j] == n:
                return False
    return True
    
def solve():
    global grid
    for y in range(9):
        for x in range(9):#for every space on the grid,
            if grid[y][x] == 0:#if there is not a number, 
                for n in range(1, 10):#test each possible number
                    if possible(y, x, n):
                        grid[y][x] = n #if available, fill that square
                        solve() #recursively check if this leads to a solution
                        grid[y][x] = 0 #if not, backtrack
                return #ends loop if there are no more squares to fill(i.e. the solving alg is finished)
    for i in range(9): #Prints grid as a readable matrix
        print(grid[i])
    input("More? Press enter: ")#user can input enter to see any other possible outcomes

setup()
solve()