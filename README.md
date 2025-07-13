# 🏢 CREO-AI: AI-Powered Real Estate Assistant

CREO-AI is a lightweight AI Agent for the Commercial Real Estate (CRE) sector. It helps brokers, landlords, and tenants with real-time property discovery, lease support, and intelligent conversation — powered by OpenAI and FastAPI.

---

## 🚀 Features

- 🔍 **Smart Q&A over internal data:** Upload `.csv` documents and let the AI answer user queries based on real property listings.
- 🧠 **LLM-backed reasoning:** Uses OpenAI GPT models to process natural language and generate database filters.
- 📂 **MongoDB Integration:** Documents and conversation history are stored in a structured MongoDB schema.
- 💬 **Conversation Tracker (CRM-style):** Keeps track of user conversations by user_id, allows reset and query history.
- ✍️ **Categorization & Optional Tagging:** AI classifies user intent for routing or segmentation purposes.
- 📌 **RESTful API Endpoints:** FastAPI backend with modular endpoints for document upload, chat, user creation and conversation history.

---

## 🧩 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **LLM:** OpenAI GPT (via API)
- **Testing Tool:** Postman

---

## 📁 Project Structure

📦 creo-ai-hackathon
├── main.py # FastAPI app entrypoint
├── upload.py # Handles file upload & parsing
├── openai_service.py # Interacts with OpenAI API
├── chat.py # Handles chat + context logic
├── crm/
│ ├── create_user.py
│ ├── update_user.py
│ ├── conversations.py
├── models/ # Pydantic schemas
├── .env # API keys and DB URI (ignored)
├── requirements.txt
└── README.md 


---

## 📦 Setup & Installation

1. **Clone the Repository**

```bash
git clone https://github.com/pinargulum/creo-ai-hackathon.git
cd creo-ai-hackathon
pip install -r requirements.txt


| Method | Endpoint                            | Description                |
| ------ | ----------------------------------- | -------------------------- |
| POST   | `/upload_docs`                      | Upload CSV file to MongoDB |
| POST   | `/chat/{user_id}`                   | Ask AI a question          |
| POST   | `/crm/create_user`                  | Register new user          |
| PUT    | `/crm/update_user/{user_id}`        | Update user details        |
| GET    | `/crm/conversations/{user_id}`      | Fetch conversation history |
| POST   | `/crm/reset_conversation/{user_id}` | Clear past chat context    |


Sample Usage
POST /chat/123456

{
  "message": "Which office spaces are available in Manhattan over 10,000 SF?"
}

🧠 Prompt Engineering Insight
We designed the prompt to:

Accept user message as the main question

Dynamically construct MongoDB filter queries

Respond only using available documents (not general knowledge)