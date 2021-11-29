import mysql.connector   
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student")  
mycursor=mysqldb.cursor()
def deletedata():
   try:   
      mycursor.execute("DELETE FROM STUDENT WHERE STUDENT_NO=1")
      mysqldb.commit() 
      print('Record deteted successfully...')  
   except:  
      
      mysqldb.rollback()  
   mysqldb.close()  