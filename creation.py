import mysql.connector
cnx = mysql.connector.connect(user='admin', password='admin123',
                              host='127.0.0.1',database='priya10',
                              auth_plugin='mysql_native_password')

print(cnx)
mycursor = cnx.cursor()

sql = "INSERT INTO students (name,rollno,DOB,Gender,Department) VALUES (%s, %s,%s, %s,%s)"
val = [
 ('Priya',1, '1998-07-13','female','cse'),
 ('Amy',2,'1997-08-18','female','ece'),
 ('Hannah',3, '1999-06-21','female','IT'),
 ('Michael',4, '1996-04-05','male','eee'),
 ('Sandy',5, '1995-05-04','male','ece')
]

mycursor.executemany(sql, val)

cnx.commit()

print(mycursor.rowcount, "record was inserted.")
