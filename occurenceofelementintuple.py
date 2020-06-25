t=(1,2,3,1,2,4,5,6,2,3,4)
i=0
for e in t:
    if t.index(e)==i:
        print(e,":",t.count(e))
    i+=1
