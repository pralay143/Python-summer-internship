import mysql.connector

conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prathu@143",
database="collegestudents"
)

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM student")

#To get only first row
#myresult = mycursor.fetchone()
#print(myresult)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
