import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()
cursor.execute("drop database sqlclass")
connect.close()