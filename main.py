from db_utils import create_db, insert_price, get_highs_and_close
import time
import pandas as pd
import yfinance as yf
from tickers import S_P_500, DJIA, NASDAQ_100, DAX, FTSE_100, FTSE_MIB, CAC_40

tickers = S_P_500 + DJIA + NASDAQ_100 + DAX + FTSE_100 + FTSE_MIB + CAC_40
batch_size = 50

ALERT_DAILY_THRESHOLD = -10.0
ALERT_HISTORICAL_THRESHOLD = -15.0

def chunks(lst, n):
    
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def check_alerts(ticker):
    yesterday_high, historical_high, today_close = get_highs_and_close(ticker)
    
    if yesterday_high is None or historical_high is None or today_close is None:
        return

    daily_variation = ((today_close - yesterday_high) / yesterday_high) * 100
    if daily_variation <= ALERT_DAILY_THRESHOLD:
        print(f"⚠️ ALERT GIORNALIERO: {ticker} è sceso del {daily_variation:.2f}% "
              f"rispetto al massimo di ieri ({yesterday_high}), close oggi: {today_close}")
    
    historical_variation = ((today_close - historical_high) / historical_high) * 100
    if historical_variation <= ALERT_HISTORICAL_THRESHOLD:
        print(f"⚠️ ALERT STORICO: {ticker} è sceso del {historical_variation:.2f}% "
              f"rispetto al massimo storico ({historical_high}), close oggi: {today_close}")

def main():
    
    create_db()
    
    for batch in chunks(tickers, batch_size):
        for ticker in batch:
            data = yf.download(ticker, period="2d", interval="1d", progress=False, auto_adjust=False)
            
            if not data.empty:
                for date_index, row in data.iterrows():
                    date_str = pd.to_datetime(date_index).strftime("%Y-%m-%d")
                    open_p = float(row["Open"].iloc[0])
                    high_p = float(row["High"].iloc[0])
                    low_p = float(row["Low"].iloc[0])
                    close_p = float(row["Close"].iloc[0])
                    
                    insert_price(ticker, date_str, open_p, high_p, low_p, close_p)
                    check_alerts(ticker)
            else:
                print(f"⚠️ Nessun dato disponibile per {ticker}")
        
        print(f"✅ Batch completato: {batch[0]} - {batch[-1]}")
        time.sleep(5)

if __name__ == "__main__":
    main()