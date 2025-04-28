"""  
What is a Regression Curve?

A regression curve (or line) is a line that visualizes the relationship between the dependent variable and the independent
 variable. This line represents the mathematical model that best explains the points in the dataset.

The most common type of regression is linear regression. In this type, a linear relationship is assumed. However, 
the regression curve may not be linear in some cases, and in such situations, more complex models are used.
"""


# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Generating 50 random data points (X is the independent variable)
X = np.random.rand(50, 1) * 10  # 50 random numbers between 0 and 10

# Real linear relationship: y = 2 * X + 1 with some noise added
y = 2 * X + 1 + np.random.randn(50, 1)  # Adding noise

# --- 1. Linear Regression Model ---
# Creating the Linear Regression model
model = LinearRegression()
model.fit(X, y)  # Fitting the model to the data

# Making predictions based on the linear regression model
y_pred = model.predict(X)

# --- 2. Polynomial Regression Model ---
# Transforming the data to a polynomial form (degree 3)
poly = PolynomialFeatures(degree=3)  # 3rd degree polynomial
X_poly = poly.fit_transform(X)  # Transforms X into a polynomial feature set

# Creating the Polynomial Regression model
poly_model = LinearRegression()
poly_model.fit(X_poly, y)  # Fitting the polynomial model to the transformed data

# Making predictions based on the polynomial regression model
y_poly_pred = poly_model.predict(X_poly)

# --- 3. Visualization (Plotting the graphs) ---
plt.figure(figsize=(12, 6))

# Plot for Linear Regression
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue', label='Real Data')  # Plotting the original data points
plt.plot(X, y_pred, color='red', label='Linear Regression Line')  # Plotting the linear regression line
plt.title('Linear Regression')
plt.xlabel('Independent Variable (X)')
plt.ylabel('Dependent Variable (y)')
plt.legend()

# Plot for Polynomial Regression
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='blue', label='Real Data')  # Plotting the original data points
plt.plot(X, y_poly_pred, color='green', label='Polynomial Regression Curve (Degree 3)')  # Plotting the polynomial regression curve
plt.title('Polynomial Regression (Degree 3)')
plt.xlabel('Independent Variable (X)')
plt.ylabel('Dependent Variable (y)')
plt.legend()

# Displaying the plots
plt.tight_layout()
plt.show()

# --- 4. Model Evaluation (R² Score) ---
# R² score for Linear Regression model
r2_score = model.score(X, y)
print(f"Linear Regression R² Score: {r2_score:.4f}")  # Printing the R² score for linear regression

# R² score for Polynomial Regression model
r2_poly_score = poly_model.score(X_poly, y)
print(f"Polynomial Regression R² Score: {r2_poly_score:.4f}")  # Printing the R² score for polynomial regression
