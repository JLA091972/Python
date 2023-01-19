from flask import Flask, render_template, request, redirect, session

# import the class
from users_cr import User
app = Flask(__name__)
app.secret_key
# ! READ users from DB

@app.route("/")
def index():
    # call the get all classmethod to get all users
    # users = User.get_all()
    # print(users)
    return render_template("index.html", users=User.get_all())

# create new users route
@app.route("/users/new")
def newuser():
    return render_template("newuser.html")

@app.route("/users/create", methods=["POST"])
def createnewuser():
    print(request.form)
    User.create_new_user(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)