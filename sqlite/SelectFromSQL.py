# INSERT Command with Error Handler #
import sqlite3
import csv

from flask import Flask
#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	

	try :

		for row in cursor.execute("SELECT firstname, lastname from employees") : 
			print row 
			print row[0],row[1]
			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



