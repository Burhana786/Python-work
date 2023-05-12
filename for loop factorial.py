limit=int(input("enter the limit:"))
print("the factorial is :")
fact=1
for i in range(1,limit+1):
    fact=fact*i
print(fact,end="")
