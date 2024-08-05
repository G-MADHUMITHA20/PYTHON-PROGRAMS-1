Data=input("enter:")
letter=input("enter a word or letter to count:")
count=0
if(len(letter)>1):
    a=Data.split(" ")
    for x in a:
        if(letter==x):
            count+=1
else:
    for x in data:
        if(letter==x):
            count+=1
print("count of the given data=",count)
