import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("dataset/students.csv")

# Select input features
X = df[[
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Score",
    "Internal_Marks"
]]

# Select target
y = df["Final_Marks"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict marks
predictions = model.predict(X_test)

# Evaluate model
print("ACTUAL MARKS:")
print(y_test.values)

print("\nPREDICTED MARKS:")
print(predictions.round(2))

print("\nMEAN ABSOLUTE ERROR:")
print(mean_absolute_error(y_test, predictions))

print("\nR2 SCORE:")
print(r2_score(y_test, predictions))

# Predict marks for a new student
new_student = pd.DataFrame([{
    "Study_Hours": 4,
    "Attendance": 80,
    "Previous_Marks": 70,
    "Assignment_Score": 75,
    "Internal_Marks": 72
}])

predicted_marks = model.predict(new_student)

print("\nNEW STUDENT PREDICTED MARKS:")
print(round(predicted_marks[0], 2))