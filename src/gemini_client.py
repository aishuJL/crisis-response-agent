import streamlit as st
import google.generativeai as genai

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in Streamlit secrets!")

genai.configure(api_key=api_key)

# Gemini Pro via v1 endpoint (correct model call)
try:
    model = genai.GenerativeModel(model_name="models/gemini-pro")
except Exception as e:
    st.error(f"Model Load Error: {str(e)}")
    raise e

def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower():
            return "Quota exceeded for Gemini API. Please wait or reduce usage."
        return f"Gemini Error: {str(e)}"
