dict1={"fruits1":"apple","fruits2":"mango"}
print(dict1.get("fruits1"))
print(dict1["fruits2"])
dict2={}
dict3=dict()                     # empty dictionary creation
print(dict1.items())
print(dict2)


# CREATION

dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=dict["model"]
#x=dict.get("model")
print(x)
print(dict)

# 2 : keys() ,updation
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.keys()
print(x)                            #before the change
car["color"]="black"
print(car)
print(x)                            # after the change 



# 3 : values() , updation

car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.values()
print(x)                      #before the change
car["year"]=2020
print(x)                      # after the change
x=car.items()
print(x)
car["color"]="red"
print(x)


# 4 : check if key exist

car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
if "model" in car:
    print("yes,model is the one of the key in dictionary")
# another example
if "color" in car:
    print("yes ,color is one of the key")
else:
    car.update({"color":"white"})
print(car)


# 5 : change values

# you can change the value of a specific item
#  by referring to its key name
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car["year"]=2018
print(car)


# 6 : update dictionary

car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.update({"color":"black"})
print(car)


# 7 : adding items

car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car["color"]="red"
print(car)


# 8 : removing items
# there are several methods to removing items
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.pop("model")
print(car)

# another
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.popitem()
print(car)

# values,items,index method
# print all items in dictionary
dict1={
    "data1":"new",
    "data2":"old"
}
for i,j in dict1.items():
    print(i,j)


#
myfamily={
    "child1":{
        "name":"email",
        "year":2004
    },
    "child2":{
        "name":"tobias",
        "year":2007

    },
    "child3":{
        "name":"thaara"
        "year":2009
    }
 }
print(myfamily["child1"["year"]])
print(myfamily["child3"]["name"])




















