# ADDITION
from unicodedata import name


'''def sum(num1,num2):
    print(num1+num2)
sum(1,9)'''

#SUBTRACTION
'''def sub(num1,num2):
    print(num1-num2)
sub(6,2)'''

# MULTIPLICATION
'''def mul(num1,num2):
    print(num1*num2)
mul(2,6)'''

# DIVISION
'''def div(num1,num2):
    print(num1/num2)
div(6,3)'''

# doc string printing
'''def sums(num1,num2):
    "this prints a passed string into this function"
    print(num1+num2)

sums(2,5)
print(sums.__doc__)'''

# RETURN
'''def sums(num1,num2):
    "this prints a passed string into this function"
    num3=num1+num2
    return num3
print(sums(5,3))
print(sums.__doc__)
print("2nd",sums(10,4))'''


# ARGUMENTS


# keyword  argument

'''def data(id,name,age):
    print("id:",id)
    print("name",name)
    print("age",age)
data1=data(name="bunu",id=101,age=23)
print(data1)'''
# print(type(data1))

# default argument

'''def data(id,name,age=14):
    print("id:",id)
    print("name",name)
    print("age",age)
data1=data(name="bunu",id=101)
print(data1)'''

# function defnition is here
'''def changeme(mylist):
    mylist.append([1,2,3,4])
    print("values inside the function",mylist)
    return
# now you call the function
mylist=[10,20,30]
changeme(mylist)
print("values outside the function",mylist)'''


# arbitary argument

'''def numbers(*num):
    print(type(num))
    print(num)
    print(len(num))
    print(num[1])
numbers(1,2,3)'''

# arbitary keyword argument

'''def datas(**item):                         # item=variable name
    print(type(item))
    print(len(item))
    print(item)
    print(item["name"])
    #print(item["id"])   error varum

datas(name="one",age="two")
print(">>>>>>>>>>>>>>>>>>>>>>>")
datas(id=101,name="john",age=21)'''


# variable length argument

'''def numbers(a,*b,c):
    print(a)
    print(b)
    print(c)
    print(type(numbers))
    print(type(a))
    print(type(b))
    print(type(c))
numbers(1,2,3,4,5,6,7,c=9)'''


# ANONYMUS FUNCTIONS

'''sum=lambda arg1,arg2:arg1+arg2
# now you can call sum as a function
print("value of total :",sum(10,20))
print("value of total :",sum(20,40))

sum=lambda a,b,c:a-b+c
print(sum(4,3,2))'''

# same in normal functionil
'''def sum(a,b,c):
    print(a-b+c)       # normal functionil onniladhikam -
    print(a+b)         # - operations cheyyam
sum(4,3,2)'''


# RETURN STATEMENT

'''def sum(arg1,arg2):                  # function definition
    total= arg1 + arg2               # add both parameter and return them
    print("inside the function :",total)
    return total
#now you can call sum function
total = sum(10,20)
print("outside the function :", total)'''



# define a function 2 values and return its sum,sub,mul
'''def opern(num1,num2):
    print("sum =",num1+num2)
    print("sub =",num1-num2)
    print("mul =",num1*num2)
    return opern
opern(2,4)'''


# define a function that accept roll no,and return whether the student is present or not
'''def student(num1):
    rollno=[2,4,6,1,5]
    if num1 in rollno:
        print("present")
    else:
        print("absent")
num1=int(input("enter a number :"))
student(num1)'''


# accept a no and return whether the no is even or odd
'''def oddoreven(num1):
    if num1%2==0:
        print("even")
    else:
        print("odd")
num1=int(input("enter a number :"))
oddoreven(num1)'''


# maximum of 3 numbers
'''def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("the largest number is :",num1)
    elif num2>num1 and num2>num3:
        print("largest is :",num2)
    else:
        print("largest number  is :",num3 )

num1=int(input("enter the first no :"))
num2=int(input("enter the second no :"))
num3=int(input("enter the third no :"))
max(num1,num2,num3)'''


# maximum of 3 nos another method

'''def maximum(num1,num2,num3):
    print(max(num1,num2,num3))
maximum(num1=int(input("enter the first no :")),num2=(int(input("enter the second no :"))),num3=int(input("enter the third no :")))'''

# count the vowel and not vowels in a word

'''def vowels(string1):
    vowel=['a','e','i','o','u']
    if string1 in vowel:'''
        

# factorial

'''def factorial(limit):
    fact=1
    for i in range(1,limit+1):
        fact=fact*i
    print("factorial is :",fact,end=" ")

limit=int(input("enter the limit :"))
factorial(limit)'''


# RECURSIVE FUNCTION

# 1-factorial
'''def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=5
print(factorial(num))'''

# 2 -sum of 5 nos

'''def sums(x):
    if x==1:
        return 1
    else:
        return(x+sums(x-1))
num=5
print(sums(num))'''

# 3 - fibanocci series

'''def fib(limit):
    if limit<=1:
        return limit
    else:
        return(fib(limit-1)+fib(limit-2))
num=10
for i in range(num):
    print(fib(i),end=" ")'''



   
# RETURNING MULTIPLE VALUES IN PYTHON

# 1 - using object

class Test:
    def __init__(self):
        self.str="geeks for geeks"
        self.x=20
def fun():
    return Test()
t=fun()
print(t.str)
print(t.x)


# 2 - using tuple

# A Python program to return multiple 
# values from a method using tuple
  
# This function returns a tuple
def fun():
    str = "geeksforgeeks"
    x   = 20
    return str, x;  # Return tuple, we could also
                    # write (str, x)
  
# Driver code to test above method
str, x = fun() # Assign returned tuple
print(str)
print(x)

# 3 - using list

# A Python program to return multiple 
# values from a method using list
# This function returns a list
def fun():
    str = "geeksforgeeks"
    x = 20   
    return [str, x];  
# Driver code to test above method
list = fun() 
print(list)

# 4 - using dictionary

# A Python program to return multiple 
# values from a method using dictionary
# This function returns a dictionary
def fun():
    d = dict(); 
    d['str'] = "GeeksforGeeks"
    d['x']   = 20
    return d
# Driver code to test above method
d = fun() 
print(d)


# 5 - using data class

from dataclasses import dataclass
@dataclass
class Book_list:
    name: str
    perunit_cost: float
    quantity_available: int = 0        
    # function to calculate total cost    
    def total_cost(self) -> float:
        return self.perunit_cost * self.quantity_available
      
book = Book_list("Introduction to programming.", 300, 3)
x = book.total_cost()
# print the total cost
# of the book
print(x) 
# print book details
print(book) 
# 900
Book_list(name='Python programming.',
          perunit_cost=200,
          quantity_available=3)

 











