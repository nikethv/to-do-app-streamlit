import streamlit as st
from utils.session import login_user_session
from api import login_user

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email and password:
        user = login_user(email, password)
        if user:
            st.success("Login successful!")
            login_user_session(email)  # Save session
            st.switch_page("pages/3_Home.py")  # ✅ Redirect to Home after login
        else:
            st.error("Invalid credentials.")
    else:
        st.warning("Please enter email and password.")
