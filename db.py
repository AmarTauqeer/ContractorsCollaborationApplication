from pymongo import MongoClient
from werkzeug.security import generate_password_hash

from user import User

client = MongoClient(
    "mongodb://localhost:27017/ContractorsCollaboration?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
)
db = client.get_database("ContractorsCollaboration")
users = db.get_collection("users")

# save users


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users.insert_one({"_id": username, "email": email, "password": password_hash})


def get_user(username):
    user_data = users.find_one({"_id": username})
    return (
        User(user_data["_id"], user_data["email"], user_data["password"])
        if user_data
        else None
    )


# save_user("amar", "amar.tauqeer@gmail.com", "amar")
