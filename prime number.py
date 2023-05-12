flag=0
num=int(input("enter the number :"))
for i in range(2,num):
    if num%2==0:
        flag=1
        break
if(flag==1):
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")