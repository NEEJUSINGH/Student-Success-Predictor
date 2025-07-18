import streamlit as st
import pandas as pd
import joblib
import random

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


# Define columns and options
num_students = 10
genders = ['Male', 'Female']
parental_support = ['Low', 'Medium', 'High']

# Generate dummy data
data = {
    'Gender': [random.choice(genders) for _ in range(num_students)],
    'AttendanceRate': [random.randint(70, 100) for _ in range(num_students)],
    'StudyHoursPerWeek': [random.randint(5, 30) for _ in range(num_students)],
    'PreviousGrade': [random.randint(60, 100) for _ in range(num_students)],
    'ExtracurricularActivities': [random.randint(0, 3) for _ in range(num_students)],
    'ParentalSupport': [random.choice(parental_support) for _ in range(num_students)],
}
sample_data = pd.DataFrame(data)
   
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
