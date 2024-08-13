n=int(input("Enter how many numbers you want:"))
a=0
b=1
if (n==1):
      print("0")
if (n==2):
      print("0 ,1")
else:
    print("0 ,1",end=" ")
    for x in range (2,n):
        c=a+b
        a=b
        b=c
        print(",",c,end=" ")
