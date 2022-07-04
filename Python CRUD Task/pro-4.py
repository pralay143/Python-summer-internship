import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="mydemo"
)

mycursor = conn.cursor()

sql = "UPDATE table_user SET user_lastname = 'Aarav' WHERE user_id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row updated")
