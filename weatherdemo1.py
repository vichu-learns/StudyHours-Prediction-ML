import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Prepare Data (Independent variable: Humidity, Dependent variable: Max Temperature)
humidity = np.array([85, 80, 78, 75, 70]).reshape(-1, 1)  # Independent variable (X)
max_temp = np.array([30, 32, 33, 35, 38])  # Dependent variable (Y)

# Step 2: Create and Train the Linear Regression Model
model = LinearRegression()
model.fit(humidity, max_temp)  # Training the model

# Step 3: Make Predictions
humidity_test = np.array([82, 76, 72]).reshape(-1, 1)  # New humidity values
predicted_temp = model.predict(humidity_test)  # Predict max temperature

# Step 4: Print Predictions
for h, t in zip(humidity_test.flatten(), predicted_temp):
    print(f"Predicted Max Temp for Humidity {h}%: {t:.2f}°C")

# Step 5: Visualize the Data
plt.scatter(humidity, max_temp, color='blue', label="Actual Data")  # Plot actual data points
plt.plot(humidity, model.predict(humidity), color='red', label="Regression Line")  # Plot best-fit line
plt.scatter(humidity_test, predicted_temp, color='green', marker='x', label="Predictions")  # Plot predictions
plt.xlabel("Humidity (%)")
plt.ylabel("Max Temperature (°C)")
plt.title("Linear Regression: Humidity vs Max Temperature")
plt.legend()
plt.show()
