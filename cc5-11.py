def main():
    #Program: Print the ordinal ending for each number in a list.
    #Note: Original program didn't include counting for 11, 12, and 13, but I added it in. 
    tempFlag = 0
    elevenWatch = 0
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
    for i in numList:
        if (i % 10) == 0:
            tempFlag = i
        if (i % 100) == 0:
            elevenWatch = i

        if i == elevenWatch + 11 or i == elevenWatch + 12 or i == elevenWatch + 13:
            print(i, "th")
        else:
            if i == 1 or i - tempFlag == 1:
                print(i,"st")
            elif i == 2 or i - tempFlag == 2:
                print(i, "nd")
            elif i == 3 or i - tempFlag == 3:
                print(i, "rd")
            else:
                print(i, "th")
        
        
main()