import sqlite3

conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS signals")
cursor.execute("DROP TABLE IF EXISTS pnl")
cursor.execute("DROP TABLE IF EXISTS top_indices")
cursor.execute("DROP TABLE IF EXISTS news")

cursor.execute("""
CREATE TABLE signals (
    stock TEXT,
    signal_type TEXT,
    confidence REAL,
    date TEXT
)
""")
cursor.executemany("INSERT INTO signals VALUES (?, ?, ?, ?)", [
    ('CG', 'BUY', 0.85, '2025-07-22'),
    ('NIMB', 'SELL', 0.78, '2025-07-22'),
    ('SBIN', 'HOLD', 0.50, '2025-07-22'),
])

cursor.execute("""
CREATE TABLE pnl (
    stock TEXT,
    profit REAL,
    loss REAL,
    date TEXT
)
""")
cursor.executemany("INSERT INTO pnl VALUES (?, ?, ?, ?)", [
    ('CG', 12000, 0, '2025-07-20'),
    ('NIMB', 0, 5000, '2025-07-21'),
    ('SBIN', 7000, 0, '2025-07-20'),
])

cursor.execute("""
CREATE TABLE top_indices (
    index_name TEXT,
    performance REAL,
    date TEXT
)
""")
cursor.executemany("INSERT INTO top_indices VALUES (?, ?, ?)", [
    ('NIFTY50', 2.3, '2025-07-22'),
    ('SENSEX', 2.1, '2025-07-22'),
    ('NIFTYBANK', 1.9, '2025-07-22'),
])

cursor.execute("""
CREATE TABLE news (
    stock TEXT,
    headline TEXT,
    date TEXT,
    sentiment TEXT
)
""")
cursor.executemany("INSERT INTO news VALUES (?, ?, ?, ?)", [
    ('CG', 'CG announces robust Q1 earnings', '2025-07-21', 'Positive'),
    ('NIMB', 'NIMB stock drops amid IT downturn', '2025-07-21', 'Negative'),
    ('SBIN', 'SBIN plans new consumer banking project', '2025-07-20', 'Positive'),
])

conn.commit()
conn.close()

print("Database stock.db created successfully!")
