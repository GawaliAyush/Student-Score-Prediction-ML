# Student-Score-Prediction-ML
Student Score Prediction System Using Machine Learning

This project predicts a student’s final exam score using Machine Learning based on their study habits, lifestyle, and academic behavior.
It includes:

✔ Machine Learning model (Linear Regression)

✔ Flask web application

✔ SQLite database integration

✔ Beautiful UI with dynamic score visualization

✔ Complete end-to-end ML pipeline

⭐ Project Features

🎯 Predict final exam score

🎯 Simple, clean, attractive UI

🎯 Dynamic circular score meter

🎯 Stores every prediction in SQLite DB

🎯 Fully explainable ML pipeline

🎯 Model + scaler saved using joblib

🎯 Flask-based deployment-ready backend

📂 Project Folder Structure
Student-Score-Prediction-ML/
│── app.py
│── requirements.txt
│── README.md
│── students.db
│
├── models/
│    ├── student_model_lr.joblib
│    ├── scaler.joblib
│
├── templates/
│    ├── index.html
│
├── static/
│    ├── style.css
│
├── data/
│    ├── student_habits_performance_clean.csv
│
└── notebooks/
     ├── data_cleaning_01.ipynb
     ├── train_model_03.ipynb
     ├── evaluation_04.ipynb

🧠 Technologies Used
🔹 Python

Core programming language

🔹 Pandas & NumPy

Data loading, cleaning, numerical operations

🔹 Scikit-Learn

Machine learning model & preprocessing
(Linear Regression + StandardScaler)

🔹 Flask

Backend web framework

🔹 HTML & CSS

Frontend UI

🔹 SQLite

Local relational database

🔹 Joblib

Model & scaler saving/loading

🔥 Machine Learning Workflow
1️⃣ Data Loading

CSV loaded using Pandas.

2️⃣ Data Cleaning

Handling missing values

Encoding categorical fields

Removing duplicates

3️⃣ Feature Engineering

Created new feature:
study_sleep_ratio = study_hours / sleep_hours

4️⃣ Train-Test Split

Used 80% for training, 20% for testing.

5️⃣ Feature Scaling

Standardized using StandardScaler.

6️⃣ Model Training

Trained a Linear Regression model due to:

Higher R² score

Lower RMSE

Simpler interpretability

7️⃣ Model Saving

Saved using joblib for Flask app integration.

🌐 Flask Web Application Workflow
🔹 Frontend → User Input

User enters:

Study hours

Sleep hours

Social media hours

Attendance

Mental health rating

Exercise frequency

🔹 Backend → Flask Processing

Receives data via POST

Builds DataFrame

Adds engineered feature

Scales data

Predicts score

Calculates confidence

🔹 Database → SQLite Logging

Each prediction is stored with timestamp.

🔹 Frontend → UI Display

Dynamic circular score indicator updates based on prediction.

🗄 SQLite Database Structure

Table: student_data

Column	Description
id	Auto-increment
student_name	Optional user input
study_hours	Hours studied per day
sleep_hours	Sleep duration
social_media	Social media usage
attendance	Attendance score
mental_health	Rating (0–10)
exercise_freq	0 = low, 1 = medium, 2 = high
prediction	Final predicted score
confidence	Model confidence
timestamp	Prediction time
▶ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Student-Score-Prediction-ML.git
cd Student-Score-Prediction-ML

2️⃣ Create Virtual Environment (optional)
conda create -n ml_env python=3.10
conda activate ml_env

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

📸 Screenshots (Add your images here)

Home page

Prediction result

Database entries

🚀 Future Enhancements

Add Random Forest & XGBoost models

Deploy on Render/Heroku/Railway

Add Admin Panel

Add Graphical Analytics Dashboard

Student Login System

🏁 Conclusion

The project demonstrates:

✔ Data Cleaning
✔ Feature Engineering
✔ Model Training
✔ Model Deployment
✔ Database Logging
✔ Attractive and functional UI

A complete end-to-end machine learning project suitable for academic submission and real-life learning.
