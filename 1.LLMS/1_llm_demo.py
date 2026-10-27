from langchain_core.prompts import load_prompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
template=load_prompt('template.json')
st.title("AI Learning Assistant")

# Initialize the model
chat_model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_completion_tokens=1000
)

# Get user inputs
topic = st.text_input(
    "Enter the topic you want to learn about:",
    key="topic"
)

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=80,
    key="age"
)

# Create the prompt template


# Generate the explanation
if st.button("Generate Explanation"):
    if topic.strip():
        chain=template|chat_model
        response=chain.invoke({
            "topic": topic,
            "years": age
        })
        st.write(response.content)
    else:
        st.warning("Please enter a topic.")
