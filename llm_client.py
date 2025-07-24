
import json
import requests
from .prompt_template import SQL_GEN_TEMPLATE
# from prompt_template import SQL_GEN_TEMPLATE

OLLAMA_HOST = "http://localhost:11434"

def call_ollama_to_generate_sql(question: str, model: str = "mistral") -> str:
    prompt = SQL_GEN_TEMPLATE.format(question=question)
    print("Prompt sent to model:\n", prompt)
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(f"{OLLAMA_HOST}/api/generate", json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"
    


def explain_sql_result_ollama(user_query: str, sql_result: list) -> str:
    prompt = f"""
You are a helpful assistant. The user asked the following question:

"{user_query}"

Here is the result retrieved from a database query (in JSON format):

{json.dumps(sql_result, indent=2)}

Now, explain this result in plain, easy-to-understand English, as if you are talking to a user in a chatbot.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",   # or use the model name you pulled in Ollama
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Ollama call failed with status {response.status_code}"


# if __name__ == "__main__":
#     question = "What is the signal for CG on 2025-07-22?"
#     result = call_ollama_to_generate_sql(question)
#     print("Generated SQL:\n", result)