# CREO-AI: Commercial Real Estate Optimizer with AI Agents 🏢🤖

CREO-AI is a smart backend system powered by FastAPI, OpenAI, and MongoDB, designed to streamline operations for the Commercial Real Estate (CRE) industry. It supports landlords, brokers, and tenants with intelligent document ingestion, question-answering, lead tracking, and visit scheduling—all via APIs.

---

## 🚀 Features

- ✨ **RAG-Based Chatbot**: Ask questions about properties, leases, or terms. Answers are generated using real-time document data via Retrieval-Augmented Generation (RAG).
- 🧠 **CRM Module**: Logs and retrieves user data, chat history, lead info, and interactions.
- 📄 **Document Upload & Indexing**: Upload property PDFs and make their data searchable for AI.
- 🕓 **Schedule a Visit**: Simulated calendar integration to book visits based on availability.
- 🧪 **JSON API Responses**: All endpoints return structured, standardized JSON data.

---

## 📦 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MongoDB Atlas (NoSQL)
- **AI**: OpenAI GPT API
- **Data Layer**: PyMongo
- **Docs & Scheduling**: Custom RAG + Calendar Simulation

---

## 📁 Folder Structure

```
creo-ai/
│
├── models/               # MongoDB schemas
├── routes/               # All API routes
│   ├── chat.py           # Chat endpoint
│   ├── upload.py         # Upload docs
│   ├── crm.py            # CRM info
│   └── schedule_visit.py # Schedule endpoint
│
├── services/
│   └── openai_service.py # RAG + Chat logic
│
├── .env                  # API keys (placeholder only!)
├── main.py               # Entry point
├── README.md             # This file
├── api_contracts.pdf     # Input/Output samples for APIs
└── requirements.txt      # Dependencies
```

---

## 🔑 Environment Setup

---

## 🧠 How the AI Works

- Uploaded documents are indexed into MongoDB.
- The chatbot (`/chat`) queries OpenAI with context from relevant documents.
- Conversation logs are saved per user ID.
- Responses are enriched using metadata like property address, rent, size, etc.

---

## 📅 Schedule Visit Endpoint

Simulates calendar availability and allows visit scheduling.

### Endpoint

```
POST /schedule_visit
```

### Request Body

```json
{
  "date": "2025-07-14",
  "time": "14:30"
}
```

### Success Response

```json
{
  "status": "confirmed",
  "message": "Visit scheduled for 2025-07-14 at 14:30"
}
```

### Failure Response

```json
{
  "status": "unavailable",
  "suggestions": ["15:00", "15:30", "16:00"]
}
```

---

## 🧾 Sample Conversation Log

```json
{
  "user_id": "xyz123",
  "user_message": "What is the rent for the property on Pine Street?",
  "ai_response": "The rent for 21 Pine Street is $5,200/month."
}
```

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/pinargulum/creo-ai-hackathon.git
cd creo-ai-hackathon
pip install -r requirements.txt
uvicorn main:app --reload
```

Access API at: `http://127.0.0.1:8000/docs`

---

## 📄 API Contract PDF

You can find the input/output schemas and sample API usage in PDF file. 
📎 

---

## 👥 Authors & Credits

Hackathon Project by Pinar Gulum  
OpenAI API | MongoDB Atlas | FastAPI | 

---

