
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'stock.db')
DB_PATH = os.path.abspath(DB_PATH)

# def run_sql_query(query: str):
#     conn = sqlite3.connect('stock.db')  # Or absolute path if needed
#     cursor = conn.cursor()

#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         print(f'SQL Query output - \n{result}')
#         col_names = [desc[0] for desc in cursor.description]
#         conn.close()
#         return [dict(zip(col_names, row)) for row in result]
#     except Exception as e:
#         conn.close()
#         return f"SQL error: {str(e)}"

def run_sql_query(query: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            col_names = [description[0] for description in cursor.description]
            result = [dict(zip(col_names, row)) for row in rows]
        else:
            conn.commit()
            result = {"status": "Query executed successfully."}
        
        conn.close()
        return result
    except Exception as e:
        return {"error": f"SQL error: {str(e)}"}

# if __name__ == "__main__":
#     query = "SELECT * FROM signals WHERE date = '2025-07-22';"
#     results = run_sql_query(query)
#     print(results)