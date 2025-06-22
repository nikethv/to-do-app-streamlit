import streamlit as st
from api import get_tasks
from utils.session import get_logged_in_user_email

st.set_page_config(page_title="To-Do App", layout="centered")
st.title("📝 Welcome to the To-Do App")
st.write("Use the sidebar to Login, Register, and manage your tasks.")

# Get the logged-in user
email = get_logged_in_user_email()

if email:
    st.subheader(f"Welcome, {email}!")
    st.title("Task Dashboard")

    if st.button("Get My Tasks"):
        tasks = get_tasks(email)
        if tasks:
            st.success(f"Found {len(tasks)} tasks:")
            for task in tasks:
                st.write(f"**Task:** {task['task_name']}")
                st.write(f"**Due:** {task['due_time']}")
                st.write(f"**Status:** {task['status']}")
                st.markdown("---")
        else:
            st.warning("No tasks found for this email.")
else:
    st.warning("Please login from the sidebar to view your tasks.")
