# file1=open("demo.txt","a")
# file1.write("welcome to python world")
# file1.close()

# file2=open("demo.txt","r")
# print(file2.read(4))
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())


#EXISTS
'''import os
if os.path.exists("demo.txt"):
    pass         # demo file und,so aa line pass cheyyunnu
else:
    file1=open("demo.txt","x")
    file1.close()
file1=open("demo.txt","r")
print(file1.read())
file1.close()'''

# REMOVE
os.remove("demo1.txt")