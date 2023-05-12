#error program

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if (num1!=num2!=num3):
    if(num1==num2==num3):
        print("numbers are equal")
    else:
        if(num1>num2)and(num1>num3):
            print("greastest number is ",num1)
        elif(num2>num1)and(num2>num3):
            print("greatest number is",num2)
        else:
            print("greatest number is",num3)
    if(num1<num2)and(num1<num3):
         print(num1 ,":is smallest")    
    elif(num2<num1)and(num2<num3):
                print(num2,":is smallest") 
    else:   
            print(num3,":is smallest")
else:
    print("not")