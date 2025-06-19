# pages/Add_Task.py

import streamlit as st
from api import add_task

def main():
    st.title("➕ Add New Task")

    if not st.session_state.get("logged_in"):
        st.warning("Please login to continue.")
        st.stop()

    task_name = st.text_input("Task Name")
    status = st.selectbox("Status", ["open", "closed"])
    due_time = st.text_input("Due Time (YYYY-MM-DD HH:MM)")

    if st.button("Add Task"):
        if not task_name or not due_time:
            st.warning("Please fill in all fields.")
        else:
            result = add_task(st.session_state["email"], task_name, status, due_time)
            if result["status"] == "success":
                st.success(result["message"])
            else:
                st.error("Failed to add task.")

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.experimental_rerun()

if __name__ == "__main__":
    main()