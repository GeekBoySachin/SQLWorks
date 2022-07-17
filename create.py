import mysql.connector as conn

connect = conn.connect(host = "localhost",user = "root", password = "root")
print(connect)
cursor = connect.cursor()
cursor.execute("create database if not exists sqlclass")
cursor.execute("use sqlclass")
cursor.execute("create table if not exists bank_details (age int ,job varchar(30) ,marital varchar(30) ,education varchar(30),`default` varchar(30),balance int,housing varchar(30) ,loan varchar(30) ,contact varchar(30) ,`day` int ,`month` varchar(30) ,duration int ,campaign int ,pdays int ,previous int ,poutcome varchar(30),y varchar(30))")
cursor.execute("show tables")
for items in cursor.fetchall():
    print(items)
quries = [
            (44,"technician","single","secondary","no",29,"yes","no","unknown",5,"may",151,1,-1,0,"unknown","no"),
            (33,"entrepreneur","married","secondary","no",2,"yes","yes","unknown",5,"may",76,1,-1,0,"unknown","no"),
            (47,"blue-collar","married","unknown","no",1506,"yes","no","unknown",5,"may",92,1,-1,0,"unknown","no"),
            (33,"unknown","single","unknown","no",1,"no","no","unknown",5,"may",198,1,-1,0,"unknown","no"),
            (35,"management","married","tertiary","no",231,"yes","no","unknown",5,"may",139,1,-1,0,"unknown","no"),
            (28,"management","single","tertiary","no",447,"yes","yes","unknown",5,"may",217,1,-1,0,"unknown","no"),
            (42,"entrepreneur","divorced","tertiary","yes",2,"yes","no","unknown",5,"may",380,1,-1,0,"unknown","no"),
            (58,"retired","married","primary","no",121,"yes","no","unknown",5,"may",50,1,-1,0,"unknown","no"),
            (43,"technician","single","secondary","no",593,"yes","no","unknown",5,"may",55,1,-1,0,"unknown","no"),
            (41,"admin.","divorced","secondary","no",270,"yes","no","unknown",5,"may",222,1,-1,0,"unknown","no"),
            (29,"admin.","single","secondary","no",390,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),
            (53,"technician","married","secondary","no",6,"yes","no","unknown",5,"may",517,1,-1,0,"unknown","no"),
            (58,"technician","married","unknown","no",71,"yes","no","unknown",5,"may",71,1,-1,0,"unknown","no"),
            (57,"services","married","secondary","no",162,"yes","no","unknown",5,"may",174,1,-1,0,"unknown","no"),
            (51,"retired","married","primary","no",229,"yes","no","unknown",5,"may",353,1,-1,0,"unknown","no"),
            (45,"admin.","single","unknown","no",13,"yes","no","unknown",5,"may",98,1,-1,0,"unknown","no"),
            (57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),
            (60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no")
            ]
quries = ",".join([str(i) for i in quries])
cursor.execute("insert into bank_details values"+quries)

procedure1 = """
DELIMITER &&  
create procedure select_pre() 
BEGIN
	select * from bank_details; 
END &&  
"""

# cursor.execute(procedure1)
# cursor.execute("call select_pre()")

procedure2 = """
DELIMITER &&  
create procedure select_pre_filter2(IN var int ,IN var1 varchar(30)) 
BEGIN
	select * from bank_details where job = var1 and balance > var;
END &&   
"""
# cursor.execute(procedure2)
# cursor.execute("call select_pre_filter2((100 ,'services' )")


cursor.execute("create table if not exists bank_details1 (age int ,job varchar(30) ,marital varchar(30) ,education varchar(30),`default` varchar(30),balance int,housing varchar(30) ,loan varchar(30) ,contact varchar(30) ,`day` int ,`month` varchar(30) ,duration int ,campaign int ,pdays int ,previous int ,poutcome varchar(30),y varchar(30))")
cursor.execute("insert into bank_details1 select * from bank_details")


connect.close()






