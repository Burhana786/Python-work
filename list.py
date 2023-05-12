# type

from operator import truediv


'''list1=["apple","cherry","banana"]
list2=[1,2,3,4,5]
print(type(list1))
print(type(list2))'''

# compare 2 list

list2=[1,2,"peter",450,"rockey",5,6]
list1=[1,2,5,"peter",450,"rockey",6]
print(list1==list2)

list3=["bunu","zinu",1,2,3]
list4=["bunu","zinu",1,2,3]
print(list3==list4)

# indexing,slicing

list1=[1,2,3,4,5,6,7]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[0:6])
print(list1[:])
print(list1[2:5])
print(list1[1:6:2])
print(list1[:-1])
print(list1[1:2:-2])
print(list1[3:7])
print(list1[2::-1])
print(list1[::-2])

# LIST OPERATIONS

# 1- concatination and repetition
list1=[1,"welcome",2,"bye"]
list2=[1,2,3,4]
list3=[5,6,7,8,9]
print(list2+list3)
print(list2*2)
print(list3*3)

# 2- membership operator
print(2 in list2)
print(7 in list3)

# 3- iteration using for loop
for i in list3:
    print(i)

# 4-length
print(len(list1))
print(len(list2))
print(len(list3))    

# 5-iteration using while loop
i=0
while i<len(list1):
    print(list1[i])
    i+=1

# 6-append() method
fruits=["apple","banana","cherry"]
fruits.append("mango")
print(fruits)

# 7- insert() method
fruits=["apple","banana","cherry"]
fruits.insert(1,"orange")
print(fruits)

# 8-extend() method
list1=["apple","banana","cherry"]
list2=["plums","papaya","grapes"]
list1.extend(list2)
print(list1)

# 9-remove()
list1=["apple","banana","cherry"]
list1.remove("banana")
print(list1)

# 10- pop()
list=["apple","cherry","banana"]
list.pop(1)
print(list)

# not specifying index no to pop(),removes last item
list=["apple","cherry","banana"]
list.pop()
print(list)

# 11- del() also delete the specified index
fruits=["apple","banana","cherry","mango"]
del fruits[2]
print(fruits)
# del() delets the list compleatly
fruits=["apple","banana","cherry","mango"]
del fruits
#print(fruits)

# 12- clear()
list=["apple","banana","cherry","mango"]
list.clear()
print(list)

# 13- loop through index numbers

list=["apple","banana","cherry","mango"]
for i in range(len(list)):
    print(list[i])

# 14- split()

'''strs="burhana wardhath"
s=list(strs.split(" "))
print(s)
print(type(s))
x=strs.split(" ")
print(type(x))'''

#built in functions in list
# 1- cmp()
# list1=[1,2,3,4]
# list2=[2,3,4]
# 2-list(seq),it converts any sequence to list
# string="burhana"
# s=list(string)
# print(type(s))





# sort()
# list=["apple","banana","pappaya","mango"]
# list.sort()
# print(list)

# sort()
# list=[3,5,8,2,1]
# list.sort()
# print(list)

# sort() descending
# list=["apple","banana","pappaya","mango"]
# list.sort(reverse = True)
# print(list)

# descending
# list=[3,5,8,2,1]
# list.sort(reverse = True)
# print(list)

# sorting without using sort()
# list1=["kiwi","apple","banana","pappaya","mango"]
# print(list1)
# print(sorted(list1))
# print(list1)


# FUNCTIONS

# 1- CUSTOMIZE SORT FUNCTION-sort the list based on how close the number is to 50
# def myfunc(n):
#     return abs(n - 50)

# list=[100,50,65,82,23]
# list.sort(key = myfunc)
# print(list)

# 2- CASE INSENSITIVE SORT
fruits=["Banana","Orange","kiwi","apple","Mango"]
fruits.sort(key = str.lower)
print(fruits)

# 3- REVERSE ORDER  ,just reverse the list
fruits=["banana","Orange","Kiwi","cherry"]
fruits.reverse()
print(fruits)

# 4- COPY A LIST : make a copy of a list with copy() method
list=["apple","banana","cherry"]
list1=list.copy()
print(list1)


# 09-08-22

# 1: sum all the items in a list
list=[1,2,3,4]
print(sum(list))

# 2: multiplies all the items in a list  (repetition)
list1=["apple","banana",1,2,3]
print(list1*2)

# 3 & 4: largest & smallest no: from a list
list1=[2,4,6,1,8,3]
print(max(list1))
print(min(list1))

# 5: check a list is empty or not
#(by checking len() method)
list1=[1,2,3,"apple"]
if(len(list1))==0:
    print(" this is an empty list")
else:
    print("this is not an empty list")

print(list1 is None)            # by checking non method

# example
list2=[]
print(len(list2)==0)