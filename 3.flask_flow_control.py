# Creating our fir flask application
# 1- Jinja
# 2 - Wrkzeug
from flask import Flask
app = Flask(__name__) # global consturctor which represents our application

@app.route("/")
def welcome(): #view function
    return "welcome to our first Flask application!"

@app.route("/cool")
def cool():
    return "This is the cool page!"

if __name__ == "__main__":
    app.run(debug=True)
