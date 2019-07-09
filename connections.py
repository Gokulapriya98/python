import mysql.connector
cnx = mysql.connector.connect(user='admin', password='admin123',
                              host='127.0.0.1',database='priya',
                              auth_plugin='mysql_native_password')

print(cnx)
