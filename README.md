💳 UPIGuard: Intelligent UPI Fraud Detection System
📌 Project Overview

UPIGuard is an AI-powered UPI Fraud Detection System developed using Machine Learning, Flask, MySQL, Bootstrap, and Chart.js.
The system detects fraudulent UPI transactions in real time by analyzing transaction patterns, probability scores, suspicious UPI IDs, and transaction amounts.

The project provides:

Secure Login Authentication
User Dashboard
Fraud Detection Engine
Risk Classification
Fraud Analytics Dashboard
Fraud Trend Visualization
Transaction History
Automatic User Blocking

This project was developed as a Major Project for B.Tech Information Technology.

🚀 Features

✅ Real-time UPI fraud detection
✅ Machine Learning based prediction
✅ Logistic Regression model
✅ Rule-based fraud analysis
✅ Risk level classification
✅ Fraud analytics dashboard
✅ Fraud trend graph visualization
✅ Transaction history monitoring
✅ Automatic account blocking after repeated fraud attempts
✅ Admin and User role management
✅ Responsive Bootstrap UI

🛠️ Technologies Used
Frontend
HTML
CSS
Bootstrap 5
Chart.js
Backend
Python
Flask
Machine Learning
Scikit-learn
Logistic Regression
Pandas
NumPy
Database
MySQL
Visualization
Matplotlib
Seaborn
📂 Project Structure

UPI-Fraud-Detection-System/
│
├── templates/
│ ├── admin_dashboard.html
│ ├── history.html
│ ├── login.html
│ ├── result.html
│ ├── user_check.html
│ └── user_dashboard.html
│
├── data/
│ └── creditcard.csv
│
├── screenshots/
│ ├── login.png
│ ├── dashboard.png
│ ├── fraud_detected.png
│ ├── safe_transaction.png
│ ├── history.png
│ ├── admin_dashboard.png
│ ├── graph.png
│ ├── blocked.png
│ ├── database.png
│ └── ml_results.png
│
├── app.py
├── model.py
├── eda.py
├── fraud_model.pkl
├── requirements.txt
└── README.md

⚙️ Installation Steps
1️⃣ Clone Repository

git clone https://github.com/yourusername/UPIGuard-AI-Fraud-Detection-System.git

cd UPIGuard-AI-Fraud-Detection-System

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Setup MySQL Database

Create database:

CREATE DATABASE fraud_detection;

Create table:

CREATE TABLE user_transactions (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100),
time BIGINT,
amount FLOAT,
probability FLOAT,
prediction VARCHAR(20)
);

4️⃣ Run Application

python app.py

🔐 Login Credentials
Admin

Username: admin
Password: admin123

User

Username: user
Password: user123

🧠 Machine Learning Model

The project uses Logistic Regression for fraud classification.

Algorithms Used
Logistic Regression
StandardScaler
Stratified Sampling
Probability Thresholding
Rule-Based Detection
📊 Fraud Detection Logic
Suspicious UPI ID Detection

suspicious_ids = ["fraud@upi", "scam@upi", "unknown@upi"]

If receiver in suspicious_ids:
probability = 0.95
prediction = 1

High Amount Fraud Rule

elif amount > 50000 and probability > 0.7:
prediction = 1

📈 Risk Classification

if probability < 0.3:
risk = "Low Risk"
elif probability < 0.7:
risk = "Medium Risk"
else:
risk = "High Risk"

🚫 Account Blocking Logic

if fraud_attempts >= 5:
payment_status = "Account Blocked 🚫"

📸 Screenshots
🔑 Login Page






👤 User Dashboard

Dashboard for secure UPI payments.




💸 UPI Payment Interface

Real-time UPI transaction verification interface.




✅ Safe Transaction

Successful legitimate transaction verification.




⚠️ Fraud Detected

Fraudulent UPI transaction detected using ML and rule-based analysis.




📜 Transaction History

User transaction history with fraud probability analysis.




📊 Admin Dashboard

Admin analytics dashboard for fraud monitoring and visualization.




📈 Fraud Trend Graph

Fraud trend analysis using Chart.js.




🚫 Account Blocking

Automatic user blocking after repeated fraud attempts.




🗄️ Database Records

MySQL database storing transaction records and fraud results.




🤖 Machine Learning Results

Confusion Matrix, ROC Curve, and Classification Report.




🏗️ System Architecture

The system follows a layered architecture:

User Interface Layer
Authentication Layer
Fraud Detection Layer
Machine Learning Layer
Database Layer
Analytics & Visualization Layer
📌 Modules
1. User Interface Module

Provides interaction for admin and users.

2. Authentication Module

Handles login/logout and role-based access.

3. Data Input Handling Module

Collects transaction details.

4. Feature Preparation Module

Converts transaction data into model features.

5. Data Preprocessing Module

Normalizes and scales input data.

6. Fraud Detection Module

Uses Logistic Regression for fraud prediction.

7. Rule-Based Detection Module

Detects suspicious UPI IDs and large transactions.

8. Risk Analysis Module

Classifies transactions into risk levels.

9. Transaction Storage Module

Stores transaction details in MySQL.

10. Fraud Monitoring Module

Analyzes fraud statistics for admin dashboard.

11. Visualization Module

Displays fraud trends using Chart.js.

12. Security & Blocking Module

Blocks users after repeated fraud attempts.

13. History Module

Displays transaction history.

📚 Future Scope
Deep Learning Integration
XGBoost and Random Forest Models
Real-Time Banking Integration
OTP Verification
Biometric Authentication
Cloud Deployment
AI Behavioral Analysis
📖 References
Scikit-learn Documentation
Flask Documentation
Bootstrap Documentation
Chart.js Documentation
MySQL Documentation
👩‍💻 Contributors
K Navya
G Sadhika
N Sahithi

Department of Information Technology
Bhoj Reddy Engineering College for Women
