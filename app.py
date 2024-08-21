from flask import Flask, render_template, request
# fask app routing

# create simple flask application
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def welcome():
    return "<h1>welcome to the channel</h1>"

@app.route("/index", methods = ["GET"])
def index():
    return "<h2>welcome to the index page</h2>"

# variable rule

@app.route("/success/<int:score>", methods = ["GET"])
def success(score):
    return "The Person has passed and score is : "+ str(score)

@app.route("/fail/<int:score>", methods = ["GET"])
def fail(score):
    return "The Person has failed and score is : "+ str(score)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        if average_marks >= 90:
            grade = 'A+'
        elif average_marks < 90 and average_marks >= 75:
            grade = 'A'
        elif average_marks < 75 and average_marks >= 60:
            grade = 'B'
        elif average_marks < 60 and average_marks >= 50:
            grade = 'C'
        elif average_marks < 50 and average_marks >= 40:
            grade = 'D'
        elif average_marks < 40 and average_marks >= 35:
            grade = 'E'
        else:
            grade = 'F'
            

            

        return render_template('form.html', score=average_marks, grade_cat = grade)

if __name__ == "__main__":
    app.run(debug=True)

