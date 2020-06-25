import itertools
def comb(l,r):
    c=itertools.combinations(l,r)
    return(list(c))
l=[1,2,3,4,5]
r=3
x=comb(l,r)
print(x)
