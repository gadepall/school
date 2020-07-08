from flask import Flask,render_template,request
import mysql.connector as mariadb
app=Flask(__name__)
@app.route('/')
def student():
  return render_template('student.html')

@app.route ('/act', methods =['GET','POST'])
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
	  msg="Data Has Been Stored"
	  return render_template('message.html',msg=msg)
	except:
  	  return "Database connection error"
if __name__=='__main__':
  app.run(debug = True)
