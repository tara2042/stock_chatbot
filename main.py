
from fastapi import FastAPI, Request
from pydantic import BaseModel


from .llm_client import call_ollama_to_generate_sql, explain_sql_result_ollama
from .prompt_template import SQL_GEN_TEMPLATE, ANSWER_GEN_TEMPLATE
from .sql_handler import run_sql_query

app = FastAPI()

# Pydantic model for input validation
class ChatRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to StockBot API. Use /chat POST endpoint."}

# ✅ Chat endpoint with proper input type
@app.post("/chat")
def chat(request: ChatRequest):
    query = request.query
    print(f"Received query: {query}")

    # Call your custom LLM/Ollama function here
    response = call_ollama_to_generate_sql(query)

    # Step 2: Execute SQL
    result = run_sql_query(response)
    natural_response = explain_sql_result_ollama(query, result)

    return {
        "user_query": query,
        "generated_sql": response,
        "result": result,
        "natural_response": natural_response
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)