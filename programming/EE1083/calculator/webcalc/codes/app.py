from flask import Flask,render_template,request
import mysql.connector as mariadb
app=Flask(__name__)
@app.route('/')
def student():
  return render_template('student.html')
@app.route ('/act', methods = ['GET','POST'])
def act():
  if (request.method == 'POST'):
	try:
   	  name=request.form['name']
	  roll=request.form['roll']
	  conn=mariadb.connect(user='root',password='123',database='Test')
	  cur=conn.cursor()
	  sql="INSERT INTO test(name,roll)values('{}','{}')".format(name,roll)
	  cur.execute(sql)
	  conn.commit()
	  return render_template("output.html",msg="Data Has Been Stored")
	except:
	  return "Database connection error"
@app.route('/display')
def display():
  conn=mariadb.connect(user='root',password='123',database='Test')
  cur=conn.cursor()
  cur.execute("Select * from test")
  rows=cur.fetchall()
  return render_template("display.html",rows=rows)
@app.route('/update')
def list():
  conn=mariadb.connect(user='root',password='123',database='Test')
  cur=conn.cursor()
  cur.execute("Select * from test")
  rows=cur.fetchall()
  return render_template("show.html",rows=rows)

@app.route ('/testupdate', methods =['GET','POST'])
def testupdate():
  conn=mariadb.connect(user='root',password='123',database='Test')
  cur=conn.cursor()
  name=request.form['name']
  roll=request.form['roll']
  print(roll)
  print(name)
  cur.execute("UPDATE test set roll='{}' where name='{}'".format(roll,name))
  conn.commit()
  return render_template('student.html',msg="Data updated")
@app.route('/backhome')
def backhome():
  return render_template('student.html')

if __name__ == '__main__':
  app.run(debug = True)
