from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('/index.html', author=author, name=name)

@app.route('/retirement', methods = ['POST'])
def retirement():
    current_age = int(request.form['c_age'])
    annual_salary = int(request.form['a_salary'])
    savings_goal = int(request.form['s_goal'])
    percentage_saved = int(request.form['p_saved'])

    # Calculate Answer
    s_per_year = (annual_salary * percentage_saved ) * 1.35
    years_goal = savings_goal / s_per_year
    age_met = current_age + years_goal
    age_met = round(age_met)

    if age_met < 100:
        r_answer = "Savings age goal will be: " + format(age_met)
    else:
        r_answer = "Saving age exceeds 100 years of age..."

    return render_template('/index.html', r_answer = r_answer)
    


@app.route('/bmi', methods = ['POST'])
def bmi():
    feet_inches = request.form['f_inches'].split()
    total_inches = int(feet_inches[0]) * 12 + int(feet_inches[1])
    meters = (total_inches * 0.025) * (total_inches * 0.025)
    kilograms = float(request.form['c_weight']) * 0.45
    actual_BMI = round(kilograms/meters)

    # Correctly state classification of BMI
    if actual_BMI <= 18.5:
        b_answer = "You are classified as: Underweight " + format(actual_BMI)
    elif actual_BMI > 18.5 and actual_BMI < 24.9:
        b_answer = "You are classified as: Normal Weight " + format(actual_BMI)
    elif actual_BMI > 25 and actual_BMI < 29.9:
        b_answer = "You are classified as: Overweight " + format(actual_BMI)
    elif actual_BMI > 30:
        b_answer = "You are classified as: Obese " + format(actual_BMI) 

    return render_template('/index.html', b_answer = b_answer)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
