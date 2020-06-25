string="aabbccdd"
unique=""
for x in string:
    if not(x in unique):
        unique+=x
print(unique)
