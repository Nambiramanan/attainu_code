def getinput():
    a=int(input())
    return (a)
  
a=[]
sum=0
print("Enter the no size of list:")
l=getinput()
print("Enter the Values in list")
for i in range(0,l):
    x=getinput()
    a.append(x)
    sum=sum+a[i]
print("The List is:",a)    
print("The addition of the list is",sum)
        
        
    
    

