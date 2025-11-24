import streamlit as st
import graphviz
import time

# Page Configuration
st.set_page_config(page_title="Kruskal's Quest", page_icon="🌲", layout="centered")

# --- CSS for styling ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        margin-bottom: 1rem;
    }
    .main-title {
        font-size: 3rem;
        color: #0E1117;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State Management ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'duration' not in st.session_state:
    st.session_state.duration = 0

# --- Header ---
st.markdown('<div class="main-title">🌲 Kruskal\'s Quest</div>', unsafe_allow_html=True)
st.caption("Master the Minimum Spanning Tree (MST) by solving the puzzle below.")
st.divider()

# --- Start Game Logic ---
if not st.session_state.game_started:
    st.info("Ready to test your knowledge? Click the button below to start the timer!")
    if st.button("Start Game ⏱️"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()
        st.rerun()

# --- Game Content (Only show if started) ---
if st.session_state.game_started:
    
    # --- Setup the Graph Data ---
    # Nodes: A, B, C, D, E
    # Edges: (Source, Target, Weight)
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 5),
        ('B', 'D', 10),
        ('C', 'E', 3),
        ('D', 'E', 7),
        ('C', 'D', 1) # The smallest edge
    ]

    # Create Graphviz diagram
    graph = graphviz.Graph()
    graph.attr(rankdir='LR')
    for u, v, w in edges:
        graph.edge(u, v, label=str(w))

    # --- QUESTION 1: The Sorting Phase ---
    st.subheader("Question 1: The Sorting Phase")
    st.markdown("Kruskal's algorithm relies on processing edges in a specific order. Look at the graph below and **select the edges in the order Kruskal's algorithm would consider them** (Ascending Weight).")

    st.graphviz_chart(graph)

    # Create options for the multiselect
    edge_options = [f"{u}-{v} (Weight: {w})" for u, v, w in edges]
    # Correct order (sorted by weight)
    sorted_edges_data = sorted(edges, key=lambda x: x[2])
    correct_order = [f"{u}-{v} (Weight: {w})" for u, v, w in sorted_edges_data]

    user_order = st.multiselect(
        "Drag and drop or select edges in the correct sorted order:",
        options=edge_options,
        help="Pick the edge with the smallest weight first, then the next smallest, etc."
    )

    st.divider()

    # --- QUESTION 2: Concept ---
    st.subheader("Question 2: Cycle Detection")
    q2_options = [
        "Breadth-First Search (BFS)",
        "Depth-First Search (DFS)",
        "Union-Find (Disjoint Set)",
        "Dijkstra's Algorithm"
    ]
    q2_answer = st.radio(
        "Which data structure is most efficiently used in Kruskal's algorithm to detect if adding an edge creates a cycle?",
        q2_options,
        index=None
    )

    st.divider()

    # --- QUESTION 3: Concept ---
    st.subheader("Question 3: Algorithm Strategy")
    q3_options = [
        "Dynamic Programming",
        "Greedy Algorithm",
        "Divide and Conquer",
        "Backtracking"
    ]
    q3_answer = st.radio(
        "Kruskal's algorithm builds the MST by always choosing the locally optimal choice (lightest edge) at each step. What type of algorithm is this?",
        q3_options,
        index=None
    )

    st.divider()

    # --- Submission Logic ---

    if st.button("Submit Answers"):
        # Calculate duration immediately
        end_time = time.time()
        st.session_state.duration = end_time - st.session_state.start_time
        
        score = 0
        feedback = []
        
        # Check Q1
        if not user_order:
            feedback.append("❌ **Q1:** You didn't select any edges.")
        elif user_order == correct_order:
            score += 1
            feedback.append("✅ **Q1:** Correct! You sorted the edges perfectly by weight.")
        else:
            feedback.append("❌ **Q1:** Incorrect. Kruskal's sorts all edges from lowest weight to highest weight.")

        # Check Q2
        if q2_answer == "Union-Find (Disjoint Set)":
            score += 1
            feedback.append("✅ **Q2:** Correct! Union-Find is efficient for cycle detection.")
        else:
            feedback.append("❌ **Q2:** Incorrect. While BFS/DFS can detect cycles, Union-Find is the standard for Kruskal's efficiency.")

        # Check Q3
        if q3_answer == "Greedy Algorithm":
            score += 1
            feedback.append("✅ **Q3:** Correct! It is a Greedy strategy.")
        else:
            feedback.append("❌ **Q3:** Incorrect. It chooses the best immediate option, making it Greedy.")

        # Display Results
        st.session_state.submitted = True
        st.session_state.score = score
        
        st.subheader("Results")
        
        # Show Time Taken
        st.markdown(f"⏱️ **Time Taken:** {st.session_state.duration:.2f} seconds")
        
        for msg in feedback:
            st.markdown(msg)
        
        if score == 3:
            st.balloons()
            st.success(f"🏆 Perfect Score! {score}/3. You are a Kruskal's Master!")
        elif score == 2:
            st.info(f"👍 Good job! {score}/3.")
        else:
            st.warning(f"📚 Keep studying! Score: {score}/3.")
            
    if st.session_state.submitted:
        if st.button("Restart Game"):
            st.session_state.game_started = False
            st.session_state.submitted = False
            st.session_state.score = 0
            st.rerun()

# --- Sidebar Info ---
with st.sidebar:
    st.header("Algorithm Recap")
    st.markdown("""
    **Kruskal's Algorithm Steps:**
    1. **Sort** all edges by weight (Low to High).
    2. Pick the **smallest** edge.
    3. Check if it forms a **cycle** with the spanning tree formed so far.
    4. If **no cycle**, include it.
    5. Repeat until you have **V-1** edges.
    """)
    if st.session_state.game_started and not st.session_state.submitted:
        st.warning("Timer is running! ⏳")
    st.info("Built with Streamlit 🎈")