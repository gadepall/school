from flask import Flask,render_template, request
app=Flask(__name__)

@app.route('/')

def cal():
	return render_template('calculator.html')


@app.route('/',methods=['POST','GET'])
def index():
	
	if request.method =='GET':
		return render_template('calculator.html')
		
	elif request.method =='POST':
		if "one" in request.form:
			result1='1'
		if "two" in request.form:
			result1='2'
		if "three" in request.form:
			result1='3'
		if "four" in request.form:
			result1='4'
		if "five" in request.form:
			result1='5'
		if "six" in request.form:
			result1='6'
		if "seven" in request.form:
			result1='7'
		if "eight" in request.form:
			result1='8'
		if "nine" in request.form:
			result1='9'
		if "zer0" in request.form:
			result1='0'
		if "add" in request.form:
			result1='+'
		if "minus" in request.form:
			result1='-'
		if "mul" in request.form:
			result1='*'
		if "div" in request.form:
			result1='/'
		if "DoIt" in request.form:
			result1='='
		if "clear" in request.form:
			result1='C'
	result1 = request.form.get('Input')
	answer=eval(result1);
	return render_template('result.html', answer=answer)
		

if __name__ == '__main__':
	app.run(debug = True)
