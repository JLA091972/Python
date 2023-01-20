
# import the class
from flask_app import app, render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#create new ninjas route
@app.route("/ninjas/new")
def newninja():
    return render_template("newninja.html", dojos=Dojo.get_all())

@app.route("/ninjas/create", methods=["POST"])
def createnewninja():
    print(request.form)
    Ninja.create_new_ninja(request.form)
    return redirect('/')
