import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*14142021bw*",
    database="Coach"
)
cur=myconn.cursor()
try:
    dbs = cur.execute("create table Client(Clientno char(6)primary key,Name varchar(20)not null,City varchar(50)not null,Pin int(10),Mobile varchar(10)" )
except:
    myconn.rollback()
myconn.close()

