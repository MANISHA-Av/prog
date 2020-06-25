def printeven(i,n):
    if n<=i:
        print(2*i)
        printeven(i-1,n)
printeven(10,1)
