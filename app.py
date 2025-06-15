import streamlit as st
import yaml
import random

# --- PASSWORD GATE ---
st.set_page_config(page_title="LexIQ Labs", layout="centered")
st.title("🔐 LexIQ Labs - PsychBlend AI")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter Access Code", type="password")
    if password == "DEMO2025":  # change this to your secure pass
        st.session_state.authenticated = True
        st.experimental_rerun()
    elif password:
        st.error("Invalid access code.")
    st.stop()

# --- FORM ---
st.header("🧠 Input Details for Personalization")

with st.form("input_form"):
    prospect_name = st.text_input("Prospect Name", "Jordan")
    pain_point = st.text_input("Main Pain Point", "No qualified leads")
    desired_outcome = st.text_input("Desired Outcome", "10 sales calls per week")
    future_timeline = st.text_input("Future Timeline", "30 days")
    wait_period = st.text_input("How long have they waited?", "3 weeks")
    competitor_name = st.text_input("Competitor Name (optional)", "Coach Lenny")
    cost_savings = st.text_input("Cost Savings (optional)", "$2000")
    added_revenue = st.text_input("Added Revenue (optional)", "$5000")
    impact_percent = st.text_input("Impact Percent (optional)", "30%")
    goal_date = st.text_input("Goal Date (optional)", "June 30")

    submitted = st.form_submit_button("🔮 Blend My Prompts")

# --- LOAD PROMPTS + GENERATE ---
if submitted:
    with open("psychology_micro_prompts.yaml", "r") as f:
        all_fragments = yaml.safe_load(f)

    selected = random.sample(all_fragments["fragments"], 5)

    st.subheader("🧩 Blended Prompts + Email Generators")

    for i, frag in enumerate(selected, 1):
        blended = frag.format(
            prospect_name=prospect_name,
            pain_point=pain_point,
            desired_outcome=desired_outcome,
            future_timeline=future_timeline,
            wait_period=wait_period,
            competitor_name=competitor_name,
            cost_savings=cost_savings,
            added_revenue=added_revenue,
            impact_percent=impact_percent,
            goal_date=goal_date
        )

        chatgpt_prompt = (
            f"Write a persuasive cold email to {prospect_name} that starts with this hook:\n"
            f"\"{blended}\"\n\n"
            f"The email should highlight their pain point: '{pain_point}', "
            f"and propose a way to achieve '{desired_outcome}' in {future_timeline}. "
            f"Include subtle urgency, a clear CTA, and end with a conversational tone."
        )

        # --- DISPLAY TABLE STYLE ---
        st.markdown(f"### 🔹 Line {i}")

        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("**🎯 Blended Prompt**")
            st.success(blended)

        with col2:
            st.markdown("**📨 ChatGPT Prompt**")
            st.code(chatgpt_prompt, language="markdown")
