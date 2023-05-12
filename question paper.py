# QUESTION PAPER : 1

# q - 2
# multiplying a string by a 3
string1="hai"
print(string1*3)

# q - 3
# checking types of triangles
side1=int(input("enter the first side of triangle :"))
side2=int(input("enter the second side of the triangle :"))
side3=int(input("enter the third side of the triangle :"))
if side1==side2==side3:
    print("this is an equilatrial triangle")
elif side1==side2 or side1==side3:
    print("this is an isosceles triangle")
else: print("this is a scalene triangle")

# q - 4
#checking a no is prime or not using while loop
num=int(input("enter a number :"))
flag=1
i=2
while i<=num/2:
    if num%i==0:
        flag=0
        break
    i+=1
if(flag==1):
    print(num,"prime number")
else:
    print(num,"not a prime number")

# q - 5 
# 1+2+6+24+120+.....for loop
n=int(input("enter the limit :"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact,"+",end=" ")


#  QUESTION PAPER : 2

# q - 2
# concatinate 2 strings
string1="Burhana"
string2="Wardhath"
print(string1+" "+string2)

# q - 3
# check a charecter is vowel or not
chara=input("enter a charecter :")
if chara in ('a','e','i','o','u'):
    print("vowel")
else:
    print("not vowel")

# q - 4
#fibonacci series using while loop
limit=int(input("enter the limit :")) 
num1=0
num2=1
sum=0
print("the fibonacci series is :",num1,num2,end=" ")
while sum<limit:
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum,end=" ")

# q - 5
# all the factors of a number using for loop
num=int(input("enter a number :"))
print("the factors are :",end=" ")
for i in range(1,num+1):
    if num%i==0:
        print(i,end=",")


# QUESTION PAPER : 3

# q - 2
# replace all instance of a substring in a string
string="example of replace all instance of substring in a string"
print(string.replace("string","**"))

# q - 3
#year is leap yr or not
year=int(input("enter the year :"))
if year%400==0:
    print("leap year")
elif year%100==0 and year%400!=0:
    print("not leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not leap year")

# q - 4
# print all the charecters in a string 'PYTHON' using while loop
string="PYTHON"
i=0
while i<len(string):
    print(string[i]) 
    i+=1

# q - 5
# display elements in a string presant at odd index position
string="ELEMENTS"
i=1
while i<len(string):
    print(string[i]) 
    i+=2

# QUESTION PAPER NO :4

# q - 2
# convert an integer to string
integer=int(2)
string1=str(integer)
print(string1)
print(type(string1))

# q - 3
# checking enterd number 3 digit or not
num=int(input("enter a number :"))
if num>999:
    print("enterd number is not 3 digit")
elif num<99:
    print("enterd number is invalid")
else:
    print("numberb is 3 digigt")  


# Q - 4
# 1++49
# 2++48
# 3++47
# 4++46
#   .
#   .
#   .
# 48++2
# 49++1

inc=1
dec=49
while inc<=49:
    print(inc,"++",dec)
    inc+=1
    dec-=1


# q - 5
# 
num=int(input("enter a number :"))
string=str(num)
rev=string[::-1]
for i in rev:
    print(i,end=" ")


# QUESTION PAPER N0 : 5

# q - 2
# string slicing
string1="string slicing"
print(string1[1])
print(string1[-1])

# q - 3
# checking last digit of a number is divisible by 3
num=int(input("enter a number :"))
lastdigit=num%10
if lastdigit%3==0:
    print(lastdigit,"is divisible by 3")
else:
    print("last digit not divisible by 3")

# q - 4
# first 10 whole numbers using while loop
i=0
while i<=10:
    print(i)
    i+=1

# q - 5
# print all the charecters of a string using for loop
string1="python"
for i in string1:
    print(i)


# QUESTION PAPER NO :6

# q - 2
#string is all uppercase
word="STRING"
print(word.isupper())

# q - 3
# display last digit of a number
num=int(input("enter a number :"))
lastdig=num%10
print("the last digit is:",lastdig)

# q - 4
# first 10 natural numbers using while loop
i=1
while i<11:
    print(i)
    i+=1

# q - 5
# 1,4,9,16,25,.... using for loop
limit=int(input("enter the limit :"))
for i in range(1,limit+1):
    print(i*i)




# QUESTION PAPER NO : 7

# q2
# first and last letter in upper case
string="burhana"
print(string[0].upper()+string[1:-1]+string[-1].upper())


# q3
# print 'hello' if enterd number divisible by 5 else print 'bye'
num=int(input("enter a number :"))
if num%5==0:
    print("hello")
else:
    print("bye")


# q 4
# first 10 odd no:
print("the first 10 odd numbers are :")
i=1
while i<20:
    print(i)
    i+=2

# q-5
# 0-->6 numbers printing except 3 and 6
print("the numbers are :")
for i in range(1,7):
    if i==3 or i==6:
        continue
    print(i)



# QUESTION PAPER NO :8

# q 2
#uppercase and lower case
string="Luminar Technolab"
print(string.upper())
print(string.lower())

# q 3
#number is devisible by 7 or not
num=int(input("enter a number :"))
if num%7==0:
    print("number is divisible by 7 ")
else:
    print("not")

# q -4
#first 10 even numbers using while loop
print("the first 10 even numbers are : ")
i=2
while i<21:
    print(i)
    i+=2

#q-5
#checking alphabet is a vowel,consenent or not using for loop
char=input("enter a charecter :")
vowel=('a','e','i','o','u')
for i in vowel:
    if char in vowel:
        print("vowel")
        break
    else:
        print("consonent")
        break



# QUESTION PAPER NUMBER :9

# q 2: integer added to string
string1="hai"
num=1
print(num+string1)


# q 3 : no is evev or not
num=int(input("enter a number :"))
if num%2==0:
    print("entered number is even",num)
else:
    print("not an even number")


# q-4 ,first 10 integers and sequence
i=1
print("the first 10 integers are :")
while i<=10:
    print(i,end=" , ")
    i+=1

# q-5 ,multiplication table of 24 using for loop
for i in range(1,11):
    mul=i*24
    print(i ,"*","24","=", mul)






