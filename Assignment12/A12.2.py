n=int(input("Enter a number"))
i=2
while i<n:
    r=n%i
    if r==0:
        break
    i+=1
if i==n:
    print("Prime Number")
else:
    print("Not Prime Number")
