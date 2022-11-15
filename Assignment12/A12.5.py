n=int(input("Enter a number"))
n+=1
while n>0:
    i=2
    while i<n:
        r=n%i
        if r==0:
            break
        i+=1
    else:
        print(n)
        break
    n+=1
        
