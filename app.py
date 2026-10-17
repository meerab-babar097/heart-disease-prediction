
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

@st.cache_resource
def load_model():
    artifact = joblib.load("heart_disease_model.pkl")
    return artifact["model"], artifact["features"]

model, features = load_model()

st.title("❤️ Heart Disease Prediction System")
st.write(
    "Enter the four required attributes to get a model prediction."
)

with st.form("prediction_form"):
    age = st.number_input(
        "Age (years)", min_value=1, max_value=120, value=45
    )

    sex = st.selectbox(
        "Sex", options=[1, 0],
        format_func=lambda x: "Male (1)" if x == 1 else "Female (0)"
    )

    cp = st.selectbox(
        "Chest Pain Type (cp)", options=[1, 2, 3, 4],
        help="Use the dataset's coded values: 1, 2, 3, or 4."
    )

    thalach = st.number_input(
        "Maximum Heart Rate Achieved (thalach)",
        min_value=50, max_value=250, value=150
    )

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame(
        [[age, sex, cp, thalach]],
        columns=features
    )

    prediction = int(model.predict(input_data)[0])

    if prediction == 1:
        st.error("Prediction: Heart disease may be present.")
    else:
        st.success("Prediction: Heart disease was not indicated.")

    st.caption(
        "This result is a machine-learning prediction, not a medical diagnosis."
    )
