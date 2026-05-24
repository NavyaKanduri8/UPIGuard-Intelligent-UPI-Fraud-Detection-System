# 💳 UPI Fraud Detection System

## 📌 Overview
This project detects fraudulent UPI transactions using Machine Learning.

---

## 🛠 Technologies Used
- Python
- Flask
- MySQL
- Scikit-learn
- Bootstrap
- Logistic Regression

---

## ✨ Features
- User & Admin Login
- Fraud Detection
- Risk Analysis
- Transaction History
- Fraud Analytics Dashboard
- Payment Blocking

---

## 📂 Modules
- User Authentication Module
- Fraud Detection Module
- Risk Evaluation Module
- Transaction History Module
- Admin Dashboard Module
- Database Management Module

---

## 🤖 Machine Learning Algorithm

### Logistic Regression
The project uses Logistic Regression for fraud prediction.

It classifies transactions as:
- Fraud
- Safe

based on transaction probability.

---

## 📚 Python Libraries Used
- pandas
- numpy
- flask
- scikit-learn
- matplotlib
- seaborn
- mysql-connector-python
- joblib

---

## 🏗 System Architecture
The system contains:
1. User Interface
2. Flask Backend
3. Machine Learning Model
4. MySQL Database
5. Admin Dashboard
6. Fraud Detection Engine

---

## 🔄 Flow of Project
1. User enters transaction details
2. Flask backend receives data
3. Features are processed
4. Logistic Regression predicts fraud probability
5. System classifies transaction
6. Fraudulent transactions are blocked
7. Results stored in MySQL database
8. Admin dashboard displays analytics

---

## 📊 Dataset
Credit Card Fraud Detection Dataset

Source:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## 🚀 Future Enhancements
- Deep Learning Integration
- Real-time Fraud Alerts
- OTP Verification
- SMS & Email Notifications
- AI-based Behavioral Analysis

---



---
## 📂 Project Structure

```bash
UPIGuard-Intelligent-UPI-Fraud-Detection-System/
│
├── app.py
├── model.py
├── eda.py
├── fraud_model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── creditcard.csv
│
├── templates/
│   ├── admin_dashboard.html
│   ├── history.html
│   ├── login.html
│   ├── result.html
│   ├── user_check.html
│   └── user_dashboard.html
│
└── screenshots/
    ├── login.png
    ├── user_dashboard.png
    ├── admin_dashboard.png
    ├── result.png
    ├── flowchart.png
    └── architecture.png
```

## ▶ How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## ✅ Conclusion
This project successfully detects suspicious UPI transactions using Machine Learning and helps improve digital payment security.
