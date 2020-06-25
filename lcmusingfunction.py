def lcm(a,b):
    if a>b:
        max=a
    else:
        max=b
    while True:
        if max%a==0 and max%b==0:
            return max
        max+=1
a=int(input("enter first number: "))
b=int(input("enter second number: "))
x=lcm(a,b)
print("LCM of two numbers are : "x)
