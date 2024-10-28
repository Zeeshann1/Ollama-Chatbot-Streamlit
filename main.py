#'''''
import streamlit as st
import ollama
from typing import Dict, Generator


# Main Ollama respose generator function
def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']

## StreamLit Code
st.subheader("Ask Any Question From Ollama Streamlit Chatbot 💻")

with st.sidebar:
        st.header("Ollama Streamlit Chatbot with Python 🚀")
        st.image("image.png")

# Streamlit Session State
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
if "messages" not in st.session_state:
    st.session_state.messages = []


# Model Selection
st.session_state.selected_model = st.selectbox(
    "Please select the model: ⚙️", [model["name"] for model in ollama.list()["models"]])

# Chat Message Display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handling
if prompt := st.chat_input("Ask Anything.."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

     # Assistant Response
    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            st.session_state.selected_model, st.session_state.messages))
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    
#'''''





