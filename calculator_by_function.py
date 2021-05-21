def getinput():
    a=int(input("Enter the a value:"))
    b=int(input("Enter the b value:"))
    return(a,b)
def getinput1():
    a=int(input("Enter the a value:"))
    return a
def getAdd(a,b):
     c=a+b
     print("The addition is:",c)
def getSub(a,b):
     c=a-b
     print("The Subtraction is:",c)
def getMul(a,b):
     c=a*b
     print("The Multiplication is:",c)
def getDiv(a,b):
     c=a/b
     print("The Division value is:",c)
def gettable(a):
     for i in range(1,11):
         print(i,"X",a, "=", a*i)
opt=0

while(opt!=6):
    print("\n\n","="*20,"\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Display table\n6.Exit\n","="*20,"\nEnter your option:")
    opt=int(input())
    if(opt==6):
        end = input("Confirm to Exit(Yes or No):\n")
        if(end == "Y" or end == "y" or end == "yes" or end == "yes"):
            break
        elif(end =="N" or end =="n" or end =="No" or end =="no"):
            opt=0
    if(opt==0 or opt>6):
        print("Enter the Valid option")
    if(opt==1):
        (a,b)=getinput()
        getAdd(a,b)
    if(opt==2):
        (a,b)=getinput()
        getSub(a,b)
    if(opt==3):
        (a,b)=getinput()
        getMul(a,b)
    if(opt==4):
        (a,b)=getinput()
        getDiv(a,b)
    if(opt==5):
        (a)=getinput1()
        gettable(a)
    






























