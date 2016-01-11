# INSERT Command with Error Handler #
import sqlite3


#--- Create connection
with sqlite3.connect("cars.db") as conn :
	# get cursor
	cursor = conn.cursor()
	


	try :
		cursor.execute("""SELECT   Make,Model,Count(Quantity)  as 'Order' 
			FROM inventory  group by Make,Model,Quantity""" )
		rows = cursor.fetchall()
		for row in rows : 
			print ("Make :  {}  Model  {} ".format(row[0],row[1]))
			print "Order : " + str(row[2])
			print
			
			
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



