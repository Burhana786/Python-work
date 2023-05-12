# sample program

'''class classname:
    a=4
    def function(self):   # data illenkilum user functionil self kodukkanam
        print("hello")
obj=classname()
print(obj.a)
obj.function()'''

#  class using init()  /parameter construct

'''class classname:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def printfunction(self):
        print(f"two numbers are : {self.a},{self.b}")
            # f -->formatted function,ie ,combine strings & variable

obj=classname(4,6)
obj.printfunction()'''

# without passing parameter in class( so no init())

'''class classname:
    def printfunction(self,num1,num2):
        print(f"parameters are :{num1},{num2}")
obj=classname()
obj.printfunction(6,4)'''


# INHERITENCE
# 1 : single inheritance(1 child: 1 parent)
'''class mainclass:
    a=5
    def prints(self):
        print("hello")
class subclass(mainclass):
    b=20
obj=subclass()
print(obj.a)
print(obj.b)
obj.prints()'''


# example derrivng function of parent class
'''class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
d=Dog()
d.eat()
d.bark()'''

# another example
'''class Fruits:
    def juice(self):
        print("drink")
class Mango(Fruits):
    def eat(self):
        print("eat")
m=Mango()
m.juice()
m.eat()'''

# 2- multi level inheritance ( 1:parent, 1:child , 1:grandchild)

'''class mainclass:
    a=5
    def prints(self):
        print("parent class")
class subclass(mainclass):
    b=88
    def subfun(self):
        print("child class")
class grandchildclass(subclass):
    c=22
    def grandfun(self):
        print("grand child class")
obj=grandchildclass()
print(obj.a)
print(obj.b)
print(obj.c)
obj.prints()
obj.subfun()
obj.grandfun()'''

# example
'''class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Babydog(Dog):
    def weep(self):
        print("weeping")
b=Babydog()
b.eat()
b.bark()
b.weep()'''

# 3- multiple inheritance( more than one parent , 1 :child)

'''class mainclass1:
    a=3
    def prints(self):     # self kodukkunnath class property kittan
        print("parent class 1")
class mainclass2:
    b=55
    def subfun(self):
        print("parent class 2")
class childclass(mainclass1,mainclass2):
    c=11
    def grandfun(self):
        print("1 child class")
obj=childclass()
obj.prints()
obj.subfun()
obj.grandfun()'''

# multiple inheritence - same function for all class

'''class mainclass1:
    a=3
    def prints(self):     
        print("parent class 1")
class mainclass2:
    b=55
    def prints(self):
        print("parent class 2")
class childclass(mainclass1,mainclass2):
    c=11
    def prints(self):
        mainclass1.prints(self)
        mainclass2.prints(self)
        print("1 child class")
obj=childclass()
obj.prints()'''

# POLIMORPHISM

# example 1



# example 2: polimorphism with user-defined function
'''def add(x,y,z=0):
    return x+y+z
print(add(2,3))
print(add(2,3,4))'''



# example 3 : polimorphism with class(loop)
'''class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def langauge(self):
        print("Hindhi is most widely used langauge in India")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington,DC is the capital of USA")
    def langauge(self):
        print("English is most widely used langauge in USA")
    def type(self):
        print("USA is a developed country")
objind=India()
objusa=USA()
for country in(objind,objusa):
    country.capital()
    country.langauge()
    country.type()'''


# example 4 : polimorphism with METHOD OVERRIDING
'''class Bird:
    def intro(self):
        print("there are many types of birds")
    def flight(self):
        print("most birds can fly, some cannot")
class Sparrow(Bird):
    def flight(self):
        print("sparrow can fly")
class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")
objbird=Bird()
objspr=Sparrow()
objost=Ostrich()

objbird.intro()
objbird.flight()

objspr.intro()
objspr.flight()

objost.intro()
objost.flight()'''


# example 5 :polimorphism with class with function & objects  
class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def langauge(self):
        print("Hindhi is most widely used langauge in India")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington,DC is the capital of USA ")
    def langauge(self):
        print("English is most widely used langauge in USA")
    def type(self):
        print("USA is a developed country")

def func(obj):
    obj.capital()
    obj.langauge()
    obj.type()

objind=India()
objusa=USA()

func(objind)
func(objusa)


# ENCAPSULATION

'''class Base:                                 # creating a base class
    def ___init___(self):
        self._a=2                          # protected member  

class Derrived(Base):                      # creating a derrived class
    def __init__(self):
        Base.__init__(self)                # calling constructer of base class
        print("calling protected member of a base class : ",self._a)
        self._a=5                          # modify the protected variable
        print("calling modified protected member outside class : ",self._a )

obj1=Derrived()
obj2=Base()

# calling protected member can be accessed ,
# but should not be done due to convention
print("accessing protected member of obj1 :",obj1._a)
# accessing the protected variable outside
print("accessing protected member of obj2 : ",obj2._a)'''



























