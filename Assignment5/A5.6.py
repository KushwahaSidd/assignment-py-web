print("Enter the three digit number")
n=int(input())
i=1
while i<3:
    r=n%10
    n=n//10
    i+=1
print(r)
