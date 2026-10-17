# Heart Disease Prediction System

## Project Overview
This project aims to develop a machine learning-based Heart Disease Prediction System using the UCI Heart Disease dataset. The system predicts whether heart disease indicators are present based on four selected patient attributes.

This project is part of Task 2 of the Structured Data Machine Learning Assignment.

## Dataset
- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Selected dataset:** Processed Cleveland dataset
- **Input features:** 4
- **Target variable:** `num`

The original target variable is converted into a binary classification:
- `0` — No heart disease indicated
- `1` — Heart disease indicated

## Selected Input Features
1. `age` — Age of the patient
2. `sex` — Sex code
3. `cp` — Chest pain type
4. `thalach` — Maximum heart rate achieved

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Machine Learning Workflow
1. Load and inspect the dataset.
2. Handle missing values and prepare the selected features.
3. Split the dataset into training and testing sets.
4. Train a Logistic Regression model.
5. Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
6. Save the trained model.
7. Build an interactive Streamlit application.
8. Deploy the application to the cloud.

## Project Files
- `Heart_Disease_Prediction.ipynb` — Data preparation, model training, and evaluation.
- `processed.cleveland.data` — Selected Cleveland dataset.
- `app.py` — Streamlit prediction application.
- `requirements.txt` — Required Python libraries.
- `heart_disease_model.pkl` — Saved trained machine learning model.

## Deployment

**Live Application:** https://heart-disease-prediction-9kkj3m5yhybso8dfbp3t7u.streamlit.app/

## Disclaimer
This project is intended for educational purposes only. Its predictions are not a medical diagnosis and must not be used as a substitute for professional medical advice.
