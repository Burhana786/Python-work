num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))
choice=int(input("1-addition\n2-subtraction\n3-multiplication\n4-division\nenter your choice"))
if(choice==1):
    print("result is :",num1+num2)
elif(choice==2):
    print("result is :",num1-num2)
elif(choice==3):
    print("result is :",num1*num2)
elif(choice==4):
    print("result is :",num1/num2)
else:
    print("invalid choice")