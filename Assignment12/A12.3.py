#n=int(input("Enter a number"))
j=2
while j<100:
    i=2
    while i<j:
        r=j%i
        if r==0:
            break
        i+=1
    else:
        print(j,end=" ")
    j+=1

