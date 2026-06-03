# 💰 Salary Prediction App

A sleek, interactive web application built with **Streamlit** that predicts a professional's salary based on their work experience, interview score, and age. The underlying machine learning model was developed and trained in a Jupyter Notebook before being deployed as a web service.

<img width="1911" height="866" alt="Screenshot 2026-06-03 120613" src="https://github.com/user-attachments/assets/a7eec416-8883-4d4a-b957-85b19bc35175" />



---

## 🚀 Features

* **Interactive UI:** Seamless input selection using Streamlit sliders for Experience, Interview Score, and Age.
* **Instant Predictions:** Real-time salary estimation at the click of a button.
* **Machine Learning Backed:** Uses a regression model trained on historical salary data to deliver accurate predictions.

---

## 🛠️ Tech Stack

* **Frontend/Web Framework:** Streamlit
* **Model Development:** Jupyter Notebook, Python
* **Data Science & ML Libraries:** Scikit-Learn, Pandas, NumPy
* **Code Editor:** VS Code

---

## 📁 Repository Structure

```text
├── notebook/
│   └── salary_prediction.ipynb   # Jupyter Notebook containing EDA and Model Training
├── app.py                         # Streamlit application main script
├── model.pkl                      # Trained serialized machine learning model (or .pkl file)
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
