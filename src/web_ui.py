import streamlit as st
from planner import plan_response
from executor import execute
import requests
from datetime import datetime

st.set_page_config(page_title="Crisis Response Agent", layout="centered")

dark_mode = st.toggle("🌙 Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: white;
            }
            .stTextInput, .stTextArea, .stSelectbox, .stButton {
                background-color: #333333;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

st.subheader("📞 Emergency Contact")
emergency_contacts = {
    "Police": "100",
    "Ambulance": "102",
    "Fire Department": "101",
    "Disaster Helpline": "108",
    "Local Support": "1234567890"
}
selected_contact = st.selectbox("Select Contact", list(emergency_contacts.keys()))
st.info(f"Call **{selected_contact}** at **{emergency_contacts[selected_contact]}**")

def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return f"{data.get('city')}, {data.get('region')}, {data.get('country')} | IP: {data.get('ip')}"
    except:
        return "Unable to fetch location"

st.write(" **Your Approximate Location:**", get_location())

st.subheader("Agent Personality")
style = st.selectbox("Choose Agent Style", ["Calm", "Urgent", "Friendly", "Formal"])
style_instructions = {
    "Calm": "Provide a composed and thoughtful response to reassure the user.",
    "Urgent": "Respond with urgency and direct action steps.",
    "Friendly": "Respond in a supportive and approachable tone.",
    "Formal": "Respond in a professional and official manner."
}

st.title("Crisis Response Agent")
emergency_type = st.selectbox("🌪️ Select Crisis Type", ["Flood", "Fire", "Earthquake", "Medical Emergency", "Other"])
user_input = st.text_area("Describe your situation", height=150)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Generate Help Plan"):
    with st.spinner("Analyzing your situation..."):
        prompt = f"{style_instructions[style]}\n\n" + plan_response(emergency_type, user_input)
        result = execute(prompt)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Agent", result))
        st.success("✅ Response Generated!")
        st.write(result)

def download_chat():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crisis_chat_{now}.txt"
    content = "\n".join([f"{sender}: {msg}" for sender, msg in st.session_state.chat_history])
    st.download_button("💾 Save Chat", content, file_name=filename)

if st.session_state.chat_history:
    st.subheader("💬 Chat History")
    for sender, msg in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {msg}")
    download_chat()
