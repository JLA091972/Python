
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "sapientia et doctrina:wisdom and learning"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['post'])
def result():
    print(request.form)
    session['name'] = request.form['name']
    session['dojoloc'] = request.form['dojoloc']
    session['favlang'] = request.form['favlang']
    session['comments'] = request.form ['comments']
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('displayresult.html')

if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.  

