import streamlit as st
import yaml
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="LexIQ Labs", layout="centered")

# --- PASSWORD GATE ---
st.title("🔐 LexIQ Labs - PsychBlend AI")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    password = st.text_input("Enter Access Code", type="password")
    if st.button("Login"):
        if password == "DEMO2025":
            st.session_state["authenticated"] = True
            st.experimental_rerun()
        else:
            st.error("Invalid access code.")
    st.stop()

# --- FORM ---
st.header("🧠 Fill Out These Details")

with st.form("input_form"):
    prospect_name = st.text_input("Prospect Name", "Jordan")
    pain_point = st.text_input("Pain Point", "No qualified leads")
    desired_outcome = st.text_input("Desired Outcome", "10 booked calls")
    future_timeline = st.text_input("Future Timeline", "30 days")
    wait_period = st.text_input("Wait Period", "2 weeks")
    competitor_name = st.text_input("Competitor", "Coach Lenny")
    cost_savings = st.text_input("Cost Savings", "$500")
    added_revenue = st.text_input("Added Revenue", "$2000")
    impact_percent = st.text_input("Impact %", "40%")
    goal_date = st.text_input("Goal Date", "End of June")
    
    submitted = st.form_submit_button("🔮 Blend My Prompts")

if submitted:
    try:
        with open("psychology_micro_prompts.yaml", "r") as f:
            data = yaml.safe_load(f)
            fragments = data["fragments"]
    except Exception as e:
        st.error(f"Failed to load prompt file: {e}")
        st.stop()

    selected = random.sample(fragments, 5)

    st.subheader("🧠 Blended Prompts + ChatGPT Prompts")
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
            f"Write a cold email to {prospect_name} that begins with this line:\n"
            f"\"{blended}\"\n\n"
            f"Highlight the pain point ({pain_point}), offer a way to reach {desired_outcome} in {future_timeline}, "
            f"and include a soft CTA and a conversational tone."
        )

        st.markdown(f"### 🔹 Prompt {i}")
        st.success(blended)
        st.markdown("**🧠 ChatGPT Prompt:**")
        st.code(chatgpt_prompt)
