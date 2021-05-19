l=int(input("Enter the Limit for check:"))
print("The perfect numbers are:")
for i in range(1,l):
    sum=0 
    for j in range(1,(i//2)+1):
        r=i%j
        if(r==0):
            sum=sum+j
    if(sum==i):
         print(sum)
