# Creating our fir flask application
# 1- Jinja
# 2 - Wrkzeug
from flask import Flask
app = Flask(__name__) # global consturctor which represents our application

@app.route("/")
def hello_world(): #view function
    return "Hello to our first Flask application!"

if __name__ == "__main__":
    app.run(debug=True)
