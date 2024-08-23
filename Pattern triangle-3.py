#1)
n=int(input("Enter:"))
for i in range(n):
    print(" " *(2*(n-i-1))+"*"*(i+1))


#2)   
n=int(input("Enter:"))
for i in range(n-2,-1,-1):
     print(" " *(2*(n-i-1))+"*"*(i+1))
