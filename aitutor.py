import streamlit as st
import random
import pandas as pd

# Initialize the app
st.set_page_config(page_title="AI Math Tutor", page_icon="📚", layout="wide")

# Load the dataset (replace 'math_dataset.csv' with your file path)
@st.cache_data
def load_data():
    return pd.read_csv('math_dataset.csv', encoding='latin1')

# Initialize the app
#st.set_page_config(page_title="AI Math Tutor", page_icon="📚", layout="wide")

# Load data
data = load_data()

# App title
st.title("📚 AI Math Tutor")
st.subheader("Learn and Practice Middle School Math!")

# Navigation
options = ["Home", "Take Quiz", "Performance Dashboard"]
choice = st.sidebar.radio("Navigate", options)

# Home Page
if choice == "Home":
    st.write("""
    Welcome to AI Math Tutor! Practice math questions, track your progress, 
    and master your skills while having fun! 🌟
    """)
    st.image("Download Isolated Mathematics font banner for free.jpg", use_column_width=True)  # Add a friendly banner image

# Take Quiz Page
elif choice == "Take Quiz":
    st.header("Take a Quiz 📝")
    
    # Select topic
    topics = data['Topic'].unique()
    topic_choice = st.selectbox("Choose a topic:", topics)
    
    # Filter data by topic
    topic_data = data[data['Topic'] == topic_choice]
    
    # Randomly select a question
    question_data = topic_data.sample(1).iloc[0]
    question = question_data['Question']
    options = [question_data['Option1'], question_data['Option2'], 
               question_data['Option3'], question_data['Option4']]
    correct_answer = question_data['Answer']
    solution = question_data['Solution']
    
    # Display question
    st.write(f"**{question}**")
    user_answer = st.radio("Select your answer:", options)
    
    # Submit button
    if st.button("Submit"):
        if user_answer == correct_answer:
            st.success("🎉 Correct! Great job!")
        else:
            st.error("❌ Oops! That's incorrect.")
            st.write(f"**Solution:** {solution}")

# Performance Dashboard
elif choice == "Performance Dashboard":
    st.header("Your Progress 📊")
    st.write("This section will display your quiz performance and suggest areas to improve.")
    # Placeholder for performance tracking (e.g., charts and tables)
    st.info("Feature under development!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for middle school students to excel in math!")
