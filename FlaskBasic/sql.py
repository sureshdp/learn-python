# Prompt for user input  data #
import sqlite3
import random


#--- Create connection
with sqlite3.connect("blog.db") as conn :
	# get cursor
	cursor = conn.cursor()
	
	try :

		cursor.execute(""" CREATE TABLE posts 
			 (title TEXT, post TEXT)""")
		cursor.execute('INSERT INTO posts VALUES ("Good", "I\'m good.:")')
		cursor.execute('INSERT INTO posts VALUES ("Well", "I\'m well.:")')
		cursor.execute('INSERT INTO posts VALUES ("excellent", "I\'m excellent.:")')
		cursor.execute('INSERT INTO posts VALUES ("Okay", "I\'m okay.:")')
	except sqlite3.OperationalError :
		print "Something wrong...Try again..."



