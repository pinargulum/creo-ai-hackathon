from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
from bson import ObjectId
from models.schemas import UserCreateRequest, UserCreateRespose, UserUpdate
from uuid import uuid4
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# MongoDB connections and create new collection
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
users_collection = db["users"]
conversation_collection = db["user_conversations"]

# Create a user
@router.post("/crm/create_user", response_model=UserCreateRespose)
def create_user(user: UserCreateRequest):
    user_id = str(uuid4())
    user_data = user.model_dump()
    user_data.update({
        "user_id": user_id,
        "created_at": datetime.now(timezone.utc)
    })
    users_collection.insert_one(user_data)
    return {
        "user_id": user_id,
         "message": "User created successfully"
    }
# Update User
@router.put("/crm/update_user/{user_id}") 
def update_user(user_id: str, user_update: UserUpdate):
    updated_data = {k: v for k, v in user_update.model_dump().items() if v is not None}
    if not updated_data:
        raise HTTPException(status_code=400, detail="No valid information to update.")
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User info updated"}
 
 # Get Conversations
@router.get("/crm/conversations/{user_id}")
def get_conversations(user_id: str):
    conversations = list(conversation_collection.find({"user_id": user_id}))
    if not conversations:
        raise HTTPException(status_code=404, detail="No conversations found")

    for c in conversations:
        c["_id"] = str(c["_id"])
    return conversations

# Delete CRM data
@router.delete("/crm/users/{user_id}")
def delete_user(user_id: str):
    result = conversation_collection.delete_one({"user_id": user_id})
    if result.deleted_count == 1:
        return {"message": "User data is deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found.")

__all__ = ["router"]     