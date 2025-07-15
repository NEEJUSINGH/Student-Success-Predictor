# 🎓 Student Success Predictor

> **Predicting student outcomes using early engagement data**

[![View App](https://img.shields.io/badge/Launch_App_on_Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://student-success-predictor-0123.streamlit.app/)

---

##  Project Overview

The **Student Success Predictor** is a machine learning-based web application designed to help identify students who may be at risk of underperforming in a course.

By analyzing early engagement indicators such as:
- Attendance rate  
- Study hours per week  
- Prior grades  
- Extracurricular involvement  
- Parental support  

...the model helps instructors and advisors intervene early and support at-risk students.

---

## Tech Stack

- **Python**: pandas, scikit-learn, joblib
- **Streamlit**: Web dashboard for user interaction
- **Jupyter Notebook**: For data exploration and model training
- **Git & GitHub**: Version control and deployment
- *(Optional)* Docker for containerization and cloud deployment

---

## Project Structure
```bash

Student-Success-Predictor/
│
├── README.md <-- Project overview (this file)
├── LICENSE <-- Open-source license (MIT)
├── .gitignore <-- Ignore unnecessary files
│
├── data/
│ ├── raw/ <-- Raw input data (e.g., Kaggle CSV)
│ └── processed/ <-- Cleaned data ready for modeling
│
├── notebooks/
│ └── 01_EDA_Modeling.ipynb <-- Data analysis & model training notebook
│
├── src/
│ ├── data_preprocessing.py <-- Data cleaning and feature prep
│ ├── train_model.py <-- Model training script
│ └── predict.py <-- Prediction logic
│
├── models/
│ └── student_success_model.pkl <-- Trained ML model
│
├── dashboard/
│ ├── app.py <-- Streamlit app code
│ └── requirements.txt <-- Required Python packages
│
└── docs/
└── methodology.md <-- Documentation on model + ethics

```

---

## How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/NEEJUSINGH/Student-Success-Predictor.git
cd Student-Success-Predictor
```
### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r dashboard/requirements.txt
```
### 4. Run the Streamlit app
```bash
cd dashboard
streamlit run app.py
```
### Deliverables

- Trained ML model (student_success_model.pkl)

- Interactive web dashboard (Streamlit)

- Jupyter Notebook for data exploration & training

- Sample student dataset (simulated)

- Documentation (docs/methodology.md)

### Future Improvements
Integrate real-time LMS API data (e.g., D2L Brightspace)

Build role-based dashboard views for instructors or advisors

Include more features like quiz scores, login frequency

Add intervention recommendation engine

Fully deploy via Streamlit Cloud, Docker, or Heroku

### License
This project is licensed under the MIT License.

### Live Demo

[Launch the App](https://student-success-predictor-0123.streamlit.app/)

Test the app by uploading a CSV with the following columns:

Gender, AttendanceRate, StudyHoursPerWeek, PreviousGrade, ExtracurricularActivities, ParentalSupport

