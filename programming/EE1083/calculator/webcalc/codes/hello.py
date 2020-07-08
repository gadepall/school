from flask import Flask
#Import the Flask class
app = Flask(__name__)
#Flask take (__name__)as an argument.
@app.route('/')
# '/' which url should call the associate function.
def student():
	return "Hello World"
if __name__=='__main__':
#server runs if the scripts executed directly from python interpreter and not used as an imported module.
	app.run()
# runs the application on local server
