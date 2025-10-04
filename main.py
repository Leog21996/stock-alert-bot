from db_utils import create_db, insert_price
from datetime import datetime
import pandas as pd
import yfinance as yf

tickers = ["AAPL", "TSLA", "UCG.MI"]

def main():
    
    create_db()
    
    for ticker in tickers:
        
        data = yf.download(ticker, period="2d", interval="1d")
        if not data.empty:
            
            last_row = data.iloc[-1]
            date = pd.to_datetime(last_row.name).strftime("%Y-%m-%d")
            open_p = float(last_row["Open"].iloc[0])
            high_p = float(last_row["High"].iloc[0])
            low_p = float(last_row["Low"].iloc[0])
            close_p = float(last_row["Close"].iloc[0])
            
            insert_price(ticker, date, open_p, high_p, low_p, close_p)
            print(f"✅ Inserito {ticker} {date}: O={open_p}, H={high_p}, L={low_p}, C={close_p}")
        else:
            print(f"⚠️ Nessun dato disponibile per {ticker}")
    
if __name__ == "__main__":
    main()