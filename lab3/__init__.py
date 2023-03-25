import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Import dataset
data = pd.read_csv("height_weight.csv")

# Create X and y arrays
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create Linear Regression model and train it
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict values using test set
y_pred = regressor.predict(X_test)

# Visualize training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Weight vs. Height (Training set)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# Visualize test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Weight vs. Height (Test set)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
