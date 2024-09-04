import time
i=input("Enter the number: ")
a,b,c,d,e="","","","",""
for x in i:
    if x=='1' :
        a+="    *\t"
    elif x=='4' :
        a+="*   *\t"
    else :
        a+="* * *\t"
print(a)
time.sleep(1)
for x in i:
    if x=='1'or x=='2' or x=='3' or x=='7':
        b+="    *\t"
    elif x=='5' or x=='6':
        b+="*    \t"
    else:
        b+="*   *\t"
print(b)
time.sleep(1)
for x in i:
    if x=='1' or x=='7' :
        c+="    *\t"
    elif x=='0':
        c+="*   *\t"
    else:
        c+="* * *\t"
print(c)
time.sleep(1)
for x in i:
    if x=='1' or x=='3' or x=='4' or x=='5' or x=='7' or x=='9':
        d+="    *\t"
    elif x=='2':
        d+="*    \t"
    else:
        d+="*   *\t"
print(d)
time.sleep(1)
for x in i:
    if x=='1' or x=='4' or x=='7':
        e+="    *\t"
    else:
        e+="* * *\t"
print(e)
time.sleep(1)



        
