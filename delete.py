import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()
cursor.execute("use sqlclass")
cursor.execute("drop table bank_details")
cursor.execute("drop table bank_details1")
cursor.execute("drop database sqlclass")
connect.close()