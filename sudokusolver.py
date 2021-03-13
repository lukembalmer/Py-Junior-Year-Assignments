#sudoku solver

grid = [[0, 7, 0, 0, 0, 0, 0, 0, 9], 
[5, 1, 0, 4, 2, 0, 6, 0, 0], 
[0, 8, 0, 3, 0, 0, 7, 0, 0], 
[0, 0, 8, 0, 0, 1, 3, 7, 0], 
[0, 2, 3, 0, 8, 0, 0, 4, 0], 
[4, 0, 0, 9, 0, 0, 1, 0, 0], 
[9, 6, 2, 8, 0, 0, 0, 3, 0], 
[0, 0, 0, 0, 1, 0, 4, 0, 0], 
[7, 0, 0, 2, 0, 3, 0, 9, 6]]

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

    for i in range(0,3):#checks if n is in square
        for j in range(0,3):
            if grid[y0+ i][x0 + j] == n:
                return False
    return True
    
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for i in range(9):
        print(grid[i])
    input("More?")
solve()