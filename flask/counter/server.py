
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "sapientia et doctrina:wisdom and learning"


# click increase
@app.route('/')
def increase():
    # request.form['plusbox']
    if 'counter' in session:
        session["counter"] += 1
    else:
        session['counter'] = 0
    return render_template('index.html')

## increase count
@app.route('/increase2')
def increase2():
    session['counter'] +=1
    return redirect("/")


# #click reset
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)    # Run the app in debug mode.
