def maxfour(*l2):
      l3=sorted(l2)
      i=-1
      while i>-5:
        print(l3[i])
        i-=1
l1=[]
n=int(input("how many number you want to enter"))
for i in range(n):
    l1+=[int(input("Enter a element"))]
maxfour(l1)

    
