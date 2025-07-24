
def classify_query(query: str) -> str:
    query = query.lower()
    if "signal" in query or "buy" in query or "sell" in query:
        return "signal"
    elif "profit" in query or "loss" in query:
        return "pnl"
    elif "top" in query or "perform" in query:
        return "top_indices"
    elif "news" in query:
        return "news"
    else:
        return "general"
