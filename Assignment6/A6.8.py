a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
d=(b*b)-(4*a*c)
if d>0:
    print("Real and Distinct Roots")
elif d==0:
    print("Real and Equal Roots")
else:
    print("Imaginary root")
