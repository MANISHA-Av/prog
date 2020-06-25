def arms(n):
    sum=0
    temp=n
    while n!=0:
        m=n%10
        sum=sum+m**3
        n=n//10
    if sum==temp:
        print("num is an armstrong number")
    else:
        print("num is not armstrong")
arms(153)
def odd_even(num):
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
odd_even(45)
def leap_year(year):
    if (year%4==0):
        if (year%100==0):
            if(year%400==0):
                print("leap year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")
leap_year(2016)