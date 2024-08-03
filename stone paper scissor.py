import random
a=["stone","paper","scissor"]
i,j,d=0,0,0
n=False
while True:
    b=input("Choose stone or paper or scissor:")
    c=random.choice(a)
    print(c)
    if (c==b):
        d+=1
    elif (c=="stone" and b=="paper") or(c=="paper" and b=="scissor") or (c=="scissor" and b=="stone"):
        i+=1
        d+=1
    else:
        j+=1
        d+=1
    if d==5:
         n==True
         break
if d==5:
    if i==j:
        print("oh match draw")
    elif i>j:
        print(" you won the game, points",i)
    else:
        print(" you lost!try next time, points",i)
            
        
        
