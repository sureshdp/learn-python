# INSERT Command with Error Handler #
import sqlite3
import csv

from flask import Flask
#--- Create connection
with sqlite3.connect("cars.db") as conn :
	# get cursor
	cursor = conn.cursor()
	
	cars = [
			('Honda', 'Accord', 10),
			('Honda', 'CR-V', 6),
			('Ford','Taurus',11),
			('Ford','F-150',5),
			('Ford','Focus',3)
			]

	try :
		cursor.executemany('INSERT INTO inventory Values(?,?,?)', cars)
		cursor.execute("UPDATE inventory SET Quantity=20 WHERE (Make='Ford' and Model != 'Focus')")
		for row in cursor.execute("SELECT * from inventory WHERE Make='Ford'" ) : 
			print row 
			
			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



