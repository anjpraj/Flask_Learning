# Creating our fir flask application
# 1- Jinja
# 2 - Wrkzeug
from flask import Flask
app = Flask(__name__) # global consturctor which represents our application

@app.route("/")
def welcome(): #view function
    return "Welcome to our first Flask application!"

if __name__ == "__main__":
    app.run()
