import streamlit as st

def login_user_session(email):
    """Set the user session upon login."""
    st.session_state["logged_in"] = True
    st.session_state["email"] = email

def logout():
    """Clear session and rerun the app."""
    st.session_state.clear()
    st.rerun()  # Ensures the app reloads after logout

def is_logged_in():
    """Check if the user is logged in."""
    return st.session_state.get("logged_in", False)

def get_logged_in_user_email():
    """Get the logged-in user's email."""
    return st.session_state.get("email")
