# 1- CREATING TUPLE

'''tuple1=(101,"peter",22)
tuple2=("apple","banana","orange")
t3=10,20,30,40,50
print(type(tuple1))
print(type(tuple2))
print(type(t3))'''

# 2 - CREATING TUPLE WITH SINGLE ELEMENT

'''t1=("bunu")
print(type(t1))
# creating a tuple with single element using ,
t2=("bunu",)
print(type(t2))'''

# 3 - INDEXING

'''tup=(1,2,3,4,5,6,7)
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[::-2])'''
# index error
#print(tup[8])

# 4 - TUPLE INDEX OUT OF RANGE

'''t1=(1,2,3,4,5,6,7)
# elt 1 --> end
print(t1[1:])
# elt 0 --> 3
print(t1[:4])
# elt 1--> 4
print(t1[1:5])
# elt 0-->6 and take step 2
print(t1[0:6:2])'''


# 5 - NEGATIVE INDEXING

'''t1=(1,2,3,4,5)
print(t1[-1])
print(t1[-4])
print(t1[-3:-1])
print(t1[:-1])
print(t1[-2:])'''

# 6 - DELETING TUPLE
# cannot delet , error occure
'''t1=(1,2,3,4,5,6)
print(t1)
del t1[0]
print(t1)
del t1
print(t1)'''

# 7 - BASIC TUPLE OPERATIONS
# conctn(+),repetation(*),membership(in) are same as list

'''t1=(1,2,3,4,5)
t2=(6,7,8,9)'''
# repetition
'''print(t1*2)'''
# concatination
'''print(t1 + t2)'''
# membership ,true if particular item in tuple,otherwise false
'''print(2 in t1)'''
# iteration
#for i in t1:
    

# EXAMPLE : 1
tup1=1,2,3,4,5,6,7
tup2=()
print(list(tup1))
list1=list(tup1)
print(list1)
del list1[0]
print(list1)
del list1[4]
print(list1)
del list1[4]
print(list1)
list2=[1,6,7]
list2.append(8)
print(list2)
print(tuple(list2))
t2=tuple(list2)
print(t2)

# EXAMPLE : 2
tup1=(1,2,3,4,5,6,7)
print(tup1)
list1=list(tup1)
print(list1)
list1.pop()   # last index remove
del list1[1]
list1.remove(5)
print(list1)
list1.append(8)
tup=(8,9,10)
list1.extend(tup2)
print(list1)

tup1=(1,2,3)
list1=list(tup1)
list1.pop()
print(list1)
print(tuple(list1))


