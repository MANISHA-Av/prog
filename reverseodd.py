def printodd(i,n):
    if n<=i:
        print(i-1)
        printodd(i-2,n)
printodd(10,1)
