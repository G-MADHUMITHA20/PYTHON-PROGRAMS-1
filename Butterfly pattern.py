n=5
for i in range(n):
    print("*" * (i+1),end="")
    print(" " *(2*(n-i-1))+"*"*(i+1))
for i in range(n-2,-1,-1):
    print("*"*(i+1),end="")
    print(" "*(2*(n-i-1))+"*"*(i+1))
        
