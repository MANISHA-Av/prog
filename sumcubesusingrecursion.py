def sum(n):
    if n<=1:
        return n**3
    else:
        return n**3+sum(n-1)
n=int(input("enter the range: "))
print("the sum is :",sum(n))
