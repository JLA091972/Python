from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play/<int:count>/<color>')
def index(count,color):
    return render_template("index.html",count=count,color=color)	# notice the 2 new named arguments!





if __name__=="__main__":
    app.run(debug=True)

