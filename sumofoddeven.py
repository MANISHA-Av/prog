l=list(map(int,input("enter the number: ").split(",")))
even=0
odd=0
for i in l:
    if i%2==0:
        even+=i
    else:
        odd+=i
    i+=1
print("sum of even number in the list: ",even)
print("sum of odd number in the list: ",odd)
