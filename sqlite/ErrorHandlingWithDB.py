# INSERT Command with Error Handler #
import sqlite3
import csv

from flask import Flask
#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()

	try :

		cursor.execute("INSERT INTO population VALUES('New York City','NY', 9000)")
		cursor.execute("INSERT INTO population VALUES('San Franscisco','CA',8000)")
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



