l1=[]
print("how many element you want to enter")
number=int(input())
for i in range(1,number+1,1):
    l1+=[int(input("Enter the number"))]
for i in l1:
    print(i,l1.count(i))
