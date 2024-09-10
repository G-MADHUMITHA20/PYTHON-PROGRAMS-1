length=int(input("Enter length:"))
a=[]
for i in range(length):
    b=int(input(f"Enter {i+1} number:"))
    a.append(b)
print("BEFORE SORTING:")
print(a)
tem=0
for j in range(0,len(a)):
    for k in range(0,len(a)):
        if a[j]<a[k]:
            tem=a[j]
            a[j]=a[k]
            a[k]=tem
print(f"AFTER SORTING:\n{a}")

