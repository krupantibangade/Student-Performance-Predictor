import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/student_model.pkl")

# Page settings
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Store prediction history
if "history" not in st.session_state:
    st.session_state.history = []

# Header
st.title("🎓 Student Performance Predictor")
st.write("Machine Learning Based Student Marks Prediction")
st.divider()

# Sidebar
st.sidebar.title("About Project")
st.sidebar.info(
    "This project uses Linear Regression "
    "to estimate student exam performance."
)

st.sidebar.write("**Technologies Used**")
st.sidebar.write("Python")
st.sidebar.write("Pandas")
st.sidebar.write("Scikit-learn")
st.sidebar.write("Streamlit")

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "Linear Regression")

with col2:
    st.metric("Dataset Size", "200 Students")

with col3:
    st.metric("Input Features", "5")

st.divider()

# Input section
st.header("📋 Enter Student Details")

with st.form("prediction_form"):

    c1, c2 = st.columns(2)

    with c1:
        study_hours = st.slider(
            "Daily Study Hours", 1.0, 10.0, 5.0
        )

        previous_marks = st.slider(
            "Previous Marks", 0.0, 100.0, 60.0
        )

        attendance = st.slider(
            "Attendance (%)", 50.0, 100.0, 75.0
        )

    with c2:
        sleep_hours = st.slider(
            "Sleep Hours", 4.0, 10.0, 7.0
        )

        assignments = st.slider(
            "Assignments Completed", 1, 10, 5
        )

    submitted = st.form_submit_button(
        "🔮 Predict Final Marks",
        use_container_width=True
    )

# Prediction
if submitted:

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "previous_marks": [previous_marks],
        "attendance": [attendance],
        "sleep_hours": [sleep_hours],
        "assignments": [assignments]
    })

    prediction = model.predict(input_data)[0]
    prediction = max(0, min(100, prediction))

    # Save history
    st.session_state.history.append({
        "Study Hours": study_hours,
        "Previous Marks": previous_marks,
        "Attendance": attendance,
        "Predicted Marks": round(prediction, 2)
    })

    st.success("Prediction completed successfully!")

    st.subheader("📊 Prediction Result")

    st.metric(
        "Estimated Final Marks",
        f"{prediction:.2f}/100"
    )

    st.progress(int(prediction))

    if prediction >= 75:
        st.success("Excellent performance! 🌟")
    elif prediction >= 50:
        st.info("Good performance. Keep improving! 👍")
    else:
        st.warning("More preparation may help. 📚")

# Prediction history
st.divider()
st.header("📈 Prediction History")

if st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

    st.subheader("Predicted Marks Chart")

    chart_data = history_df[
        ["Predicted Marks"]
    ]

    st.line_chart(chart_data)

    if st.button("Clear Prediction History"):
        st.session_state.history = []
        st.rerun()

else:
    st.info("Your prediction history will appear here.")

st.divider()

st.caption(
    "Student Performance Predictor | Built using Python and Machine Learning"
)
