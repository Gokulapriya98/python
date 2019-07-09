import mysql.connector
cnx = mysql.connector.connect(user='admin', password='admin123',
                              host='127.0.0.1',
                              auth_plugin='mysql_native_password')

print(cnx)
mycursor=cnx.cursor()
mycursor.execute("create database priya10")
mycursor.execute("show databases")
for x in mycursor:
    print(x)