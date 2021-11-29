import mysql.connector
from insertdata import *
from getdata import *
from deletedata import *
from updatedata import *
from getstudentist import *
import os

mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root12!@",database="Student") 
mycursor = mysqldb.cursor()

print('1:Insert')
print('\n2:Get All data')
print('\n3:Uppdate data')
print('\n4:Delete data')
print('\n5:Get Student List')
print('Enter your choice')
n=int(input())
if n==1:
    insertdata()
elif n==2:
    getdata()
elif n==4:
    deletedata()
elif n==3:
    updatedata()
elif n==5:
    getstudentlist()
else:
    print('Invalid choice')