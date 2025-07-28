import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

models = genai.list_models()
for m in models:
    print(m.name)
