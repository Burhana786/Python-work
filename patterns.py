# num=5
# spaces=6
# cols=1
# for row in range(0,int(num/2)+1):
#     #spaces
#     for space in range(1,spaces):
#         print(" ",end="")
#     spaces=1
#     #col
#     for col in range(1,cols+1):
#         print("*",end="")
#     print()
#     cols+=1
# #row
# for row in range(int(num/2),num+1):
#     #spaces
#     for space in range(1,space):
#         print

# num=5
# spaces=5
# #row
# for row in range(num+1,1,-1):
#     #space
#     for space in range(1,spaces):
#         print("",end=" ")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line




# num=5
# spaces=5
# #row
# for row in range(num+1,1,-1):
#     #space
#     for space in range(1,spaces):
#         print("",end="")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line




# num=5
# spaces=5
# #row
# for row in range(num+1,1,-1):
#     #space
#     for space in range(1,spaces):
#         print(" ",end=" ")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line






# num=5
# spaces=5
# #row
# for row in range(1,num+1):
#     #space
#     for space in range(1,spaces):
#         print(" ",end=" ")
#     spaces-=1
#     #col
#     for col in range(1,row+1):
#         print("*",end=" ")  #for column
#     print()  #for new line
# spaces=2
# for row in range(num,1,-1):
#     #space
#     for space in range(1,spaces):
#         print(" ",end=" ")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line


# num=5
# spaces=5
# #row
# for row in range(1,num+1):
#     #space
#     for space in range(1,spaces):
#         print(" ",end="")
#     spaces-=1
#     #col
#     for col in range(1,row+1):
#         print("*",end=" ")  #for column
#     print()  #for new line
# spaces=2
# for row in range(num,1,-1):
#     #space
#     for space in range(1,spaces):
#         print(" ",end="")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line


# num=5
# spaces=5
# #row
# for row in range(1,num+1):
#     #space
#     for space in range(1,spaces):
#         print("",end="")
#     spaces-=1
#     #col
#     for col in range(1,row+1):
#         print("*",end=" ")  #for column
#     print()  #for new line
# spaces=2
# for row in range(num,1,-1):
#     #space
#     for space in range(1,spaces):
#         print("",end="")
#     spaces+=1
#     #col
#     for col in range(0,row-1):
#         print("*",end=" ")  #for column
#     print()  #for new line




# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()

# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

# num=5
# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(col,end=" ")
#     print()


# num=9
# for row in range(1,num):
#     for col in range(-1+row,-1,-1):
#         print(format(2**col,"4d"),end=" ")
#     print()

# num=9
# for row in range(1,num):
#     for col in range(-1+row,-1,-1):
#         print(format(2**col,"4d"),end=" ")
#     print()

# num=5
# colm=1
# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(colm,end=" ")
#         colm+=1
#     print()

# #format method
# num=5
# colm=1
# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(format(colm,"3d"),end=" ")
#         colm+=1
#     print()


# character=65
# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(chr(character),end=" ")
#         character+=1
#     print()


# num=5
# for row in range(1,num+1):
#     for col in range(num):
#         print("%",end=" ")
#     print()


# character=65
# spaces=6
# num=5
# for row in range(1,num+1):
#     for space in range(1,spaces):
#         print(" ",end=" ")
#     spaces-=1
#     for col in range(1,row+1):
#         print(chr(character),end=" ")
#         character+=1
#     print()

# num=9
# for row in range(1,num):
#     for col in range(0,row,1):
#         print(format(2**col,"4d"),end=" ")
#     for  col in range(-1+row,-1,-1):
#         print(format(2**col,"4d"),end=" ") 
#     print()

#21-7-2022
#exponenet pattern
'''rows = 9
for i in range(1, rows):                        #for row
    for j in range(i-1, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    #for i in range(-1 + i, -1, -1):
        #print(format(2 ** i, "4d"), end=' ')
    print("")'''

    # number pattern
'''n=1
inc=1
for i in range(0,5):
    for j in range(0,inc):
        print(n,end="")
        n=n+1
    print()
    inc=inc+2'''
# pattern

'''for i in range(1,6):         # i-row1,j=row2,k=col
    print("+",end="")
print()
for j in range(1,4):
    for k in range(1,6,4):
        #if k==3 and j==3:
        if k==1 or k==5:
            print(" -",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,6):         # i-row1,j=row2,k=col
    print("+",end="")'''
    











    #pattern
















    #hello

'''for i in range(1,10):         # i-row1,j=row2,k=col
    print("+",end="")
print()
for j in range(1,10):
    for k in range(1,10):
        if j==5:
            print("+ hello +",end="")
            break 
        elif k==1 or k==9:
            print("+",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,10):         # i-row1,j=row2,k=col
    print("+",end="")'''