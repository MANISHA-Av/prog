a=input("enter three words:")
words=a.split(",")
words.sort()
print("words in dictionary order are:")
for i in words:
    print(i,end=" ")
