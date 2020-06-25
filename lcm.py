a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a>b:
    max=a
else:
    max=b
while True:
    if (max%a==0 and max%b==0):
        print("LCM is",max)
        break
    max+=1
