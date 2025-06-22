
# 🛫 A320 Flight Performance Predictor

This project applies **machine learning** to simulate and predict key flight performance metrics of the Airbus A320 aircraft. It provides an interactive application for flight engineers and aviation students to explore how parameters such as temperature, wind, slope, and weight affect takeoff performance.

---

## 🚀 Project Overview

**Goal:** Predict three important performance outputs:
- ✈️ Takeoff Distance (m)
- ⛽ Fuel Burn per 100 NM (kg)
- 📈 Climb Rate (ft/min)

Using:
- Outside Air Temperature (°C)
- Runway Slope (%)
- Headwind or Tailwind (kt)
- Aircraft Weight (kg)

---

## 📁 Files

| File | Description |
|------|-------------|
| `a320_analysis.py` | Trains and saves 3 Linear Regression models |
| `a320_app.py` | Streamlit web app for making predictions |
| `A320_data.xlsx` | Synthetic dataset of 200 rows for A320 flight scenarios |
| `*.joblib` | Saved machine learning models |
| `README.md` | Project documentation (this file) |

---

## 🧠 Machine Learning Models

All models are trained using **Linear Regression** via scikit-learn.

- **Takeoff Model:** `Takeoff Distance = f(OAT, Slope, Wind, Weight)`
- **Fuel Burn Model:** `Fuel Burn = f(OAT, Slope, Wind, Weight)`
- **Climb Rate Model:** `Climb Rate = f(OAT, Slope, Wind, Weight)`

Models are saved using `joblib` for use in the Streamlit app.

---

## 🖥️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2: (Optional) Retrain models
```bash
python a320_analysis.py
```

### Step 3: Run the web app
```bash
streamlit run a320_app.py
```

---



## ✅ Future Improvements

- Add charts to the app
- Add more Aircraft Models to select
- Add flight safety margins and checks
- Deploy app on Streamlit Cloud or web server

---

## 📬 Contact

Developed by: **Youssef Hany**  
Aviation & Aeronautical Engineering Enthusiast  
Feel free to connect on [LinkedIn]: (https://www.linkedin.com/in/youssef-hany-2302b52a0/)

