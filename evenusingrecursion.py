def even_number(num):
    if num<2:
        return num%2==0
    return (even_number(num-2))
num=int(input("enter the number : "))
if (even_number(num==True)):
    print(num,"is an even number")
else:
    print(num,"is an odd number")
    
