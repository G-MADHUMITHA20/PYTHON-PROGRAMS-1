#METHOD 1:
i=5
for x in range(1,i+1):
    for y in range(1,2):
        if x>1:
            y="*"+" "
        else:
            y="*"
        i-=1
        print(" "*i,x*y," "*i)
#METHOD 2:
i=5
for x in range(i):
    print(" "*(i-x-1)+"* "*(x+1))
