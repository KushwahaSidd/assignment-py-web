n=int(input("Enter a number"))
count=0
j=2
while j>0:
    i=2
    while i<j:
        r=j%i
        if r==0:
            break
        i+=1
    else:
        if count!=n:
            print(j,end=" ")
            count+=1
        else:
            break
    j+=1
