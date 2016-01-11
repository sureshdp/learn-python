# Create a SQLite3 database and table #
import sqlite3
from flask import Flask
#--- Create connection
conn = sqlite3.connect("cars.db")

# get cursor
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
				(Make TEXT, Model TEXT, Quantity INT)""")

# close the DB connection
conn.close()

