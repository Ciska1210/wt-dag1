print('Mysql read application')

import mysql.connector

dbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wt"
)

myCursor = dbconnection.cursor()
myCursor.execute("SELECT * FROM agents")

allAgents = myCursor.fetchall()

print(allAgents)

for a in allAgents:
    print(a[1])

#Extra commentaar