                    #METHOD-1
n=int(input("Enter:"))
for i in range(n-1,-1,-1):
     print(" " *(1*(n-i-1))+"*"*(i+1))


                    #METHOD-2
n=int(input("Enter:"))
for x in range(n,0,-1):
    y="*"
    print(" "*n,x*y)
    n+=1

