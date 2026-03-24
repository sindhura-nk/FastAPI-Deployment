# 🩺 Diabetes Prediction Web App 🩺

## 📌 Project Overview

This project is an end-to-end Machine Learning web application that predicts whether a patient is likely to be **Diabetic, Non-Diabetic, or Pre-Diabetic** based on medical parameters.

The application is built using **FastAPI** and deployed as a web service, allowing users to input health data through a simple UI and receive real-time predictions.

<https://diabetes-predictor-model-deployment.onrender.com>
---

## 🎯 Objective

To develop a practical healthcare analytics solution that:

* Predicts diabetes risk using clinical data
* Demonstrates end-to-end ML workflow (data → model → deployment)
* Provides an interactive interface for users

---

## 📊 Features Used

The model uses the following input features:

* Gender
* Age
* Urea
* Creatinine (Cr)
* HbA1c
* Cholesterol
* Triglycerides (TG)
* HDL
* LDL
* VLDL
* BMI

---

## 🧠 Machine Learning Model

* Model Type: Random Forest Classifier
* Preprocessing:

  * Feature scaling / transformation using a saved preprocessor (`pre.pkl`)
* Model File: `model.pkl`

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* NumPy
* Jinja2 (HTML Templates)
* Uvicorn

---

## 🌐 Application Workflow

1. User enters medical details in the web form
2. Data is sent to FastAPI backend
3. Preprocessing is applied using saved pipeline
4. Model predicts the diabetes status
5. Result is displayed on the UI

---

## 📁 Project Structure

```
project/
│
├── main.py               # FastAPI application
├── model.pkl             # Trained ML model
├── pre.pkl               # Preprocessing pipeline
├── requirements.txt      # Dependencies
│
├── templates/
│   └── DiabetesPrediction.html
│
├── static/
│   └── style.css
```

---

## 🚀 Deployment

The application is deployed using Render and can be accessed via:

<https://diabetes-predictor-model-deployment.onrender.com>

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone <https://github.com/sindhura-nk/FastAPI-Deployment/>
cd project
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
uvicorn main:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000
```

---

## 📈 Future Enhancements

* Add prediction probability (confidence score)
* Improve UI/UX design
* Integrate database for storing predictions
* Add visualization dashboard (Power BI / Plotly)
* Deploy using Docker

---

## 💡 Key Learnings

* Built and deployed an end-to-end ML application
* Integrated machine learning model with FastAPI
* Handled real-time form data using HTML & backend
* Understood deployment workflows and production setup

---

## 👩‍💻 Author

**Sindhura Nadendla**
Data Science Consultant

---

## 📬 Contact

📧 [nk.sindhura@gmail.com](mailto:nk.sindhura@gmail.com)
