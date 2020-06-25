thisdict=dict(input().split(":") for _ in range(2))
print(thisdict)
sums=0
for i in thisdict.values():
    sums+=int(i)
print(sums)
