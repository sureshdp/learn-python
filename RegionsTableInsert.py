# INSERT Command with Error Handler #
import sqlite3


from flask import Flask
#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	
	cities = [
			('New York City', 'Northeast'),
			('San Francisco', 'West'), 
			('Chicago', 'Midwest'), 
			('Houston', 'South'), 
			('Phoenix', 'West'), 
			('Boston', 'Northeast'), 
			('Los Angeles', 'West'), 
			('Houston', 'South'), 
			('Philadelphia', 'Northeast'), 
			('San Antonio', 'South'), 
			('San Diego', 'West'), 
			('Dallas', 'South'),
			('San Jose', 'West'), 
			('Jacksonville', 'South'), 
			('Indianapolis', 'Midwest'), 
			('Austin', 'South'), 
			('Detroit', 'Midwest')
			]

	try :
		#cursor.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")
		cursor.executemany("INSERT INTO regions VALUES(?,?)", cities)
		cursor.execute("SELECT * FROM regions ORDER BY region ASC")
		rows = cursor.fetchall()
		for row in rows :
			print row[0] , row[1]

			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



