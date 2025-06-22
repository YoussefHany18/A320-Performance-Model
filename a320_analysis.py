import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

from sklearn.metrics import mean_absolute_error

# load dataset
df =pd.read_excel("A320_data.xlsx")

# Model 1: predicting takeoff Distance f(climb rate, Fuel Burn, Headwind, weight)
x1 = df[["OAT (C)", "Runway Slope (%)", "Headwind/Tailwind (kt)", "Aircraft Weight (kg)"]]
y1 =df["Takeoff Distance (m)"]

model1 = LinearRegression().fit(x1, y1)
print("Model 1 - Takeoff Distance Prediction")
print("Intercept:", model1.intercept_)
print("Coefficients:", model1.coef_)
print("R^2 Score:", model1.score(x1,y1))



# Model 2: predicting Fuel Burn per 100 Nautical Miles

x2 =df[["OAT (C)", "Runway Slope (%)", "Headwind/Tailwind (kt)", "Aircraft Weight (kg)"]]
y2 =df["Fuel Burn per 100 NM (kg)"]

model2 = LinearRegression().fit(x2,y2)
print("\nModel 2 - Fuel Burn Prediction")
print("Intercept:", model2.intercept_)
print("Coefficients:", model2.coef_)
print("R^2 Score:", model2.score(x2,y2))

#Model 3: Predicting Climb Rate

X3 = df[["OAT (C)", "Runway Slope (%)", "Headwind/Tailwind (kt)", "Aircraft Weight (kg)"]]
y3 = df["Climb Rate (ft/min)"]

model3 = LinearRegression().fit(X3, y3)

print("\nModel 3 - Climb Rate Prediction")
print("Intercept:", model3.intercept_)
print("Coefficients:", model3.coef_)
print("R² Score:", model3.score(X3, y3))

#-------------------------------------------------------------------------------
# === Test Model 1: Takeoff Distance ===



#-----------------------------------------------------------------------------------
import joblib

# Save trained models
joblib.dump(model1, "takeoff_model.joblib")
joblib.dump(model2, "fuel_model.joblib")
joblib.dump(model3, "climb_model.joblib")

