a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
p=0
for x in range(a,1,-1):
    if a%x==0 and b%x==0:
        print("GCD is",x)
        p=1
        break
if p==0:
    x=1
    print(1)
print("LCM is",int((a*b)/x))
