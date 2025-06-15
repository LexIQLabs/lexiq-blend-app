import streamlit as st
import yaml
import random

# --- CONFIG ---
st.set_page_config(page_title="LexIQ Labs – PsychBlend", layout="centered")

# --- STYLING ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0f0f0f;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    .stButton button {
        background-color: #3EB489;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #3EB489;
    }
    </style>
""", unsafe_allow_html=True)

# --- UNIQUE CODES ---
VALID_CODES = {
    "ALEX78G2": "Alex",
    "JRD2024VIP": "Jordan",
    "SMRAKEY09": "Samira",
    "DEMO2025": "Demo User"
}

# --- GATE ---
def access_gate():
    st.title("🔐 LexIQ Labs")
    st.markdown("Enter your access code to unlock **PsychBlend AI**.")
    code_input = st.text_input("🔑 Access Code", type="password", help="Personal code issued after purchase.")
    if code_input in VALID_CODES:
        st.success(f"Welcome, {VALID_CODES[code_input]} 👋")
        return True
    elif code_input:
        st.error("Invalid code. Please check and try again.")
        return False
    else:
        return False

if not access_gate():
    st.stop()

# --- APP START ---
st.title("🧠 PsychBlend AI")
st.markdown("#### Elite Prompt Composer for Closers, Creators & Strategists")
st.markdown("Use psychology-infused micro-prompts to craft influence-first messages for ChatGPT, email, or DMs.")

# --- PROMPT LOGIC ---
@st.cache_data
def load_prompts():
    with open("psychology_micro_prompts.yaml", "r") as f:
        return yaml.safe_load(f)

prompts = load_prompts()

st.markdown("---")
st.markdown("### ✍️ Fill in Context Variables")

with st.form("input_form"):
    data = {
        'prospect_name': st.text_input("👤 Prospect Name", "Alex"),
        'pain_point': st.text_input("⚠️ Pain Point", "low engagement"),
        'desired_outcome': st.text_input("🎯 Desired Outcome", "10 booked calls"),
        'future_date': st.text_input("📅 Future Timeline", "90 days"),
        'waiting_period': st.text_input("⏳ Wait Period", "2 weeks"),
        'competitor_name': st.text_input("🏆 Competitor Name", "Coach Lenny"),
        'cost_savings': st.text_input("💸 Cost Savings", "$500/month"),
        'added_revenue': st.text_input("📈 Added Revenue", "$2,000"),
        'impact_percent': st.text_input("📊 Impact %", "30%"),
        'goal_date': st.text_input("🚀 Goal Date", "End of this month"),
    }

    submitted = st.form_submit_button("🔮 Blend My Prompts")

if submitted:
    st.markdown("### 💬 Your Blended Prompts")
    sampled = random.sample(prompts, 5)
    for i, prompt in enumerate(sampled, 1):
        for key, value in data.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value)
        st.markdown(f"`{i}. {prompt}`")
    st.success("✅ Copied? Use them inside ChatGPT or cold DMs.")


