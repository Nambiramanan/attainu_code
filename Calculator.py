opt=0
while(opt !=6):
    print("\n\nEnter your option:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Display table\n6.Exit")
    opt=int(input())
    if(opt==0 or opt>6 ):
        print("\nPlease Select the Valid option")
    elif(opt==1):
        print("\nEnter the A and B Value:")
        a=int(input())
        b=int(input())
        c=a+b
        print("\nThe Addition of A and B is:",c)
    elif(opt==2):
        print("\nEnter the A and B Value:")
        a=int(input())
        b=int(input())
        c=a-b
        print("\nThe Subtraction of A and B is:",c)
    elif(opt==3):
        print("\nEnter the A and B Value:")
        a=int(input())
        b=int(input())
        c=a*b
        print("\nThe Multiplication of A and B is:",c)
    elif(opt==4):
        print("\nEnter the A and B Value:")
        a=int(input())
        b=int(input())
        c=a/b
        print("\nThe Divison of A and B is:",c)
    elif(opt==5):
        print("\nEnter the A Value:")
        a=int(input()) 
        for i in range(1,11):
            print(i,"*",a, "=", a*i)
    elif(opt==6):
        end = input("Confirm to Exit(Yes or No):\n")
        if(end == "Y" or end == "y" or end == "yes" or end == "yes"):
            break
        elif(end =="N" or end =="n" or end =="No" or end =="no"):
            opt=0
            
            
        
