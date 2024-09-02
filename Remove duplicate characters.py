a=input("Enter the string:")
b=""
for x in a:
    if x not in b:
        b=b+x
print(b)
