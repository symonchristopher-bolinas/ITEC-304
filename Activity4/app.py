from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2(): 
    return render_template('index2.html')

@app.route('/activity1')
def activity1(): 
    return render_template('activity1.html')

@app.route('/index3')
def index3(): 
    return render_template('index3.html')

@app.route('/index4')
def index4(): 
    return render_template('index4.html')

app.run(host="localhost", debug=True)
