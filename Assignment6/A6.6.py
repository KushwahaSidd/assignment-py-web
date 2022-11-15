n=int(input("Enter the number"))
count=0
while n!=0:
    count+=1
    n=n//10
if count==3:
    print("Number is three digit")
else:
    print("NUMBER is not three digit")
