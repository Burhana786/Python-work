import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*14142021bw*"
)
cur=myconn.cursor()
try:
    cur.execute("create database Coach" )
except:
    myconn.rollback()
myconn.close()

