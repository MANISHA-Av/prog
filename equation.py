print("Quadratic equation: ax^2+bx+c")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("the roots are imaginary")
else:
    root1=(-b+d1)/2*a
    root2=(-b-d1)/2*a
    print("the first root :",round(root1,2))
    print("the second root :",round(root2,2))
