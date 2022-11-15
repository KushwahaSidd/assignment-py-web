m=1
l1=[]
n=int(input("HOW  many number you want to enter"))
for i in range(n):
    l1+=[int(input("Enter the element"))]
for e in l1:
    m=m*e
print(m)
