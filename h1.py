n,k=map(int,input().split())
maxi=0
count=0
ch=[]
for i in range(n):
    strings=input()
    if strings[i]==strings[i+1]:
        count+=1
        ch.append(string[i])
    else:
        maxi=max(count,maxi)
        count=1
maxi=max(count,maxi)
print(maxi+k)
