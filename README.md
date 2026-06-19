# Customer Churn Prediction (End-to-End ML Project with Flask)

A complete Machine Learning web application that predicts whether a customer will churn or not using Logistic Regression and Flask.

---

## 🚀 Project Overview

This project predicts customer churn based on user input data such as credit score, age, balance, salary, etc.

The system uses a trained Machine Learning model and provides real-time predictions through a Flask web application.

---

## 🎯 Problem Statement

Banks and businesses want to identify customers who are likely to leave (churn) so they can take preventive actions and improve retention.

This project solves that problem using Machine Learning.

---

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Type: Binary Classification
- Output: 
  - 1 → Customer WILL CHURN ❌  
  - 0 → Customer WILL NOT CHURN ✅

---

## 📊 Model Evaluation

The model performance was evaluated using classification metrics:

- Accuracy: 88% (approx)
- Precision: 0.86
- Recall: 0.84
- F1 Score: 0.85

### Evaluation Methods:
- Train-test split
- Confusion Matrix
- Classification Report

---

## ⚙️ Project Workflow

1. Data Collection (Banking dataset)
2. Data Preprocessing
3. Feature Encoding (Country, Gender)
4. Train-Test Split
5. Model Training (Logistic Regression)
6. Model Evaluation
7. Save Model using Joblib
8. Flask Web App Development
9. User Input → Prediction → Output Display

---

## 🧾 Input Features

- Credit Score
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card (0/1)
- Active Member (0/1)
- Estimated Salary
- Country (France / Germany / Spain)
- Gender (Male / Female)

---

## 🛠 Tech Stack

- Python 🐍
- Flask 🌐
- Scikit-learn 🤖
- NumPy 🔢
- Pandas 📊
- HTML / Css🎨
- Joblib (Model saving)

---
## 📂 Project Structure
customer-churn-project/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html

## Run Flask app
python app.py

📊 Output Example
Customer WILL CHURN ❌
Customer WILL NOT CHURN ✅



💡 Key Learnings
End-to-end Machine Learning pipeline
Data preprocessing and feature encoding
Model training and evaluation
Flask web development

<img width="606" height="891" alt="output png" src="https://github.com/user-attachments/assets/e3bfad0d-c0e6-421b-9ddb-6b96b65302a3" />



👨‍💻 Author
Arun Kumar T
Ai & Machine Learning Engineer 🚀
