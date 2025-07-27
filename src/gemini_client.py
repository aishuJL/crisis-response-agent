import os
import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
api_key = st.secrets["GEMINI_API_KEY"]
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower():
            return "⚠️ Quota exceeded for Gemini API. Please wait a few minutes or switch to a lower model (gemini-pro)."
        return f"❌ Gemini Error: {str(e)}"
