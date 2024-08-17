n=int(input("Enter number:"))
i=n
r=0
while i>0:
    d=i%10
    r=r*10+d
    i=i//10
if r==n:
    print("PALINDROME.")
else:
    print("NOT A PALINDROME.")
