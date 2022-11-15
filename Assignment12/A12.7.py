n=int(input("Enter a number"))
a=1
b=0
i=1
while i<=n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1
    
