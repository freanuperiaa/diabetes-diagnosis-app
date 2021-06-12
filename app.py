# app.py

from flask import Flask, render_template, request

from logistic_reg import lr_model

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
        pregnancy = float(request.form['pregnancy'])
        glucose = float(request.form['glucose'])
        bp = float(request.form['bp'])
        skin_thickness = float(request.form['skinThickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetesPedigree'])
        age = float(request.form['age'])
        result = lr_model.predict(
            pregnancy, glucose, bp, skin_thickness, insulin, bmi,
            diabetes_pedigree, age
        )
        print(result)
        if result == [1]:
            return render_template('have-diabetes.html')
        else:
            return render_template('no-diabetes.html')
    if request.method == "GET":
        return render_template('setvalues.html')


if __name__ == '__main__':
    app.run(debug=True)

