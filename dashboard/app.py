<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib


st.title("🎓 Student Success Predictor")
st.subheader("Predict which students may need support early.")
st.markdown("🚀 Under development.")

uploaded_file = st.file_uploader("Upload a CSV File", type = ["CSV"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required_cols = ["Gender", "AttendanceRate", "StudyHoursPerWeek", "PreviousGrade", "ExtracurricularActivities", "ParentalSupport"]
    if all (col in df.columns for col in required_cols):
        student_model = joblib.load("../models/student_success_model.pkl")
        df_encoded = pd.get_dummies(df[required_cols], columns=["Gender", "ParentalSupport"], drop_first=True)
        predictions = student_model.predict(df_encoded)
        df["Prediction"]= predictions
        df["Prediction"]= df["Prediction"].map({1:"Not At Risk", 0:"At Risk"})
        st.write("Prediction Result")
        st.dataframe(df)
    else:
        st.error("Uploaded file does not have the required columns")
=======
import streamlit as st

# Set up the main title
st.title("Student Success Predictor")

# Add a subtitle
st.subheader("Predict which students may need support early, using engagement data.")

# Add a simple introductory message
st.markdown("""
Welcome to the Student Success Predictor!

- Upload your student engagement data (coming soon).
- Get risk predictions based on early behaviors.
- Help advisors and instructors intervene in time.

This project is currently under development. Stay tuned!
""")

# Footer
st.markdown("---")
st.caption("Developed by Neeju Singh | Powered by Python and Streamlit")
>>>>>>> 4dc8ad53412ffae07005a14ef57f9b985c264b36
