def printeven(i,n):
    if i<=n:
        print(2*i)
        printeven(i+1,n)
printeven(1,10)
