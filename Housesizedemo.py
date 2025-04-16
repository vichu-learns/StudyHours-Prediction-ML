import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Training Data (House Size in Square Feet & Corresponding Prices in $1000s)
house_size = np.array([600, 750, 900, 1100, 1500]).reshape(-1, 1)  # Input (X)
house_price = np.array([150, 180, 210, 250, 320])  # Output (Y)

# Step 2: Create and Train the Model
model = LinearRegression()
model.fit(house_size, house_price)

# Step 3: Predict Prices for New Houses
new_sizes = np.array([800, 1000, 1300]).reshape(-1, 1)
predicted_prices = model.predict(new_sizes)

# Step 4: Print the Predictions
for size, price in zip(new_sizes.flatten(), predicted_prices):
    print(f"Predicted Price for {size} sq.ft: ${price:.2f}K")

# Step 5: Visualization
plt.scatter(house_size, house_price, color='blue', label="Training Data")  # Original Data
plt.plot(house_size, model.predict(house_size), color='red', linestyle="dashed", label="Regression Line")  # Line of Best Fit
plt.scatter(new_sizes, predicted_prices, color='green', marker='x', s=100, label="Predictions")  # Predictions

plt.xlabel("House Size (sq.ft)")
plt.ylabel("Price ($1000s)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()
