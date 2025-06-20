from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    return client.todo_db

def insert_sample_users():
    db = get_db()
    users_col = db["users"]
    users_col.insert_many([
        {"email":"niketh.vattumilli@gmail.com","password":"Niketh#2004"},
        {"email": "alice@example.com", "password": "alice123"},
        {"email": "bob.smith@testmail.com", "password": "b0bSecure"},
        {"email": "charlie99@demo.org", "password": "charlie_pass"},
        {"email": "diana_dev@workmail.com", "password": "diana789"},
        {"email": "eve.hacker@fake.net", "password": "1234secure"}
    ])
    
def insert_sample_tasks():
    db = get_db()
    tasks_col = db["tasks"]
    tasks_col.insert_many([
            {"email": "alice@example.com", "task_name": "Buy groceries", "status": "open", "due_time": "2025-06-15 18:00"},
        {"email": "alice@example.com", "task_name": "Finish homework", "status": "closed", "due_time": "2025-06-13 22:00"},
        {"email": "bob.smith@testmail.com", "task_name": "Call plumber", "status": "open", "due_time": "2025-06-14 10:00"}
    ]) 