# src/gemini_client.py

import streamlit as st
import google.generativeai as genai

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in Streamlit secrets!")

genai.configure(api_key=api_key)

# ✅ Use correct model name with full path
model = genai.GenerativeModel(model_name="models/gemini-pro")

def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower():
            return "⚠️ Quota exceeded. Try again later."
        return f"❌ Gemini Error: {str(e)}"
