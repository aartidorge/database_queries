import mysql.connector
import datetime
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student") 
mycursor = mysqldb.cursor()
    
def insertdata():
   query = 'INSERT INTO STUDENT VALUES (%s, %s, %s, %s);'
   try:
      data = [
            (1, 'Marga', '1996-07-02', '2021-11-10'),
            (2, 'Theda', '1997-10-20', '2021-11-11'),
            (3, 'Marielle', '1995-2-10', '2021-10-18')
            ]

      mycursor.executemany(query, data)
   
      mysqldb.commit()
      print('{} records inserted'.format(mycursor.rowcount))
   except(Exception) as error:
      print(error)
   finally:
      if mysqldb is not None:
         mycursor.close()
         mysqldb.close()
         print('\nConnection closed')
   mysqldb.close()

