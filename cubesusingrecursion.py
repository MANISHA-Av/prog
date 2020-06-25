def printcubes(i,n):
    if i<=n:
        print(i**3)
        printcubes(i+1,n)
printcubes(1,10)
