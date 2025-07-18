import streamlit as st
import pandas as pd
import joblib

# ===== Page Config =====
st.set_page_config(page_title="Student Success Predictor", layout="centered")

# ===== Title and Description =====
st.markdown("<h1 style='color:#2c3e50;'>Student Success Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#34495e;'>Predict which students may need support early based on key academic indicators.</h4>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("### 📄 Required Columns:")
st.markdown("""
<ul>
  <li>Gender</li>
  <li>AttendanceRate</li>
  <li>StudyHoursPerWeek</li>
  <li>PreviousGrade</li>
  <li>ExtracurricularActivities</li>
  <li>ParentalSupport</li>
</ul>
""", unsafe_allow_html=True)

# ===== File Uploader =====
uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

# ===== Prediction Logic (unchanged) =====
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required_cols = ["Gender", "AttendanceRate", "StudyHoursPerWeek", "PreviousGrade", "ExtracurricularActivities", "ParentalSupport"]

    if all(col in df.columns for col in required_cols):
        student_model = joblib.load("models/student_success_model.pkl")
        predictions = student_model.predict(df[required_cols])
        df["Prediction"] = predictions
        df["Prediction"] = df["Prediction"].map({1: "Not At Risk", 0: "At Risk"})

        st.success("✅ Predictions generated successfully!")
        st.markdown("### 🔍 Prediction Results")
        st.dataframe(df)
    else:
        st.error("Uploaded file does not contain all required columns.")
