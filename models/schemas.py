from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    category: str

# Create User
class UserCreateRequest(BaseModel):
    name: str
    email: str
    company: str
    role: str
    preferences: dict = {}

class UserCreateRespose(BaseModel):
    user_id: str
    message: str

# Update user Data
class UserUpdate(BaseModel):
    name: str
    email: str
   

