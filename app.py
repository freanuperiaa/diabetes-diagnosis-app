# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h3>Diabetes Checker</h3>
    <br/><br/>
    <p>(please go to localhost:5000/diagnose)</p>
    """

@app.route('/diagnose', methods=["POST", "GET"])
def set_values():
    if request.method == "POST":
        print(request.form['nm'])
        print(request.form['pregnancy'])
        print(request.form['glucose'])
        print(request.form['bp'])
        print(request.form['skinThickness'])
        print(request.form['insulin'])
        print(request.form['bmi'])
        print(request.form['diabetesPedigree'])
        print(request.form['age'])
        return "Hello"
    if request.method == "GET":
        return render_template('setvalues.html')


if __name__ == '__main__':
    app.run(debug=True)

