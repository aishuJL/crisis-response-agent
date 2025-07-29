# src/app.py

import streamlit as st
from planner import plan_response
from executor import execute

st.title("Crisis Response Agent")

emergency_type = st.selectbox("Select crisis type", ["Fire", "Flood", "Earthquake", "Medical", "Other"])
user_input = st.text_area("Describe your situation:")

if st.button("Generate Help"):
    prompt = plan_response(emergency_type, user_input)
    result = execute(prompt)
    st.markdown("### Agent Response")
    st.write(result)
