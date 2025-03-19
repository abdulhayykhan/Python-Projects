import streamlit as st
import random
import time

# Set page title and layout
st.set_page_config(page_title="Flashcard Quiz App", layout="centered")

# Define questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the square root of 64?": "8"
}

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(list(questions.keys()))
if "result" not in st.session_state:
    st.session_state.result = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "timer_start" not in st.session_state:
    st.session_state.timer_start = time.time()

# Function to pick a new question
def new_question():
    st.session_state.current_question = random.choice(list(questions.keys()))
    st.session_state.result = ""
    st.session_state.timer_start = time.time()

# Function to check the answer
def check_answer():
    user_answer = st.session_state.user_input.strip()
    correct_answer = questions[st.session_state.current_question]
    
    st.session_state.attempts += 1
    elapsed_time = round(time.time() - st.session_state.timer_start, 2)

    if user_answer.lower() == correct_answer.lower():
        st.session_state.result = f"🎉 Correct! Well done. (⏱ {elapsed_time}s)"
        st.session_state.score += 1
        st.balloons()  # Fun confetti effect
    else:
        st.session_state.result = f"❌ Wrong! The correct answer is: **{correct_answer}** (⏱ {elapsed_time}s)"

# Random background color for variety
bg_color = random.choice(["#F0E68C", "#ADD8E6", "#98FB98", "#FFB6C1"])

# Streamlit UI with dynamic styles
st.markdown(
    f"""
    <style>
        .main {{
            background-color: {bg_color};
            padding: 20px;
            border-radius: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("🧠 Flashcard Quiz App 🎴")
st.subheader("Test your knowledge and have fun!")

st.write(f"**Question ({st.session_state.attempts + 1}):** {st.session_state.current_question}")

# User input for answer
st.session_state.user_input = st.text_input("Your Answer:", key="user_input")

# Buttons for checking answer and getting a new question
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Check Answer"):
        check_answer()

with col2:
    if st.button("🔄 Next Question"):
        new_question()

st.write(st.session_state.result)

# Display score
st.markdown(f"**📊 Score: {st.session_state.score} / {st.session_state.attempts}**")

st.markdown("</div>", unsafe_allow_html=True)
