num=int(input("enter the number:"))
rev=0
temp=num
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if rev==temp:
    print(temp,"is palindrom")
else:
    print(temp,"is not palindrom")