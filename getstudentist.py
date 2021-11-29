import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student") 
mycursor=mysqldb.cursor()
def getstudentlist():
   try:  
      mycursor.execute("select STUDENT_NO, STUDENT_NAME from STUDENT")
      result=mycursor.fetchall()  
      for i in result:    
         roll=i[0]  
         name=i[1]  
         print(roll,name)  
   except Exception as e:   
      print(e) 

   mysqldb.close()
