def hollowpyramid(rows):
    for i in range(rows):
        print(" "*i,end="")
        for j in range(2*(rows-i)-1):
            if i==0 or j==0 or j==2*(rows-i)-2:
                print("*",end="")
            else:
                print(" ",end="")
        print()

rows=10
hollowpyramid(rows)
