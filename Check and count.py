n=input("ENTER:")
count=0
a=0
b=0
c=0
d=0
e=0
for x in n:
    if x in ("aeiou"):
        count+=1
    elif x.isspace():
        a+=1
    elif x.isdigit():
        b+=1
    elif x.isalnum()!=True:
        c+=1
    elif x.isupper():
        e+=1
    else:
        d+=1
print("Vowels\t\t=",count)
print("Space\t\t=",a)
print("Digits\t\t=",b)
print("Symbol\t\t=",c)
print("Upper case\t=",e)
