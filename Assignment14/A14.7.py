l1=[10,20,30,10.5,"sidd",25,15.6]
i=0
count=0
while i<6-count:
    if type(l1[i])!=int:
        l1.remove(l1[i])
        i+=1
        count+=1
        
print(l1)
