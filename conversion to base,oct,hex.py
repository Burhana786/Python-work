#octal
num=int(input("enter the number :"))
o=oct(num)                                         #convert to octal
print("after converting to octal :",end="")        #print octal
print(o)

#hexa decimal
h=hex(num)                                         #convert to hex
print("after converting to hexa decimal :",end="") #print hex
print(h)

#binary
num1=input("enter the binary number :")
num2=int(num1,2)                                   #convert to int
print("after converting to integer :",end="")                                  
print(num2)