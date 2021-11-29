import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student") 
mycursor=mysqldb.cursor()
def getdata():
   try:  
      mycursor.execute("select * from STUDENT")
      result=mycursor.fetchall()  
      for i in result:    
         roll=i[0]  
         name=i[1]  
         dob=i[2]  
         doj=i[3]
         print(roll,name,dob,doj)  
   except:   
      print('Error:Unable to fetch data.') 

   mysqldb.close()