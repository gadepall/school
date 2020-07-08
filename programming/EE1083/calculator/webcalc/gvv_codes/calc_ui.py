from flask import Flask,render_template,request
#import mysql.connector as mariadb
app=Flask(__name__)
@app.route('/')

def student():
	return render_template('calc.html')

if __name__=='__main__':
	app.run(debug = True)
