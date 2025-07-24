# stock_chatbot
A chatbot which takes queries in plain english and transforms into sql queries to retrieve related information


# Stock Chatbot

A FastAPI-powered chatbot that uses Ollama (Mistral) to generate SQL queries and answer user questions using local SQLite data.

## Requirements
- Python 3.10+
- Ollama (with Mistral model)
- FastAPI
- SQLite

## How to run

1. Start Ollama:
```bash
ollama run mistral

### Run FastAPI:
uvicorn stockbot.app.main:app --reload

### TESt with:
curl -X POST http://127.0.0.1:8000/chat -d '{"query":"Show me all the top indices on 2025-07-22"}' -H "Content-Type: application/json"


---

### 🧬 5. **Create GitHub repository**

1. Go to: https://github.com
2. Click ➕ → **New Repository**
3. Name it (e.g., `stock_chatbot`)
4. Don’t initialize with README/gitignore (you already have those)
5. Click **Create Repository**

---

### 🔗 6. **Add GitHub remote and push**

```bash
# Replace with your actual repo URL
git remote add origin https://github.com/YOUR_USERNAME/stock_chatbot.git
git branch -M main
git add .
git commit -m "Initial commit of stock chatbot"
git push -u origin main

### Test Your Clone
git clone https://github.com/tara2042/stock_chatbot.git
cd stock_chatbot
pip install -r requirements.txt
uvicorn stockbot.app.main:app --reload
