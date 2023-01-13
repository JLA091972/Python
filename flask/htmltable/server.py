
# Import Flask to allow us to create our app
from flask import Flask, render_template
from users import users

app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    return render_template("index.html", users = users)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
