def printsquares(i,n):
    if i<=n:
        print(i*i)
        printsquares(i+1,n)
printsquares(1,10)
