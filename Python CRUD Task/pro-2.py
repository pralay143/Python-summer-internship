import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="myDemo"
)

mycursor = conn.cursor()

sql = "INSERT INTO table_user (user_id,user_firstname,user_lastname,user_address, user_email, user_password) VALUES(001,'Prajapati','Devanshi','Ahemdabad','d@gmail.com', 034),(002,'Sharma','Prachi','Rajkot','pr@gmail.com', 030),(003,'Suthar','Naiya','Bayad','na@gmail.com',027)"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row inserted.")