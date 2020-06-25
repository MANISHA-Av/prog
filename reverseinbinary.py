def reverse(num):
    result=0
    while num:
        result=(result << 1)+(num & 1)
        num>>=1
    print(result)
num=int(input("enter number : "))
reverse(num)
