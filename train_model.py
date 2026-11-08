
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Step 1: Load student dataset
data = pd.read_csv("data/student_data.csv")

# Step 2: Select input features
X = data[[
    "study_hours",
    "previous_marks",
    "attendance",
    "sleep_hours",
    "assignments"
]]

# Step 3: Select target
y = data["final_marks"]

# Step 4: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model training completed successfully!")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Step 8: Save trained model
joblib.dump(model, "models/student_model.pkl")

print("Model saved successfully!")
