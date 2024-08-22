n=int(input("Enter:"))
for i in range(n):
    print(" " *(1*(n-i-1))+"*"*(i+1))

    
              #METHOD-2
n=int(input("Enter:"))
for x in range(1,n+1):
    y="*"
    print(" "*n,x*y)
    n-=1
