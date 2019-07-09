import mysql.connector
cnx = mysql.connector.connect(user='admin', password='admin123',
                              host='127.0.0.1',database='priya10',
                              auth_plugin='mysql_native_password')

print(cnx)
mycursor=cnx.cursor()
mycursor.execute("CREATE TABLE students (name VARCHAR(255), rollno VARCHAR(255),DOB date,Gender varchar(255),Department varchar(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)