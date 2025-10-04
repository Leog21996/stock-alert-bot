from db_utils import create_db, insert_price
from datetime import datetime
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
            data = yf.download(ticker, period="2d", interval="1d", progress=False, auto_adjust=False)
            
            if not data.empty:
                last_row = data.iloc[-1]
                date = pd.to_datetime(last_row.name).strftime("%Y-%m-%d")
                open_p = float(last_row["Open"].iloc[0])
                high_p = float(last_row["High"].iloc[0])
                low_p = float(last_row["Low"].iloc[0])
                close_p = float(last_row["Close"].iloc[0])
                insert_price(ticker, date, open_p, high_p, low_p, close_p)
        print(f"✅ Batch completato: {batch[0]} - {batch[-1]}")
        time.sleep(5)
    
if __name__ == "__main__":
    main()