from db import get_db
from bson.objectid import ObjectId

# ----------------------------
# User Authentication
# ----------------------------

def login_user(email, password):
    db = get_db()
    users_col = db["users"]
    
    user = users_col.find_one({"email": email, "password": password})
    
    if user:
        return {
            "status": "success",
            "user_id": str(user["_id"]),
            "email": user["email"]
        }
    else:
        return {
            "status": "failure",
            "message": "Invalid email or password"
        }

def register_user(email, password):
    db = get_db()
    users_col = db["users"]

    existing_user = users_col.find_one({"email": email})
    if existing_user:
        return {"status": "failure", "message": "Email already registered."}

    users_col.insert_one({"email": email, "password": password})
    return {"status": "success", "message": "User registered successfully."}

# ----------------------------
# Task Operations
# ----------------------------

def add_task(email, task_name, status, due_time):
    db = get_db()
    tasks_col = db["tasks"]
    tasks_col.insert_one({
        "email": email,
        "task_name": task_name,
        "status": status,
        "due_time": due_time
    })
    return {"status": "success", "message": "Task added successfully."}

def get_tasks(email):
    db = get_db()
    tasks_col = db["tasks"]
    
    tasks = list(tasks_col.find({"email": email}))
    
    for task in tasks:
        task["_id"] = str(task["_id"])
        
    return tasks    

def update_task_status(task_id, new_status):
    db = get_db()
    tasks_col = db["tasks"]
    tasks_col.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": new_status}}
    )

def update_task(task_id, task_name, status, due_time):
    db = get_db()
    tasks_col = db["tasks"]
    tasks_col.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": {
                "task_name": task_name,
                "status": status,
                "due_time": due_time
            }
        }
    )
