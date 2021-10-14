import mysql.connector
import datetime

db = mysql.connector.connect(
	host="mysqlx-1.mysql.database.azure.com",
	user="didi@mysqlx-1",
	passwd="mysql123!@#",
	database="D1"
)
# getting the cursor by cursor() method
mycursor = db.cursor()

insertQuery = "insert into kmsg(message,createdate) values(%s,%s);"

i = 1
for i in range(1000000):
#while i < 6:
  print(i)
  i += 1
  currentDate = datetime.datetime.now()
  val = ("99yang"+str(i), currentDate)
  mycursor.execute(insertQuery, val)
  print("No of Record Inserted :", mycursor.rowcount)
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)

  # To ensure the Data Insertion, commit database.
  blukSize=100
  if i%blukSize==0:
    db.commit()
    print("commit every "+str(blukSize)+" records")


# close the Connection
db.close()
