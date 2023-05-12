limit=int(input("enter the limit :"))
num1=sum=0
num2=1
print("the fibnoccci series is:")
print(num1)
print(num2)
for i in range(0,limit):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum)
print("end of loop")