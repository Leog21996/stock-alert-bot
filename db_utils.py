import sqlite3
from datetime import datetime, timedelta

DB_NAME = "stocks.db"

def create_db():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,
        open_price REAL,
        high_price REAL,
        low_price REAL,
        close_price REAL NOT NULL,
        PRIMARY KEY (ticker, date)
        )
        """)
    conn.commit()
    conn.close()
    
def insert_price(ticker: str, date: str, open_p: float, high_p: float, low_p: float, close_p: float):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO stock_prices (ticker, date, open_price, high_price, low_price, close_price)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (ticker, date, open_p, high_p, low_p, close_p))
    cutoff = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=30)).strftime("%Y-%m-%d")
    cursor.execute("DELETE FROM stock_prices WHERE date < ?", (cutoff,))
    conn.commit()
    conn.close()
    
def get_prices(ticker:str):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, open_price, high_price, low_price, close_price
        FROM stock_prices 
        WHERE ticker = ? ORDER BY date
        """, (ticker,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_latest_price(ticker:str):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, open_price, high_price, low_price, close_price 
        FROM stock_prices 
        WHERE ticker = ? 
        ORDER BY date DESC LIMIT 1
        """, (ticker,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_highs_and_close(ticker):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT date, high, close FROM stock_prices
        WHERE ticker = ?
        ORDER BY date DESC
        """, (ticker,))
    
    rows = cursor.fetchall()
    conn.close()
    
    if len(rows) < 2:
        return None, None, None
    
    today_close = rows[0][2]
    yesterday_high = rows[1][1]
    historical_high = max([row[1] for row in rows[2:]]) if len(rows) > 2 else yesterday_high
    
    return yesterday_high, historical_high, today_close