def printodd(i,n):
    if i<=n:
        print(i)
        printodd(i+2,n)
printodd(1,10)
