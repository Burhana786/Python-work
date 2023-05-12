# USING SET() METHOD

days=set(["monday","tuesday","wednesday","thursday",
"friday","saturday","sunday"])
print(days)
print(type(days))

print("looping through the set elements ... : ")
for i in days:
    print(i)

# ACCESS ITEMS
set1={"apple","banana","cherry"}
for x in set1:
    print(x)

# CHECKING ITEM using  IN 
set2={"apple","banana","cherry"}
print("banana" in set2)

# ADD ITEMS : .add()
set1={"apple","banana","cherry"}
set1.add("orange")
print(set1)  

# JOIN 2 SETS
# union
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)      # set3=set1+set2
print(set3)

# update
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)          #set1=set1+set2
print(set1)

#INTERSECTION
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.intersection_update(y)
print(x)


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.intersection(y)
print(z)


# SYMMETRIC DEFFERANCE
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.symmetric_difference_update(y)
print(x)



x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)


x={"apple","banana","cherry"}
y=x
z=x.copy()
x.add("mango")
print(x)
print(y)
print(z)

x={"apple","banana","cherry"}
del x


















