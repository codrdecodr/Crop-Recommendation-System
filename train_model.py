import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("Crop-recommendation.csv")

# Split features and target
X = df.drop(columns=["label"])  # Features: N, P, K, Temp, Humidity, pH, Rainfall
y = df["label"]  # Target: Crop name

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, "crop_recommendation_model.pkl")
print("🎯 Model saved as crop_recommendation_model.pkl")
