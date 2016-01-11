# Create a SQLite3 database and table #
import sqlite3
import csv

from flask import Flask
#--- Create connection
with sqlite3.connect("new.db") as conn :
	# get cursor
	cursor = conn.cursor()
	

	# open the csv file and assign 
	employees = csv.reader(open("employees.csv","rU"))

	cursor.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
	cursor.executemany("INSERT INTO employees(firstname,lastname) values (?,?)",employees)


