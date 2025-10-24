import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------------------------------------
# 🌟 Page Setup
# -------------------------------------------------------------
st.set_page_config(
    page_title="🔥 Calories Burnt Prediction System",
    page_icon="💪",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------
# 💅 Custom CSS Styling
# -------------------------------------------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 25px 50px;
        border-radius: 20px;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.1);
    }
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(90deg, #ff4b4b, #ffb347);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }
    .subtitle {
        text-align: center;
        color: #333333;
        font-size: 20px;
        font-weight: 500;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4b4b, #ffb347);
        color: white;
        border: none;
        padding: 12px 40px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff6f6f, #ffd27f);
        transform: scale(1.08);
        box-shadow: 0px 4px 15px rgba(255, 100, 100, 0.4);
    }
    .footer {
        text-align: center;
        color: #555;
        margin-top: 50px;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 🧠 Load Trained Model
# -------------------------------------------------------------
try:
    RandomForest = pickle.load(open('RandomForest.pkl', 'rb'))
except FileNotFoundError:
    st.error("❌ Model file 'RandomForest.pkl' not found! Please ensure it’s in the same folder as app.py.")
    st.stop()

# -------------------------------------------------------------
# 🏋️ Title & Subtitle
# -------------------------------------------------------------
st.markdown('<div class="title">🔥 Calories Burnt Prediction System 🔥</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict your calorie burn rate based on your exercise details 💪</div>', unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 🧍 User Inputs
# -------------------------------------------------------------
st.header("📋 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Select Gender", ("Male", "Female"))
    age = st.number_input("Age (Years)", min_value=10, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

with col2:
    weight = st.number_input("Weight (kg)", min_value=30, max_value=150, value=65)
    duration = st.number_input("Exercise Duration (minutes)", min_value=5, max_value=120, value=30)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=60, max_value=200, value=100)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0, value=38.0)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 🔮 Prediction
# -------------------------------------------------------------
if st.button("💥 Predict Calories Burnt"):
    gender = 1 if gender == "Male" else 0
    features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

    prediction = RandomForest.predict(features)[0]
    st.success(f"🔥 You are estimated to burn **{prediction:.2f} Calories!** Keep going strong 💪")
    st.balloons()

# -------------------------------------------------------------
# 🌻 Footer
# -------------------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="footer">
        Developed with ❤️ using <b>Machine Learning & Streamlit</b><br>
        <i>© 2025 Calories Burnt Predictor | Stay Fit 🔥</i>
    </div>
""", unsafe_allow_html=True)
