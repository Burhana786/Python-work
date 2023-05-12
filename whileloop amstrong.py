num=(input("enter a number :"))
sum=0
length=len(num)
temp=num=int(num)
while num>0:
    rem=num%10
    sum=sum+rem**length
    num=num//10
if sum==temp:
    print(temp,"is amstrong number")
else:
    print(temp,"is not amstrong ")  