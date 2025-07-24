
SQL_GEN_TEMPLATE = """
You are a helpful assistant. Convert the user question to an SQL query based on the following schema:

- Table: signals(stock, signal_type, confidence, date)
- Table: pnl(stock, profit, loss, date)
- Table: top_indices(index_name, performance, date)
- Table: news(stock, headline, date, sentiment)

Question: {question}
SQL:
"""

ANSWER_GEN_TEMPLATE = """
You are a financial assistant. Given the SQL output below, respond with a clear, concise answer to the user query.

SQL Output:
{data}

User Question: {question}

Answer:
"""

# prompt_templates.py

# SQL_GEN_TEMPLATE = "Write a SQL query to answer the following question:\n{question}"
# ANSWER_GEN_TEMPLATE = "Given the SQL result: {result}, provide a clear answer to:\n{question}"
# GENERAL_QUESTION = "Give answer to the following question:\n{question}"