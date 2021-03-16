#fibonacci problems

def fib(x):
    #assuming x is an int >= 0
    #return fibonacci of x
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

fibonacci = fib(11)
print(fibonacci)