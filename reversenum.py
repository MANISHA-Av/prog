def naturalnumber(i,n):
    if i>=n:
        print(i)
        i-=n
        return naturalnumber(i,n)
    else:
        return 1
i=int(input())
n=int(input())

naturalnumber(i,n)
