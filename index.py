l=[1,5,7,3,2,1,3,6,5,1]
element=int(input("enter the element to find:"))
for i in range(len(l)):
    if l[i]==element:
        print(i,end=" ")
    i+=1 
