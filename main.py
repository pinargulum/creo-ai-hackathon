from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.upload import router as upload_router
from routes.crm import router as crm
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(crm)



