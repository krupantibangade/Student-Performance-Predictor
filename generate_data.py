
import pandas as pd
import numpy as np

# Step 1: Generate student data
np.random.seed(42)

students = 200

study_hours = np.random.uniform(1, 10, students)
previous_marks = np.random.uniform(30, 95, students)
attendance = np.random.uniform(50, 100, students)
sleep_hours = np.random.uniform(4, 10, students)
assignments = np.random.randint(1, 11, students)

# Step 2: Calculate final marks
noise = np.random.normal(0, 5, students)

final_marks = (
    study_hours * 3
    + previous_marks * 0.45
    + attendance * 0.15
    + sleep_hours * 0.5
    + assignments * 0.5
    + noise
)

final_marks = np.clip(final_marks, 0, 100)

# Step 3: Create student dataset
data = pd.DataFrame({
    "study_hours": study_hours,
    "previous_marks": previous_marks,
    "attendance": attendance,
    "sleep_hours": sleep_hours,
    "assignments": assignments,
    "final_marks": final_marks
})

# Step 4: Save data in CSV file
data.to_csv("data/student_data.csv", index=False)

print("Student dataset created successfully!")
print(data.head())

print("\nTotal students:", len(data))
