def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
n=int(input("enter the range: "))
print("the sum is :",sum(n))
