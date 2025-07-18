import streamlit as st
import pandas as pd
import joblib
from io import StringIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Student Success Predictor", layout="wide")

# --- PAGE HEADER ---
st.markdown("""
    <style>
        .main {background-color: #f5f7fa;}
        h1, h2, h3, .stMarkdown {font-family: 'Arial', sans-serif;}
        .title {color: #2c3e50;}
        .subtitle {color: #34495e;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Student Success Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='subtitle'>Predict which students may need support early</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR HELP ---
st.sidebar.title("🔧 App Guide")
st.sidebar.markdown("""
1. Download the sample CSV  
2. Upload your student data  
3. View at-risk predictions  
""")

# --- DOWNLOAD DUMMY CSV ---
dummy_csv = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "AttendanceRate": [85, 90],
    "StudyHoursPerWeek": [12, 18],
    "PreviousGrade": [70, 85],
    "ExtracurricularActivities": [1, 2],
    "ParentalSupport": ["High", "Medium"]
})

csv_buffer = StringIO()
dummy_csv.to_csv(csv_buffer, index=False)
st.download_button(
    label="📥 Download Sample CSV",
    data=csv_buffer.getvalue(),
    file_name="student_sample.csv",
    mime="text/csv"
)

st.markdown("Upload a CSV with the following columns:")
st.code("Gender, AttendanceRate, StudyHoursPerWeek, PreviousGrade, ExtracurricularActivities, ParentalSupport")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required_cols = ["Gender", "AttendanceRate", "StudyHoursPerWeek", "PreviousGrade", "ExtracurricularActivities", "ParentalSupport"]
    
    if all(col in df.columns for col in required_cols):
        student_model = joblib.load("models/student_success_model.pkl")
        df_encoded = pd.get_dummies(df[required_cols], columns=["Gender", "ParentalSupport"], drop_first=True)
        predictions = student_model.predict(df_encoded)
        df["Prediction"] = predictions
        df["Prediction"] = df["Prediction"].map({1: "Not At Risk", 0: "At Risk"})

        # Summary
        st.markdown("### Prediction Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Students", len(df))
        with col2:
            st.metric("At Risk", (df["Prediction"] == "At Risk").sum())

        # Highlighted table
        def highlight_risk(row):
            return ['background-color: #f8d7da' if row["Prediction"] == "At Risk" else '' for _ in row]

        st.markdown("### Detailed Predictions")
        st.dataframe(df.style.apply(highlight_risk, axis=1))

    else:
        st.error("Your file is missing one or more required columns.")
