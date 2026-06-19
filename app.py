from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# load trained model
model = joblib.load("churn_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # numeric inputs
    credit_score = int(request.form["credit_score"])
    age = int(request.form["age"])
    tenure = int(request.form["tenure"])
    balance = float(request.form["balance"])
    products_number = int(request.form["products_number"])
    credit_card = int(request.form["credit_card"])
    active_member = int(request.form["active_member"])
    estimated_salary = float(request.form["estimated_salary"])

    # categorical inputs
    country = request.form["country"]
    gender = request.form["gender"]

    # encoding
    country_germany = 1 if country == "Germany" else 0
    country_spain = 1 if country == "Spain" else 0
    gender_male = 1 if gender == "Male" else 0

    # final input array (11 features)
    input_data = np.array([[
        credit_score,
        age,
        tenure,
        balance,
        products_number,
        credit_card,
        active_member,
        estimated_salary,
        country_germany,
        country_spain,
        gender_male
    ]])

    # prediction
    prediction = model.predict(input_data)[0]

    # result
    result = "Customer WILL CHURN ❌" if prediction == 1 else "Customer WILL NOT CHURN ✅"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)