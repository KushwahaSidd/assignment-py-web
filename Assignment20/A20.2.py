def prime(n):
    i=2
    while i<n:
        p=n%i
        if p==0:
            print("Not Prime number")
            break
        i+=1
    else:
        print("prime number")

n=int(input("Enter the number"))
prime(n)
