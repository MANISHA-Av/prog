def printevensum(i,n):
    if i>n:
        return 0
    return (i+printevensum(i+2,n))
i=int(input("enter the starting range : "))
n=int(input("enter the ending range : "))
print("sum is : ",printevensum(i,n))
