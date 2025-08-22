from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_age(birthdate):
    today = datetime.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    if age_days < 0:
        age_months -= 1
        age_days += 30
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        dob_str = request.form["dob"]
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        age = calculate_age(dob)
    return render_template("index.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
