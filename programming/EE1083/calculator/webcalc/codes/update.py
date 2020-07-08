from flask import Flask,render_template,request
import mysql.connector as mariadb
app=Flask(__name__)
@app.route('/')
def list():
	conn=mariadb.connect(user='root',password='123',database='Test')
	# connecting to the database
	cur=conn.cursor()
	cur.execute("Select * from test")
	# fetching all the data from test table.
	rows=cur.fetchall()
	return render_template("show.html",rows=rows)
	#returning show.html file

@app.route ('/testupdate', methods =['GET','POST'])
def testupdate():
	conn=mariadb.connect(user='root',password='123',database='Test')
	cur=conn.cursor()
	name=request.form['name']
	roll=request.form['roll']
	print(roll)
	print(name)
	cur.execute("UPDATE test set roll='{}' where name='{}'".format(roll,name))
	# Query for updating the data in test table.
	conn.commit()
	return render_template('message.html',msg="Data updated")
@app.route('/backhome')
def backhome():
	return render_template('student.html')
	# returing to the main page after updating
if __name__ == '__main__':
	app.run(debug = True)
