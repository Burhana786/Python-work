import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect( 
  host="localhost",
  user="root",
  password="*14142021bw*",
  database = "student")  
#creating the cursor object  

cur = myconn.cursor()  

      
try:  
    
    cur.execute("select Employee.name,Employee.id,Employee.salary,Department.dept_id,Department.dept_name from Departments join Employee on Department.dept_id=Employee.dept_id")  
    print("name id salary dept_id dept_name")
    for row in cur:
        print("%s %s %s %s %s"%(row[0],row[1],row[2],row[3],row[4]))
except:  
    myconn.rollback()  
  
myconn.close()   