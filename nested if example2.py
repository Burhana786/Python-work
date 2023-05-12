num1=int(input("enter the first number: "))        #read num1,num2,num3 from user
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if(num1>num2):
    if(num1>num3):
        print("greatest number is ",num1)
    else:
        print("greatest number is",num3)    
else:
        if num2>num3:
            print("greatest number is ",num2)  
        else:
            print("num3 is greater")

