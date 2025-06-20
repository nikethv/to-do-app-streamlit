
# 📝 To-Do List Web App (Streamlit + MongoDB)

This is a simple, user-friendly task management web app built using **Streamlit** for the frontend and **MongoDB** for backend data storage. Users can register, log in, add tasks with due dates, and automatically close overdue tasks.

---

## 🚀 Features

- 🔐 User Registration and Login
- ✅ Add, Edit, and View Tasks
- 🗓️ Due date and time picker
- 🔄 Auto-close tasks past due
- 🧠 Session management using Streamlit
- 💾 MongoDB integration for storing users and tasks

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** MongoDB (local or Atlas)

---

## 📂 Project Structure

To-do-list/
│
├── app.py # Main Streamlit launcher
├── api.py # API logic for database operations
├── db.py # MongoDB connection
├── README.md # This file
│
├── utils/
│ ├── session.py # User session handling
│
├── pages/
│ ├── 1_Login.py # Login page
│ ├── 2_Register.py # Registration page
│ ├── 3_Home.py # Main dashboard with task list
│ ├── 4_Add_task.py # Add new tasks (if used separately)

yaml
Copy
Edit

---

## ▶️ How to Run

1. **Install dependencies:**

```bash
pip install streamlit pymongo
Start MongoDB locally or connect to MongoDB Atlas.

Run the app:

bash
Copy
Edit
streamlit run app.py
✨ Future Enhancements
Task filtering (open/closed)

Task priority and reminders

User profile page

📧 Contact
Developed by Niketh Vattumilli
📩 niketh.vattumilli@gmail.com

