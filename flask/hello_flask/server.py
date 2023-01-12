from flask import Flask, render_template
# from werkzeug.exceptions import HTTPException  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'hello World!' 

@app.route('/dojo')    
def dojo():
    return 'Dojo'


@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/hello/<name>/<int:count>') ## take whatever name is adding in the url: http://localhost:5000/hello/jay  <---- jay
def printx(name,count):
    print(name)
    return (f'Hi {name * count} ')

@app.route('/hello2/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello2(name):
    print(name)
    return (f'Hello, {name}')

@app.errorhandler(404)
def page_not_found(error):
    return ('Sorry! No response. Try again.')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

