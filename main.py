from db_utils import create_db, insert_price
import time
import pandas as pd
import yfinance as yf
from tickers import S_P_500, DJIA, NASDAQ_100, DAX, FTSE_100, FTSE_MIB, CAC_40

tickers = S_P_500 + DJIA + NASDAQ_100 + DAX + FTSE_100 + FTSE_MIB + CAC_40
batch_size = 50

def chunks(lst, n):
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main():
    
    create_db()
    
    for batch in chunks(tickers, batch_size):
        for ticker in batch:
            data = yf.download(ticker, period="30d", interval="1d", progress=False, auto_adjust=False)
            
            if not data.empty:
                for date_index, row in data.iterrows():
                    date_str = pd.to_datetime(date_index).strftime("%Y-%m-%d")
                    open_p = float(row["Open"].iloc[0])
                    high_p = float(row["High"].iloc[0])
                    low_p = float(row["Low"].iloc[0])
                    close_p = float(row["Close"].iloc[0])
                    
                    insert_price(ticker, date_str, open_p, high_p, low_p, close_p)
            else:
                print(f"⚠️ Nessun dato disponibile per {ticker}")
        
        print(f"✅ Batch completato: {batch[0]} - {batch[-1]}")
        time.sleep(5)

if __name__ == "__main__":
    main()