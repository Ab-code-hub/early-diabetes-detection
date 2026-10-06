import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Early Diabetes Detection",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

model = joblib.load("random_forest_pipeline.joblib")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@600;700;800&display=swap');

.stApp {
    min-height: 100vh;
    background:
        linear-gradient(90deg, rgba(3,22,55,.94), rgba(5,35,82,.80)),
        url("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=2200&q=85");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
    font-family: 'Inter', sans-serif;
}
.block-container {max-width:1180px; padding-top:3.2rem; padding-bottom:4rem;}
header[data-testid="stHeader"] {background:transparent;}
.hero {padding:1rem 0 2.3rem; max-width:850px;}
.badge {
    display:inline-block; padding:.42rem .85rem; border:1px solid rgba(105,190,255,.45);
    border-radius:999px; background:rgba(22,137,221,.20); color:#bfe8ff;
    font-size:.78rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase;
    margin-bottom:1rem;
}
.hero h1 {
    font-family:'Manrope',sans-serif; font-size:clamp(3rem,6vw,5.6rem);
    line-height:.98; letter-spacing:-.055em; margin:0; color:white; font-weight:800;
}
.hero h1 span {color:#63c7ff;}
.hero p {margin-top:1.25rem; max-width:720px; color:rgba(235,246,255,.82); font-size:1.05rem; line-height:1.7;}
.glass {
    background:rgba(8,31,65,.63); border:1px solid rgba(180,224,255,.20);
    box-shadow:0 25px 70px rgba(0,0,0,.30); backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px); border-radius:24px;
    padding:1.55rem 1.7rem 1.7rem; margin-top:1rem;
}
.section-title {font-family:'Manrope',sans-serif; font-size:1.25rem; font-weight:800; color:white;}
.section-subtitle {color:rgba(220,238,250,.70); font-size:.9rem; margin-bottom:1.25rem;}
label,.stSelectbox label,.stNumberInput label {color:#eaf7ff !important; font-weight:600 !important;}
div[data-baseweb="select"] > div, div[data-testid="stNumberInput"] > div {
    background:rgba(255,255,255,.075) !important;
    border:1px solid rgba(190,226,250,.22) !important;
    border-radius:12px !important; color:white !important;
}
input {color:white !important;}
div[data-baseweb="select"] span {color:white !important;}
.stNumberInput button {background:rgba(255,255,255,.08) !important; color:white !important; border:none !important;}
.stButton > button {
    width:100%; border:0; border-radius:14px; min-height:3.15rem;
    background:linear-gradient(135deg,#24a9ff,#0876dc); color:white;
    font-family:'Manrope',sans-serif; font-weight:800; font-size:1rem;
    box-shadow:0 12px 30px rgba(0,130,235,.28);
}
.result {
    margin-top:1.4rem; padding:1.4rem 1.5rem; border-radius:18px;
    background:rgba(255,255,255,.075); border:1px solid rgba(255,255,255,.15);
}
.result-title {color:#9edfff; font-size:.8rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase;}
.result-value {color:white; font-family:'Manrope',sans-serif; font-size:2rem; font-weight:800; margin-top:.25rem;}
.probability {color:rgba(232,245,255,.78); margin-top:.35rem;}
.footer-note {text-align:center; color:rgba(220,238,250,.58); font-size:.76rem; margin-top:1.8rem;}
div[data-testid="stAlert"] {border-radius:14px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="badge">Supervised Learning Diabetes Screening</div>
  <h1>Early Diabetes<br><span>Detection</span></h1>
  <p>A supervised-learning system designed to estimate diabetes risk from selected
  patient health information. Enter the required details below to generate a prediction.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">
<div class="section-title">Patient Information</div>
<div class="section-subtitle">Complete all fields before generating a prediction.</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male", "Other"], index=None, placeholder="Select gender")
    age = st.number_input("Age", min_value=1.0, max_value=120.0, value=None, placeholder="Enter age")
    hypertension = st.selectbox("Hypertension", [0, 1], index=None,
        placeholder="Select hypertension status", format_func=lambda x: "No" if x == 0 else "Yes")
    heart_disease = st.selectbox("Heart Disease", [0, 1], index=None,
        placeholder="Select heart disease status", format_func=lambda x: "No" if x == 0 else "Yes")

with col2:
    smoking_history = st.selectbox("Smoking History",
        ["never", "current", "former", "No Info", "ever", "not current"],
        index=None, placeholder="Select smoking history")
        bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=95.7,
    value=None,
    step=0.1,
    placeholder="Enter BMI"
)

HbA1c_level = st.number_input(
    "HbA1c Level",
    min_value=3.5,
    max_value=9.0,
    value=None,
    step=0.1,
    placeholder="Enter HbA1c level"
)

blood_glucose_level = st.number_input(
    "Blood Glucose Level",
    min_value=80.0,
    max_value=300.0,
    value=None,
    step=1.0,
    placeholder="Enter blood glucose level"
)
st.markdown("<br>", unsafe_allow_html=True)
predict = st.button("🔍  Predict Diabetes")
st.markdown("</div>", unsafe_allow_html=True)

if predict:
    fields = {
        "Gender": gender, "Age": age, "Hypertension": hypertension,
        "Heart Disease": heart_disease, "Smoking History": smoking_history,
        "BMI": bmi, "HbA1c Level": HbA1c_level, "Blood Glucose Level": blood_glucose_level
    }
    missing = [name for name, value in fields.items() if value is None]

    if missing:
        st.warning("Please complete the following field(s): " + ", ".join(missing))
    else:
        patient = pd.DataFrame([{
            "gender": gender, "age": age, "hypertension": hypertension,
            "heart_disease": heart_disease, "smoking_history": smoking_history,
            "bmi": bmi, "HbA1c_level": HbA1c_level,
            "blood_glucose_level": blood_glucose_level
        }])

        prediction = model.predict(patient)[0]
        probability = model.predict_proba(patient)[0][1]
        result = "Diabetes" if prediction == 1 else "No Diabetes"

        st.markdown(f"""
        <div class="result">
          <div class="result-title">Prediction Result</div>
          <div class="result-value">{result}</div>
          <div class="probability">Estimated probability of diabetes:
            <strong>{probability:.2%}</strong></div>
        </div>
        """, unsafe_allow_html=True)

        st.info("Academic project prototype only. This prediction is not a medical diagnosis "
                "and should not replace professional medical advice.")

st.markdown('<div class="footer-note">Early Diabetes Detection Using Supervised Learning • Academic Project</div>',
            unsafe_allow_html=True)
