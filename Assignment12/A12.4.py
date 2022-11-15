print("Enter two number")
a=int(input())
b=int(input())

j=2
while a<=b:
    i=2
    while i<a:
        r=a%i
        if r==0:
            break
        i+=1
    else:
        print(a,end=" ")
    a+=1
