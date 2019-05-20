from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'


temp11 = ""
@app.route('/', methods=['GET', 'POST'])

def calculator():
    
    if request.method == 'GET':
        return render_template('calc_bkup.html')

    elif request.method == 'POST': 
        global temp11
        if "one" in request.form:
            temp11 = request.form['name']
            result = temp11 + "1" 
        elif "two" in request.form:
            temp11 = request.form['name'] 
            result = temp11 + "2" 
        elif "three" in request.form:
            temp11 = request.form['name']
            result = temp11 + "3"
        elif "four" in request.form:
            temp11 = request.form['name']
            result = temp11 + "4"
        elif "five" in request.form:
            temp11 = request.form['name']
            result = temp11 + "5"
        elif "six" in request.form:
            temp11 = request.form['name']
            result = temp11 + "6"
        elif "seven" in request.form:
            temp11 = request.form['name']
            result = temp11 + "7"
        elif "eight" in request.form:
            temp11 = request.form['name']
            result = temp11 + "8"
        elif "nine" in request.form:
            temp11 = request.form['name']
            result = temp11 + "9"
        elif "zero" in request.form:
            temp11 = request.form['name']
            result = temp11 + "0"
        elif "dot" in request.form:
            temp11 = request.form['name']
            result = temp11 + "."
        elif "cancel" in request.form:
            temp11 = request.form['name']
            result = ""
        elif "plus" in request.form:
            temp11 = request.form['name']
            result = temp11 + "+"
        elif "minus" in request.form:
            temp11 = request.form['name']
            result = temp11 + "-"
        elif "mul" in request.form:
            temp11 = request.form['name']
            result = temp11 + "*"
        elif "slash" in request.form:
            temp11 = request.form['name']
            result = temp11 + "/"
        elif "open" in request.form:
            temp11 = request.form['name']
            result = temp11 + "("
        elif "close" in request.form:
            temp11 = request.form['name']
            result = temp11 + ")" 
        elif "back" in request.form:
            temp11 = request.form['name']
            result = temp11[:-1]
        elif "percentile" in request.form:
            temp11 = request.form['name']
            result = temp11 + "%"
        elif "equals" in request.form:
            temp11 = request.form['name']
            if temp11[-1] == "+" or temp11[-1] == "-" or temp11[-1] == "*" or temp11[-1] == "/" or temp11[0] == "+" or temp11[0] == "-" or temp11[0] == "*" or temp11[0] == "/" or temp11[0] == "%" or temp11[-1] == "%":
                return render_template('calc_bkup2.html', result=temp11)
            else :
                result2 = eval(temp11)
                temp11 = str(result2)
                return render_template('calc_bkup.html',  result=result2)

        temp11 = result
        return render_template('calc_bkup.html',  result=result)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)