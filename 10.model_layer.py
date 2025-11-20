# Creating our fir flask application
# 1- Jinja
# 2 - Wrkzeug
from flask import Flask, render_template, jsonify, json, abort
from model import db, load_db
db = load_db()

app = Flask(__name__) # global consturctor which represents our application
m = "Welcome to our first Flask application!"
f = "Akaash"
l = "Sharma"
@app.route("/")
def welcome(): #view function
    return render_template("home.html", message=m, first_name=f, last_name=l) #jinja variable passing

@app.route("/")
def welcome(): #view function
    return render_template("home.html",
                            message=m,
                              first_name=f,
                                last_name=l,
                                questions = db) #jinja variable passing
@app.route("/questions/<int:index>")
def questions_view(index):
    try:    
        questions_db = db[index]
        return render_template("quiz.html",
                                index=index,
                                  question=questions_db,
                                  max_index=len(db) - 1)
    except IndexError:
        abort(404, description="Question not found")
if __name__ == "__main__":
    app.run(debug=True)
