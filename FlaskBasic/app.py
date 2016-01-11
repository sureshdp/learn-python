# --- Flask Hello Mac World --- #
from flask import Flask
#--- Create Application object 
app = Flask(__name__)
# use decorators to link the function to a URL
#@app.route("/")

# error handling
app.config["DEBUG"] = True

@app.route("/test/<search_query>")
def search(search_query) :
	return search_query

@app.route("/integer/<int:value>")
def int_type(value) :
	print value + 1
	return "correct"

@app.route("/float/<float:value>") 
def float_type(value) :
	print value + 1
	return "correct"

@app.route("/path/<path:value>") 
def path_type(value) :
	print value 
	return "correct"

@app.route("/name/<name>") 
def  index(name) :
	if name.lower() == "suresh" :
		return "Hello, {}".format(name)
	else :	
		return "Not Found" , 404

# define the view using a function, which returns a string
@app.route("/hello") 
def hello_world():
	return "Hello, Mac World !?!?!?!"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()

