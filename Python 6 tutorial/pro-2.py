import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="collegestudents"
)
mycursor = conn.cursor()
sql = "INSERT INTO student (Name, Rollnumber, Branch) VALUES ('Devanshi', 11, 'IT')"
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "row inserted.")
