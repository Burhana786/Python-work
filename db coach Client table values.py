import mysql.connector   
myconn = mysql.connector.connect( 
  host="localhost",
  user="root",
  password="*14142021bw*",
  database = "Coach"
  ) 

cur = myconn.cursor()  
sql = "insert into Client(Clientno, Name, City, Pin, Mobile)values (%s, %s, %s, %d, %s)"  
val = [("C00001","Ivan Bayross","Bombay",400054,"3456212343"),("C00002","Vandana Saitwal","Madras",780001,"8976532322"),("C00003","Pramada Jaguste","Bombay",400007,"9090898765"),()]  
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
    myconn.commit()
      
except:  
    myconn.rollback()  
  
myconn.close()   