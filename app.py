import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Pocket Smart AI", page_icon="💰")
st.title("💰 Pocket Smart AI")
st.subheader("Your Smart Budget & Recommendation Assistant")

# API Key from Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-3.8-flash")

# User Inputs
st.sidebar.header("Enter Your Details")
income = st.sidebar.number_input("Monthly Income (₹)", 5000, 1000000, 20000)
rent = st.sidebar.number_input("Rent / Hostel (₹)", 0, 500000, 5000)
food = st.sidebar.number_input("Food Expense (₹)", 0, 500000, 3000)
travel = st.sidebar.number_input("Travel (₹)", 0, 500000, 2000)
others = st.sidebar.number_input("Others (₹)", 0, 500000, 2000)
goal = st.sidebar.text_input("What you want to buy? (ex: iPhone 15, Bike)")

if st.button("💡 Analyze My Budget"):
    total_expense = rent + food + travel + others
    savings = income - total_expense
    
    prompt = f"""
    Act as a smart financial advisor for a college student in India.
    Income: {income} rupees
    Expenses: Rent {rent}, Food {food}, Travel {travel}, Others {others}
    Total Expense: {total_expense}, Savings: {savings}
    Goal: {goal}
    
    Give in 3 parts:
    1. Budget Analysis with 50/30/20 rule
    2. Is the goal affordable? If not, how many months to save?
    3. 3 Smart Money Saving Tips for students in Tamil Nadu
    Make it friendly and simple.
    """
    
    with st.spinner("AI is analyzing your pocket..."):
        response = model.generate_content(prompt)
        st.success("Analysis Ready!")
        st.markdown(response.text)

st.markdown("---")
st.caption("Built by Fathima | Powered by Gemini AI")
