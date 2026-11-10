🎓 Student Performance Predictor

A Machine Learning project that predicts students' estimated final exam marks based on their academic performance and daily habits.

📌 Project Overview

The Student Performance Predictor uses **Linear Regression**, a supervised machine learning algorithm, to estimate students' final marks using five input features.

The project provides an interactive web application built using Streamlit.

✨ Features

- Predict estimated final exam marks.
- Enter study hours and previous marks.
- Consider attendance and sleep hours.
- Include completed assignments.
- View prediction results.
- View prediction history and charts.

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
 📂 Project Structure

Student_Performance_Predictor/
│
├── data/
│   └── student_data.csv
│
├── models/
│   └── student_model.pkl
│
├── app.py
├── generate_data.py
├── train_model.py
├── requirements.txt
└── README.md

⚙️ Installation and Setup

1. Clone the repository:
git clone https://github.com/krupantibangade/Student-Performance-Predictor.git

2. Open the project folder:
cd Student-Performance-Predictor

3. Create a virtual environment:
python -m venv venv

4. Activate it (Windows PowerShell):
.\venv\Scripts\Activate.ps1

5. Install dependencies:
pip install -r requirements.txt

6. Generate the dataset:
python generate_data.py

7. Train the machine learning model:
python train_model.py

8. Run the application:
streamlit run app.py

Open http://localhost:8501 in your browser.

 🧠 Machine Learning Algorithm

**Linear Regression**

Input features:
1. Study Hours
2. Previous Marks
3. Attendance
4. Sleep Hours
5. Assignments Completed

Output:
- Estimated Final Marks

👩‍💻 Author

**Krupanti Bangade**

Student | IT

---

⭐ If you find this project useful, consider giving it a star!

