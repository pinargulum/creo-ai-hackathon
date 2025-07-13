from openai import OpenAI
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import re

load_dotenv()

# MongoDB
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
knowledge_collection = db["knowledge"]
conversation_collection = db["user_conversations"]

def ask_openai(message: str, user_id: str) -> dict:
    # get the document from MongoDB
    documents = knowledge_collection.find().limit(50)
    data_snippets = []

    for doc in documents:
        snippet = f"""
Property Address: {doc.get("Property Address", "")}
Floor: {doc.get("Floor", "")}
Suite: {doc.get("Suite", "")}
Size (SF): {doc.get("Size (SF)", "")}
Rent/SF/Year: {doc.get("Rent/SF/Year", "")}
Monthly Rent: {doc.get("Monthly Rent", "")}
GCI On 3 Years: {doc.get("GCI On 3 Years", "")}
"""
        data_snippets.append(snippet.strip())

    context = "\n\n".join(data_snippets)

    # History
    past_conversations = conversation_collection.find({"user_id": user_id}).sort("timestamp", -1).limit(10)
    chat_history = "\n".join([
        f"User: {c['user_message']}\nAssistant: {c['assistant_response']}" 
        for c in reversed(list(past_conversations))
    ])

    prompt = f"""
You are a helpful commercial real estate assistant.

Here is the user's previous conversation history (if any):
{chat_history}

Here is relevant property data: 
{context}

Now answer the user's new message:
{message}

Please answer the user's question using **only** the data above. 
If the answer is not in the data, say exactly: "I don’t have that information."

At the end of your response, ALWAYS include the category of the conversation. 
You MUST respond in the following exact format:

Answer: <your answer here>  
Category: <Property Address | Size | Rent>

"""

    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    content = response.choices[0].message.content.strip()
    
    match = re.search(r"Answer:\s*(.*?)\s*Category:\s*(.*)", content, re.DOTALL)
    if match:
        answer = match.group(1).strip()
        category = match.group(2).strip()
    else:
        answer = content
        category = "Uncategorized"

    return {
        "reply": answer,
        "category": category
    }
