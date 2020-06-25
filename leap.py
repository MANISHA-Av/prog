num=int(input("enter the year:"))
if (num%4==0 and num%100!=0 or num%400==0):
    print("the year is a leap year")
else:
    print("enter year is not a leap year")
