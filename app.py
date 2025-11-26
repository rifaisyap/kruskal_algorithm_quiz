import streamlit as st
import time

st.set_page_config(page_title="Kruskal Quiz", layout="centered")

st.title("🎮 Kruskal's Algorithm – Quiz Game")
st.write("Press **Start Quiz** to begin. The timer starts once you click Start.")

# Initialize session
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Create start button
if not st.session_state.quiz_started:
    if st.button("▶ Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.start_time = time.time()
        st.rerun()

if not st.session_state.quiz_started:
    st.stop()

# Insert Image (used only for Q1 now)
st.write("---")
st.subheader("Graph Reference")
st.image("image.png", width=600)
st.write("Refer to the graph above for **Question 1**.")

# Question 1
st.markdown("### **1. Which edge is the *first* added to the MST using Kruskal’s Algorithm?**")

q1_options = [
    "A. Edge (5, 4) with weight 9",
    "B. Edge (1, 2) with weight 2",
    "C. Edge (2, 3) with weight 3",
    "D. Edge (1, 4) with weight 1",
]

correct_q1 = "D. Edge (1, 4) with weight 1"

q1 = st.radio(
    "",
    q1_options,
    index=None,
    key="q1"
)

# Question 2 (original Q3)
st.write("---")
st.markdown("### **2. Which data structure is used to detect cycles in Kruskal’s Algorithm?**")

q2_options = [
    "A. Stack",
    "B. Queue",
    "C. Union–Find (Disjoint Set)",
    "D. Binary Tree",
]

correct_q2 = "C. Union–Find (Disjoint Set)"

q2 = st.radio(
    "",
    q2_options,
    index=None,
    key="q2"
)

# Question 3 (original Q4)
st.write("---")
st.markdown("### **3. Which statement correctly describes Kruskal’s Algorithm?**")

q3_options = [
    "A. It starts from one node and expands outward.",
    "B. It selects edges with the largest weight first.",
    "C. It is a greedy algorithm used to build an MST.",
    "D. It only works for directed graphs.",
]

correct_q3 = "C. It is a greedy algorithm used to build an MST."

q3 = st.radio(
    "",
    q3_options,
    index=None,
    key="q3"
)

# Submit button
st.write("---")
if st.button("✅ Submit Answers"):
    score = 0
    st.subheader("Results")

    # Question 1
    st.markdown("### **Question 1**")
    if q1 == correct_q1:
        st.success("✔ Correct!")
        score += 1
    else:
        st.error(f"✘ Incorrect. You chose: {q1}")
        st.info(f"Correct answer: **{correct_q1}**")

    # Question 2
    st.markdown("### **Question 2**")
    if q2 == correct_q2:
        st.success("✔ Correct!")
        score += 1
    else:
        st.error(f"✘ Incorrect. You chose: {q2}")
        st.info(f"Correct answer: **{correct_q2}**")

    # Question 3
    st.markdown("### **Question 3**")
    if q3 == correct_q3:
        st.success("✔ Correct!")
        score += 1
    else:
        st.error(f"✘ Incorrect. You chose: {q3}")
        st.info(f"Correct answer: **{correct_q3}**")

    # Final Score
    st.write("---")
    st.markdown(f"## 🎯 Final Score: **{score} / 3**")

    # Time
    duration = int(time.time() - st.session_state.start_time)
    if duration < 60:
        st.write(f"⏱️ Time taken: **{duration} sec**")
    else:
        st.write(f"⏱️ Time taken: **{duration//60} min {duration%60} sec**")

    # Restart
    if st.button("🔄 Restart Quiz"):
        st.session_state.quiz_started = False
        st.rerun()
