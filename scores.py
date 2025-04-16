# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Read data from csv file
data = pd.read_csv("Study_data.csv")

#Data
Hours = data["Hours"].values.reshape(-1,1)
Scores = data["Scores"].values

#Train the model
Model = LinearRegression()
Model.fit(Hours, Scores)

#Test data
New_Hours = np.array([11,13,9.5,2.5,1.6]).reshape(-1, 1)
Predicted_Scores = Model.predict(New_Hours)

#Print Output
for h, s in zip(New_Hours.flatten(), Predicted_Scores) :
    print(f"Predicted scores for {h} hours is : {s}")

#Visualize
plt.scatter(Hours, Scores, color = 'blue', label = "Training Data")
plt.plot(Hours, Model.predict(Hours), color = 'red', linestyle = 'dashed', label = "Regression Line")
plt.scatter(New_Hours, Predicted_Scores, color = 'green', label = "Predicted data")

plt.xlabel = ("Study Hours")
plt.ylabel = ("Scores")
plt.title = ("Study Hours based on Scores")
plt.legend()
plt.show()