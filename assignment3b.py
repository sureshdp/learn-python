# Prompt for user input  data #
import sqlite3
import random


#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	
	prompt = """
	Select the operation that you want
	1. Average
	2. Max
	3. Min
	4. Sum
	5. exists
	"""


	try :

		while True :
			x = raw_input(prompt)

			# if user enters 
			if x in set (["1","2","3","4","5"]) :
				# parse the input
				operation = {1:"avg", 2:"Max", 3:"Min",4:"Sum"}[int(x)]
				cursor.execute("SELECT {}(num) FROM numbers" .format(operation))
				get = cursor.fetchone()
				print operation + ": %f" % get[0]
			elif x == 5 :
				print "Exit"
				break	

	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



