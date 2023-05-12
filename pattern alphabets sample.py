'''character=65
num=5
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(chr(character),end="")
        character+=1
    print()

character=65
num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print(chr(character),end="")
    character+=1
    print()'''



'''character=65
num=5
cols=1
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(chr(character),end="")
    cols+=1
    print()'''

'''num=5
spaces=5
for row in range(1,num+1):
    for col in range(1,col):
        print("%",end="")
    print()'''

'''num=9
for row in range(1,num):
    for col in range(-1+row,-1,-1):
        print(format(2**col,"4d"),end="")
    print()


num=5
for row in range(1,num+1):
    for col in range(num):
        print("%",end="")
    print()'''

