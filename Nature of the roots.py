                   #Nature of the roots of equation.
print("General equation:Ax^2+bx+c")
a=int(input("Enter a(a should not be 0):"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=(b**2)-(4*a*c)
print("d=",d)
if d>0:
    print("\tDistinct real roots")
elif d==0:
    print("\tEqual roots")
elif d<0:
    print("\tComplex or imaginary roots")
