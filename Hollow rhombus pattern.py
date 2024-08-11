a=0
i=0
for x in range(4,0,-1):
    for y in range(1,2):
        y="*"
        a=x*y
        print(a," "*i+x*y)
        i+=2
i=4
for x in range(2,5):
    for y in range(1,2):
        y="*"
        a=x*y
        print(a," "*i+x*y)
        i-=2
