import mysql.connector    
myconn = mysql.connector.connect( host="localhost",
  user="root",
  password="*14142021bw*",
database = "student")  

cur = myconn.cursor()  
  
try:  
  dbs = cur.execute("create table Department(dept_id int(20)primary key not null,dept_name varchar(10)not null)");  
except:  
    myconn.rollback()  
  
myconn.close()   

