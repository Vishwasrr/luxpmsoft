from enum import auto
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="chonu@23",
    auth_plugin="mysql_native_password",
    database='R')

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="splunk_user",
#     password="password@23",
#     auth_plugin="mysql_native_password")

print(mydb)


mycursor = mydb.cursor()

# mycursor.execute('create database R')
# mycursor.execute('show databases')
# mycursor.execute("use R;")
mycursor.execute("create table oddnos  (key varchar(20), value varchar(100));")

# for db in mycursor:
#     print(db)

"""
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'chonu@23';
FLUSH PRIVILEGES;
"""
