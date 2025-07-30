import streamlit as st
from planner import plan_response
from executor import execute
from gemini_client import generate_content  

st.write(generate_content("Say hi from Gemini"))


st.title("Crisis Response Agent")

emergency_type = st.selectbox("Select crisis type", ["Fire", "Flood", "Earthquake", "Medical", "Other"])
user_input = st.text_area("Describe your situation:")

if st.button("Generate Help"):
    prompt = plan_response(emergency_type, user_input)
    result = execute(prompt)
    st.markdown("### Agent Response")
    st.write(result)

# Optional debug test to ensure Gemini works
with st.expander("🔍 Test Gemini Connection (Debug)"):
    if st.button("Test Gemini API"):
        test_response = generate_content("How can AI help in crisis response?")
        st.write(test_response)
