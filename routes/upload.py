from fastapi import APIRouter, UploadFile, File
import csv
from io import StringIO
from pymongo import MongoClient
import openai
import os
from dotenv import load_dotenv

load_dotenv() #loads env

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB= os.getenv("MONGO_DB")

client = MongoClient(MONGO_URI)
print("Mongo Connected")
db = client[MONGO_DB] #veriable name
knowlage_collection = db["knowledge"]
users_collection = db["users"]

@router.post("/upload_docs")
async def  upload_docs(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return { "error": "Only CSV files are supported for now"}
    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.DictReader(StringIO(decoded))
    inserted = 0
    for row in reader:
            print(row)
            knowlage_collection.insert_one(dict(row))
            inserted += 1
    return {"message": f"{inserted} rows inserted into knowlage base."}

__all__ = ["router"]