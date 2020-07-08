from flask import Flask,render_template,request
import mysql.connector as mariadb
app=Flask(__name__)
@app.route('/')
def list():
	conn=mariadb.connect(user='root',password='123',database='Test')
	# Connecting to Database 
	cur=conn.cursor()
	cur.execute("Select * from test") #This query is used to fetch the Data from the Database
	rows=cur.fetchall()
	return render_template("display.html",rows=rows)
	# Returning display.html File
if __name__ == '__main__':
	app.run(debug = True)
