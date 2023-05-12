import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect( 
  host="localhost",
  user="root",
  password="*14142021bw*",
  database = "student")  
#creating the cursor object  

cur = myconn.cursor()  
sql = "insert into Employee(name, id, salary, dept_id, branch_name)values (%s, %s, %s, %s, %s)"  
val = [("Binu",105,35000.00,207,"Alaska"),("jack",106,77000.00,202,"Uk")]  
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
    myconn.commit()
      
except:  
    myconn.rollback()  
  
myconn.close()   




