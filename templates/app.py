from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import joblib
import numpy as np
import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="fraud_detection"
)

cursor = db.cursor()

# Flask App
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load ML Model
model = joblib.load("fraud_model.pkl")

# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Admin Login
        if username == "admin" and password == "admin123":

            session["role"] = "admin"
            session["username"] = username

            return redirect(url_for("home"))

        # User Login
        elif username == "user" and password == "user123":

            session["role"] = "user"
            session["username"] = username

            return redirect(url_for("home"))

        else:
            return "Invalid Credentials"

    return render_template("login.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- HOME ---------------- #

@app.route("/")
def home():

    if "role" not in session:
        return redirect(url_for("login"))

    # ---------- ADMIN DASHBOARD ---------- #

    if session["role"] == "admin":

        # Total Transactions
        cursor.execute("SELECT COUNT(*) FROM user_transactions")
        total = cursor.fetchone()[0]

        # Fraud Transactions
        cursor.execute("""
            SELECT COUNT(*)
            FROM user_transactions
            WHERE prediction='Fraud'
        """)

        fraud_count = cursor.fetchone()[0]

        # Fraud Percentage
        if total > 0:
            fraud_percent = round((fraud_count / total) * 100, 2)
        else:
            fraud_percent = 0

        # Recent Transactions
        cursor.execute("""
            SELECT username, time, amount, probability, prediction
            FROM user_transactions
            ORDER BY id DESC
            LIMIT 10
        """)

        recent_transactions = cursor.fetchall()

        # Fraud Trend
        cursor.execute("""
            SELECT DATE(FROM_UNIXTIME(time)) as day,
            SUM(CASE WHEN prediction='Fraud' THEN 1 ELSE 0 END) as frauds
            FROM user_transactions
            GROUP BY day
            ORDER BY day DESC
            LIMIT 7
        """)

        trend_data = cursor.fetchall()

        trend_data = trend_data[::-1]

        dates = [str(row[0]) for row in trend_data]
        frauds = [row[1] for row in trend_data]

        return render_template(
            "admin_dashboard.html",
            total=total,
            fraud_count=fraud_count,
            fraud_percent=fraud_percent,
            recent_transactions=recent_transactions,
            dates=dates,
            frauds=frauds
        )

    # ---------- USER DASHBOARD ---------- #

    return render_template("user_dashboard.html")


# ---------------- CHECK TRANSACTION ---------------- #

@app.route("/check", methods=["GET", "POST"])
def check_transaction():

    if "role" not in session or session["role"] != "user":
        return redirect(url_for("login"))

    if request.method == "POST":

        import time as t

        receiver = request.form["receiver"]
        amount = float(request.form["amount"])

        # Generate Features
        time_value = int(t.time())

        features = np.zeros((1, 30))

        features[0][0] = time_value
        features[0][-1] = amount

        # Suspicious UPI IDs
        suspicious_ids = [
            "fraud@upi",
            "scam@upi",
            "unknown@upi"
        ]

        # Prediction
        if receiver in suspicious_ids:

            probability = 0.95
            prediction = 1

        else:

            probability = model.predict_proba(features)[0][1]

            if probability >= 0.8:
                prediction = 1
            else:
                prediction = 0

        # Risk Level
        if probability < 0.3:
            risk = "Low Risk"

        elif probability < 0.7:
            risk = "Medium Risk"

        else:
            risk = "High Risk"

        # Status
        if prediction == 1:
            status = "Fraud"
        else:
            status = "Safe"

        # Save to Database
        sql = """
        INSERT INTO user_transactions
        (username, time, amount, probability, prediction)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            session["username"],
            time_value,
            amount,
            probability,
            status
        )

        cursor.execute(sql, values)

        db.commit()

        return render_template(
            "result.html",
            prediction=prediction,
            probability=probability,
            risk=risk
        )

    return render_template("user_check.html")


# ---------------- HISTORY ---------------- #

@app.route("/history")
def history():

    if "role" not in session:
        return redirect(url_for("login"))

    sql = """
    SELECT time, amount, probability, prediction
    FROM user_transactions
    WHERE username=%s
    """

    cursor.execute(sql, (session["username"],))

    records = cursor.fetchall()

    from datetime import datetime

    formatted_records = []

    for row in records:

        formatted_time = datetime.fromtimestamp(
            row[0]
        ).strftime('%d-%m-%Y %I:%M %p')

        formatted_records.append(
            (
                formatted_time,
                row[1],
                row[2],
                row[3]
            )
        )

    return render_template(
        "history.html",
        records=formatted_records
    )


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":

    app.run(debug=True)
