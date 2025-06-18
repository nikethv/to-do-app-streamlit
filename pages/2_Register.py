import streamlit as st
from api import register_user


st.title("📝 Register")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if email and password:
        result = register_user(email, password)
        if result["status"] == "success":
            st.success("Registration successful!")
            st.switch_page("pages/1_Login.py")  # or go straight to dashboard if you prefer
        else:
            st.error(result["message"])
    else:
        st.warning("Please fill in all fields.")
