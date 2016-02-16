# Prompt for user input  data #
import sqlite3
from flask import flask, render_template, request, session, \
	flash, redirect, url_for, get

# configuration

DATABAS = 'blog.db'

app = Flask(__name__)

#--- app configuration
app.config.from_object(__name__)

def connect_db() :
	retun sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__' :
	app.run(debug=True)

