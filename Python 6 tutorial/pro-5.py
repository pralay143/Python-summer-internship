import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="collegestudents"
)

mycursor = conn.cursor()

sql = "DELETE FROM student WHERE Rollnumber = 2"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "row deleted")
