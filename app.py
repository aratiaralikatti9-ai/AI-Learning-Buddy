import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🤖",
    layout="wide"
)

# Background design
st.markdown("""
<style>

.stApp {
    background-color: #eaf4ff;
}

/* Main heading */
h1 {
    color: #2563eb;
    text-align: center;
    font-weight: 700;
}

/* Sub headings */
h2, h3 {
    color: #1e40af;
}

/* Button style */
.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background-color: #1d4ed8;
}

/* Input boxes */
.stTextInput input,
.stTextArea textarea {
    border-radius: 10px;
    border: 1px solid #93c5fd;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #dbeafe;
}

</style>
""", unsafe_allow_html=True)


# Your existing project code starts here
st.title("🤖 AI Dashboard")
st.markdown("""
## Welcome to AI Learning Buddy

An intelligent educational assistant powered by Artificial Intelligence that simplifies complex concepts, generates personalized learning content, creates assessments, and supports self-paced learning through interactive conversations.

✨ Explain Concepts
📖 Real-Life Examples
📝 AI-Generated Quizzes
💬 Ask Anything
""")

st.title("🤖 AI Learning Buddy")
st.write("Learn any topic with the help of AI.")


# Load API key from secrets.toml
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


topic = st.text_input("Enter a Topic")


option = st.selectbox(
    "Choose Learning Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)


if st.button("Generate"):

    if topic:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for beginners."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions with answers about {topic}."

        else:
            prompt = topic


        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        st.subheader("AI Response")
        st.write(response.choices[0].message.content)


    else:
        st.warning("Please enter a topic.")