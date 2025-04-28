import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Step 1: Generate synthetic dataset (50 samples, 2 features)
np.random.seed(42)

# Features: X, labels: y
X = np.random.randn(50, 2)  # 50 samples, 2 features
y = np.random.randint(0, 2, size=50)  # 50 labels, 0 or 1 (binary classification)

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Create and train the model (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 3: Make predictions
y_pred = model.predict(X_test)

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Print the results
print("Confusion Matrix:")
print(cm)

# Other metrics (Accuracy, Classification Report)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
