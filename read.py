import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()

cursor.execute("use sqlclass")
cursor.execute("select * from bank_details")
for items in cursor.fetchall():
    print(items)

cursor.execute("select age , job from  bank_details ")
for items in cursor.fetchall():
    print(items)

cursor.execute("select `default` , age from  bank_details ")
for items in cursor.fetchall():
    print(items)

cursor.execute("select * from bank_details where  age = 41")
for items in cursor.fetchall():
    print(items)

cursor.execute("select * from bank_details where job = 'retired' and balance > 100")
for items in cursor.fetchall():
    print(items)
cursor.execute("select * from bank_details where education = 'primary' or balance < 100")
for items in cursor.fetchall():
    print(items)
cursor.execute("select distinct job from  bank_details ")
for items in cursor.fetchall():
    print(items)
cursor.execute("select * from bank_details order by age")
for items in cursor.fetchall():
    print(items)
cursor.execute("select * from bank_details order by age desc ")
for items in cursor.fetchall():
    print(items)
cursor.execute("select count(*) from bank_details")
for items in cursor.fetchall():
    print(items)
cursor.execute("select sum(balance) from bank_details")
for items in cursor.fetchall():
    print(items)
cursor.execute("select avg(balance) from bank_details")
for items in cursor.fetchall():
    print(items)
cursor.execute("select * from bank_details where  balance = (select min(balance) from bank_details ) ")
for items in cursor.fetchall():
    print(items)

cursor.execute("select * from bank_details1")
for items in cursor.fetchall():
    print(items)

connect.close()
