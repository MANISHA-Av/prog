def sum(n):
    if n<=1:
        return n*n
    else:
        return n*n+sum(n-1)
n=int(input("enter the range: "))
print("the sum is :",sum(n))
