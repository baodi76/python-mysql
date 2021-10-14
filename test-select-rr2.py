import mysql.connector
import time

mydb = mysql.connector.connect(
	host="mysqlx-r-2.mysql.database.azure.com",
	user="didi@mysqlx-r-2",
	passwd="mysql123!@#",
	database="D1"
)
mydb.autocommit = True
mycursor = mydb.cursor()

for a in range(1000):
    print (a)
    time.sleep(10)
    mycursor.execute("SELECT count(*) from kmsg")
    myresult = mycursor.fetchall()
    print("the total <RR2> count is "+str(myresult[0][0]))

    #for x in myresult:
        #print("the total count is "+str([0][0]))
        #print(x)
        #myresult=0