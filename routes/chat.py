from fastapi import APIRouter
from openai import OpenAI
from pymongo import MongoClient
from models.schemas import ChatRequest, ChatResponse
from services.openai_service import ask_openai
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# MongoDB
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
knowledge_collection = db["knowledge"]
conversation_collection = db["user_conversations"]

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    result = ask_openai(request.message, request.user_id)
    conversation = {
        "user_id": request.user_id,
        "user_message": request.message,
        "assistant_response": result["reply"],
        "category": result["category"],
        "timestamp": datetime.now(timezone.utc)
    }
    conversation_collection.insert_one(conversation)
    return {"reply": result["reply"], "category": result["category"]}

@router.post("/reset")
def reset_conversation(request: ChatRequest):
    result = conversation_collection.delete_many({"user_id": request.user_id})
    return {"message": f"{result.deleted_count} conversation deleted {request.user_id}"}
   
__all__ = ["router"]  