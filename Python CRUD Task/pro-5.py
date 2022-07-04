import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="mydemo"
)

mycursor = conn.cursor()

sql = "DELETE FROM table_user WHERE user_id = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row deleted")
