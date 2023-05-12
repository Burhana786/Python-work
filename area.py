#area of rectangle,square,circle,triangle

choice=int(input("1-rectangle\n2-square\n3-circle\n4-triangle\nenter your choice :"))  #select any choice  #select choice
if choice==1:                               #for rectangle                      
    length=int(input("enter the length :"))
    breadth=int(input("enter the breadth"))
    print("area=",length*breadth)
elif choice==2:                             #for square
    side=int(input("enter the side:"))
    print("area=",4*side)
elif choice==3:                             #for circle
    radius=float(input("enter the radius:"))
    print("area=",3.14*radius*radius)
elif choice==4:                              #for triangle
    length=int(input("enter the length :"))
    breadth=int(input("enter the breadth"))
    print("area=",(length*breadth)/2)
else:
    print("invalid choice")