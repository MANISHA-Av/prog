month=int(input("enter the number of month"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("number of days in month is 31")
elif month==4 or month==6 or month==9 or month==11:
    print("number of days in month is 30")
else:
    print("number of days in month is 28")
