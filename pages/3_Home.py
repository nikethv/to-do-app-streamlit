import streamlit as st
from datetime import datetime
from api import add_task, get_tasks, update_task, update_task_status
from utils.session import is_logged_in, logout

# Handle flexible datetime formats
def parse_due_time(due_time_str):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(due_time_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unknown date format: {due_time_str}")

# Check login
if not is_logged_in():
    st.warning("Please log in to access this page.")
    st.stop()

st.title("📋 Home - Task Dashboard")

if st.button("Logout"):
    logout()  # Automatically reruns using st.rerun() from session.py

email = st.session_state["email"]

# Add Task
task_name = st.text_input("Task Name")
status = st.selectbox("Status", ["open", "closed"])
due_date = st.date_input("Due Date")
due_time = st.time_input("Due Time")
due_datetime = datetime.combine(due_date, due_time).strftime("%Y-%m-%d %H:%M")

if st.button("Add Task"):
    add_task(email, task_name, status, due_datetime)
    st.success("✅ Task Added!")

# Display Tasks
st.subheader("Your Tasks")
tasks = get_tasks(email)

for task in tasks:
    task_id = task["_id"]
    due = parse_due_time(task["due_time"])
    now = datetime.now()

    # Auto-close overdue tasks
    if due < now and task["status"] != "closed":
        update_task_status(task_id, "closed")
        task["status"] = "closed"

    st.markdown(f"**📝 Task:** {task['task_name']}")
    st.markdown(f"📅 **Due:** {task['due_time']}")
    st.markdown(f"🚦 **Status:** {task['status']}")

    # Edit section
    with st.expander("✏️ Edit Task"):
        new_name = st.text_input("Edit Task Name", value=task["task_name"], key=f"name_{task_id}")
        new_status = st.selectbox(
            "Edit Status", ["open", "closed"],
            index=["open", "closed"].index(task["status"]),
            key=f"status_{task_id}"
        )
        new_due_date = st.date_input("Edit Due Date", value=due.date(), key=f"due_date_{task_id}")
        new_due_time = st.time_input("Edit Due Time", value=due.time(), key=f"due_time_{task_id}")
        new_due = datetime.combine(new_due_date, new_due_time).strftime("%Y-%m-%d %H:%M")

        if st.button("Save Changes", key=f"save_{task_id}"):
            update_task(task_id, new_name, new_status, new_due)
            st.success("✅ Task Updated!")
            st.rerun()

    st.divider()

