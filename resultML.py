#import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

#Load the Data
data = pd.read_csv("Study_Data.csv")

data['Result'] = (data['Scores']>=40).astype(int)

x = data['Hours'].values.reshape(-1,1)
y = data['Result'].values

#Create and Train the Model
model = LogisticRegression()
model.fit(x, y)

#Make Predictions
new_hours = np.array ([1.5, 4, 6, 7.5, 8.4, 9, 12]).reshape(-1,1)
predictions = model.predict(new_hours)

#Print the Results
for h, res in zip (new_hours.flatten(), predictions):
    print(f"{h} hours - {'pass' if res==1 else 'fail'}")

# Plot sigmoid curve
X_test = np.linspace(0, 12, 300).reshape(-1,1)
y_prob = model.predict_proba(X_test)[:,1]

#Visualize
plt.scatter(x, y, color='blue', label='Data')
plt.plot(X_test, y_prob, color='red', label='Sigmoid Curve')
plt.xlabel("Study Hours")
plt.ylabel("Pass Probablity")
plt.legend()
plt.show()
