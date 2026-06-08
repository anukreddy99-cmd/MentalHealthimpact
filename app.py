import streamlit as st
import pandas as pd
import pickle

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Mental Health Impact Predictor",
    page_icon="🧠",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    color: #2563eb;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}

.prediction-box {
    background-color: #f0f9ff;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #2563eb;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<h1 class='title'>🧠 Mental Health Impact Predictor</h1>",
            unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Predict mental health impact based on social media usage and lifestyle factors</p>",
    unsafe_allow_html=True
)

st.divider()

# ------------------ INPUTS ------------------
st.subheader("Enter Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 10, 60, 20)
    usage_hours = st.slider("Daily Social Media Usage (Hours)", 0.0, 15.0, 4.0)
    study_hours = st.slider("Study Hours", 0.0, 12.0, 4.0)

with col2:
    sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
    physical_activity = st.slider("Physical Activity (Hours)", 0.0, 8.0, 1.0)
    daily_unlocks = st.number_input("Daily Phone Unlocks", 0, 500, 100)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

platform = st.selectbox(
    "Most Used Platform",
    ["Instagram", "YouTube", "WhatsApp", "Facebook", "Twitter", "LinkedIn"]
)

st.divider()

# ------------------ PREDICT BUTTON ------------------
if st.button("Predict Impact Score", use_container_width=True):

    # Replace this section with actual model prediction
    sample_score = round(
        (usage_hours * 2 + daily_unlocks/50 + study_hours) -
        (sleep_hours + physical_activity),
        2
    )

    st.markdown(
        f"""
        <div class='prediction-box'>
        Predicted Impact Score: {sample_score}
        </div>
        """,
        unsafe_allow_html=True
    )

    if sample_score < 10:
        st.success("Low Mental Health Impact")
    elif sample_score < 20:
        st.warning("Moderate Mental Health Impact")
    else:
        st.error("High Mental Health Impact")

st.divider()

st.caption("Built using Python, Machine Learning and Streamlit")
