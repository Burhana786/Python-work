#1
num=5
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(col,end="")
    print()

#2
num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print(col,end="")
    print()

#3
num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print(row,end="")
    print()

#4
num=5
col=1
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(format(col,"3d"),end="")
    print()

#5
'''num=5
co1=1
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(format(col,"3d"),end="")
    col+=1
    print()'''

    #2
num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print(col,end="")
    print()