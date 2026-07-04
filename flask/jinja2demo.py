# Building url dynamically 
# variable rule 
# jinja 2 template engine

'''
{{ }} expressions to print out in html
{%...%} conditions, for loops
{#...#} this is for comments in jinja2 template engine
'''



## variableb rule 

from flask import Flask, render_template, url_for, redirect, request

### setting up the wsgi application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to the Flask learning page, Created by Anunay Naman"

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/success/<int:score>')
def success(score):
    return f"The marks you got is " + str(score)



@app.route('/result/<int:score>')
def result(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    
    exp = {'score' : score, 'res': res}
    
    return render_template('result.html', results = exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results = score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        total_score = (science + maths + english)/3
    else: 
        return render_template('getres.html')
    return redirect(url_for('successif', score = total_score))








































if __name__ == "__main__":
    app.run(debug = True)
