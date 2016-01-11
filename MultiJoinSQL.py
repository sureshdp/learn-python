# INSERT Command with Error Handler #
import sqlite3


#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	


	try :
		cursor.execute("""SELECT DISTINCT  population.cirty, population.population, 
		   regions.region FROM population, regions WHERE 
		   population.cirty = regions.city ORDER by 
		      population.cirty asc""" )
		rows = cursor.fetchall()
		for row in rows : 
			print "City : "  + row[0]
			print "Population : " + str(row[1])
			print "Region : " + row[2]
			print
			
			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



