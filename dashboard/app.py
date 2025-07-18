import streamlit as st
import pandas as pd
import joblib


# Page setup
st.set_page_config(page_title="Student Success Predictor", layout="centered")

# Header
st.title("Student Success Predictor")
st.subheader("Predict which students may need support early.")
st.markdown("---")

# Column requirements
st.markdown("#### Required CSV Columns")
st.markdown("- Gender  \n- AttendanceRate  \n- StudyHoursPerWeek  \n- PreviousGrade  \n- ExtracurricularActivities  \n- ParentalSupport")

# ===== Download Dummy CSV =====
st.markdown("---")
st.markdown("Need an example file?")
sample_data = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "AttendanceRate": [90, 85],
    "StudyHoursPerWeek": [20, 15],
    "PreviousGrade": [80, 75],
    "ExtracurricularActivities": [2, 1],
    "ParentalSupport": ["High", "Medium"]
})
csv = sample_data.to_csv(index=False).encode('utf-8')
st.download_button("Download Example CSV", csv, file_name="example_student_data.csv", mime="text/csv")

uploaded_file = st.file_uploader("Upload a CSV File", type = ["CSV"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required_cols = ["Gender", "AttendanceRate", "StudyHoursPerWeek", "PreviousGrade", "ExtracurricularActivities", "ParentalSupport"]
    if all (col in df.columns for col in required_cols):
        student_model = joblib.load("models/student_success_model.pkl")
        df_encoded = pd.get_dummies(df[required_cols], columns=["Gender", "ParentalSupport"], drop_first=True)
        predictions = student_model.predict(df_encoded)
        df["Prediction"]= predictions
        df["Prediction"]= df["Prediction"].map({1:"Not At Risk", 0:"At Risk"})
        st.write("Prediction Result")
        st.dataframe(df)
    else:
        st.error("Uploaded file does not have the required columns")
