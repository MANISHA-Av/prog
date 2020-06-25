def nextPrime(n):
    for i in n:
        i+=1
        for j in range(2,i//2):
            if i%j==0:
                break
        else:
            return n

n=set(input("enter  the elements : "))
nextPrime(list(n))
