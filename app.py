import streamlit as st
import requests
import json

# Streamlit UI setup
st.title("🤖 Gemini Chatbot")
st.write("Ask me anything, and I'll answer using Google's Gemini API!")

# Set your API key (Do NOT hardcode in production)
API_KEY = "AIzaSyDUsNMBuDq0C7zAmJjSQUEU5-hLNtcd4v8"  # Replace this with your actual key

# Define function to communicate with Gemini API
def chat_with_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            result = response.json()
            text_response = result['candidates'][0]['content']['parts'][0]['text']
            return text_response
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            return f"Error decoding response: {e}, Raw response: {response.text}"
    else:
        return f"Error: {response.status_code} - {response.text}"

# User input box
user_input = st.text_input("You:", "")

# Generate response when user enters text
if user_input:
    with st.spinner("Thinking... 🤔"):
        response_text = chat_with_gemini(user_input)
    st.write(f"🤖 Gemini: {response_text}")
