import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="mydemo"
)

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM table_user")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
