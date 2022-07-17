import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()
cursor.execute("use sqlclass")
cursor.execute("update bank_details set balance = 0 where job = 'unknown'")
cursor.execute("update bank_details set contact = 'known' , y = 'yes' where month = 'may'")
cursor.execute("update bank_details set `default` = 'NULL' where `default`= 'no'")

cursor.execute("select * from (select  job , age , education , y from bank_details ) as a where a.age = 58")
for items in cursor.fetchall():
    print(items)


cursor.execute("create view bank_view as select  job , age , education , y from bank_details")
cursor.execute("select * from bank_view where age = 58")
for items in cursor.fetchall():
    print(items)

cursor.execute("select * from bank_details")
for items in cursor.fetchall():
    print(items)
connect.close()