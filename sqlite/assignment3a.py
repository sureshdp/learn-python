# INSERT random data #
import sqlite3
import random


#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	


	try :
		cursor.execute("DROP TABLE if exists numbers" )
		cursor.execute("CREATE TABLE numbers(num int)")
		for i in range(100) :
			cursor.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



