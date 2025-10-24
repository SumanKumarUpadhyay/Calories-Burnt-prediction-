💥 Calories Burnt Prediction System 💪

🧠 “Know your burn, track your progress, and stay fit — powered by Machine Learning.”

A modern, AI-driven web app that predicts Calories Burnt during workouts based on personal details and exercise metrics.
Built using Streamlit, Scikit-learn, and Python, this project combines elegant design 🎨 with powerful ML intelligence ⚙️.

🌈 ✨ Project Highlights

🎯 Predicts the number of calories burnt instantly

🧍 Gender-based personalized prediction

⚡ Built using Random Forest Regressor

💻 Interactive Streamlit front-end

🎨 Gradient UI with glowing buttons & smooth transitions

🎈 Balloon animation and success visuals

📊 Real-world fitness dataset integration

🧠 Tech Stack
🧩 Component	💻 Technology Used
Language	Python 3 🐍
ML Framework	Scikit-learn
Frontend	Streamlit 🌐
Data Handling	Pandas, NumPy
Model Storage	Pickle
UI Styling	HTML + CSS (inline custom)
📂 Dataset Overview

The project uses two CSV datasets:

🧾 calories.csv – contains calories burnt data

🏋️ exercise.csv – includes physical & workout information

After merging on the User_ID column, the dataset contains:

Column	Description
Gender	Male / Female (encoded as 1 / 0)
Age	Age of individual
Height	Height in cm
Weight	Weight in kg
Duration	Exercise duration (minutes)
Heart Rate	Average heart rate (bpm)
Body Temp	Body temperature (°C)
Calories	Target variable (calories burnt)



⚙️ How It Works

🧹 Data Preprocessing

Merging datasets

Encoding gender

Handling nulls and scaling data


🧮 Model Training

Algorithm: RandomForestRegressor

Model evaluation using R² score & MAE

💾 Model Deployment

Model saved as RandomForest.pkl

Integrated with a Streamlit app for real-time prediction


🎨 UI & Design Highlights
Feature	Description
🏠 Homepage	Gradient Title “🔥 Calories Burnt Prediction System”
🧾 Input Form	Card-style input box with soft shadows
🎨 Buttons	Orange-red glowing gradient buttons
🎈 Animation	Balloons on successful prediction
💬 Footer	Clean gradient footer with developer credits

✨ The interface feels like a modern fitness dashboard, not just a plain ML app!

🧩 Code Snippet (Model Loading)
# Load Model
import pickle
RandomForest = pickle.load(open('RandomForest.pkl', 'rb'))

# Predict
features = [[gender, age, height, weight, duration, heart_rate, body_temp]]
prediction = RandomForest.predict(features)[0]

🚀 How to Run Locally
🧰 Step 1: Clone Repository
git clone https://github.com/yourusername/calories-burnt-prediction.git
cd calories-burnt-prediction

🧱 Step 2: Install Dependencies
pip install -r requirements.txt

🧠 Step 3: Run App
streamlit run app.py

🧾 Requirements.txt
streamlit
pandas
numpy
scikit-learn
pickle-mixin

📊 Model Performance
Metric	Score
R² Score	0.96
Mean Absolute Error (MAE)	12.4

✅ Highly accurate predictions for calorie estimation.

🖼️ App Preview (Demo)
🪄 Input Page	⚡ Prediction Result

	

“🔥 You are estimated to burn 230.45 Calories! Keep going strong 💪”

👨‍💻 Developer Info
🧑 Name	Suman Kumar
🎓 Field	Computer Science & Engineering
💼 Project	Machine Learning — Calories Burnt Predictor
🏛️ Workshop	IIT Bhilai — Data Preprocessing & Kaggle ML
💬 Motto	Learn. Build. Inspire.
🌱 Future Enhancements

🩺 Add activity type (Running, Yoga, Cycling, etc.)

📱 Mobile-responsive layout

☁️ Cloud deployment (Streamlit Cloud / Hugging Face)

🧾 User progress tracking dashboard

🧬 AI-based nutrition suggestion system

❤️ Acknowledgements

Special thanks to:

Streamlit team for easy UI deployment

Scikit-learn for robust ML tools

Kaggle for open datasets

