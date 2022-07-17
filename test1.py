
import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()
cursor.execute("use sqlclass")
cursor.execute("create table if not exits ineurondb(age int,job varchar(20),marital varchar(5),education varchar(20),'default' varchar(20),balance int,housing varchar(20),loan varchar(20),contact char(20),day int(5),month char(20),duration int(5),campaign char(20),pdays int(5),previous char(20),poutcome char(20),y char(20))")
cursor.execute("describe ineurondb")
# cursor.execute('insert into details values("sachin",23)')

# age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,y
# 58,management,married,tertiary,no,2143,yes,no,unknown,5,may,261,1,-1,0,unknown,no
# 44,technician,single,secondary,no,29,yes,no,unknown,5,may,151,1,-1,0,unknown,no
# 33,entrepreneur,married,secondary,no,2,yes,yes,unknown,5,may,76,1,-1,0,unknown,no
# 47,blue-collar,married,unknown,no,1506,yes,no,unknown,5,may,92,1,-1,0,unknown,no
# 33,unknown,single,unknown,no,1,no,no,unknown,5,may,198,1,-1,0,unknown,no
# 35,management,married,tertiary,no,231,yes,no,unknown,5,may,139,1,-1,0,unknown,no
# 28,management,single,tertiary,no,447,yes,yes,unknown,5,may,217,1,-1,0,unknown,no
# 42,entrepreneur,divorced,tertiary,yes,2,yes,no,unknown,5,may,380,1,-1,0,unknown,no

# connect.commit()
# cursor.execute('select * from details')
print(cursor.fetchall())
connect.close()