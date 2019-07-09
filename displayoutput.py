import mysql.connector
cnx = mysql.connector.connect(user='admin', password='admin123',
                              host='127.0.0.1',database='priya10',
                              auth_plugin='mysql_native_password')
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)