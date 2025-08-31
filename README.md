# Diabetes Prediction App
A Machine Learning web application that predicts whether a person is likely to have diabetes or not based on medical input parameters.

# Project Overview
- Built a Random Forest Classifier to predict diabetes.
- Achieved high accuracy by testing multiple models.
- Deployed using Streamlit Cloud for live demo access.
- End-to-end workflow: Data preprocessing → Model training → Evaluation → Deployment.

# Dataset
Source: Diabetes Dataset
Features include: Glucose, BMI, Age
Target: Outcome (0 = Non-Diabetic, 1 = Diabetic)

# Tech Stack
Python
Pandas, NumPy for data analysis
Scikit-learn for machine learning
Joblib for model serialization
Streamlit for deployment

# Model Training
Tried Logistic Regression, Lasso Regression, Random Forest
Selected Random Forest Classifier as it gave the best accuracy
Accuracy achieved: ~76% 

# Live Demo

https://diabetes-prediction-app-kguvgkopqzt93urkupwtah.streamlit.app/

# How to Run Locally

1. Clone the repository:
git clone https://github.com/ashwanikumar-28/diabetes-prediction-app.git
cd diabetes-prediction-app

2. Install dependencies:
pip install requirements.txt

      
