
# import the class
from flask_app import app, render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# ! READ dojos from DB
@app.route("/")
def index():
    #call the get all classmethod to get all dojos
    # dojos = Dojo.get_all()
    # print(dojos)
    return redirect('/dojos')   #render_template("index.html", dojos=Dojo.get_all())

# create new dojos route
@app.route("/dojos")
def newdojo():
    return render_template("index.html", dojos=Dojo.get_all())

@app.route("/dojos/create", methods=["POST"])
def createnewdojo():
    print(request.form)
    Dojo.create_new_dojo(request.form)
    return redirect('/')

# read 1 dojo
@app.route("/dojos/<int:id>")
def getonedojo(id):
    data = {'id':id}
    return render_template('showdojo.html',dojo = Dojo.get_dojo_ninjas(data) )

