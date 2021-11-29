import mysql.connector  
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student")
mycursor=mysqldb.cursor()
def updatedata():
   try:  
      mycursor.execute("UPDATE STUDENT SET STUDENT_NAME='Saurabh Rao', STUDENT_DOB='1997-03-03',STUDENT_DOJ='2021-10-21' WHERE STUDENT_NO = 11")
      mysqldb.commit() 
      print('Record updated successfully...')   
   except:   
      
      mysqldb.rollback()  
   mysqldb.close()