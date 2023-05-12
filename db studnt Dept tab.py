import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect( 
  host="localhost",
  user="root",
  password="*14142021bw*",
  database = "student")  
#creating the cursor object  

cur = myconn.cursor()  
sql = "insert into Department(dept_id,dept_name)values (%s,%s)" 
val=[(201,"civil"),(202,"mech"),(207,"accounts")]
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
    myconn.commit()
      
except:  
    myconn.rollback()  
  
myconn.close()   


