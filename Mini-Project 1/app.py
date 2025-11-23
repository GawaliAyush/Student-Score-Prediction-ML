from flask import Flask, render_template, request
import joblib
import pandas as pd
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Load model + scaler
model = joblib.load("models/student_model_lr.joblib")
scaler = joblib.load("models/scaler.joblib")


# -------------------------------
# CREATE DATABASE IF NOT EXISTS
# -------------------------------
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS student_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours REAL,
            sleep_hours REAL,
            social_media REAL,
            attendance INTEGER,
            mental_health INTEGER,
            exercise_freq INTEGER,
            prediction INTEGER,
            confidence REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()   # Run DB setup at startup


@app.route("/")
def home():
    return render_template("index.html", prediction=None, confidence=None, percent=0, remaining=100)


@app.route("/predict", methods=["POST"])
def predict():

    # -------------------- INPUTS --------------------
    student_name = request.form["student_name"]
    study_hours = float(request.form["study_hours"])
    sleep_hours = float(request.form["sleep_hours"])
    social_media = float(request.form["social_media"])
    attendance = int(request.form["attendance"])
    mental_health_rating = int(request.form["mental_health_rating"])
    exercise_frequency = int(request.form["exercise_frequency"])

    # Derived feature
    study_sleep_ratio = study_hours / (sleep_hours + 1e-6)

    # -------------------- DATAFRAME --------------------
    df = pd.DataFrame([{
        'study_hours_per_day': study_hours,
        'sleep_hours': sleep_hours,
        'social_media_hours': social_media,
        'attendance_percentage': attendance,
        'mental_health_rating': mental_health_rating,
        'exercise_frequency': exercise_frequency,
        'study_sleep_ratio': study_sleep_ratio
    }])

    scaled = scaler.transform(df)

    # -------------------- PREDICT --------------------
    prediction = round(model.predict(scaled)[0])
    prediction = max(0, min(prediction, 100))   # Ensure 0–100

    confidence = 100 - abs(85 - prediction)
    confidence = max(50, confidence)
    confidence = round(confidence, 2)

    percent = prediction
    remaining = 100 - prediction


    # -------------------- SAVE TO DATABASE --------------------
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
    INSERT INTO student_data
    (student_name, study_hours, sleep_hours, social_media, attendance, mental_health,
     exercise_freq, prediction, confidence, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    student_name,
    study_hours,
    sleep_hours,
    social_media,
    attendance,
    mental_health_rating,
    exercise_frequency,
    prediction,
    confidence,
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
))
    conn.commit()
    conn.close()


    # -------------------- RETURN RESULT --------------------
    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        percent=percent,
        remaining=remaining
    )


if __name__ == "__main__":
    app.run(debug=True)
