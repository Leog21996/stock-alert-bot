from db_utils import create_db, insert_price, get_prices, get_latest_price
from datetime import datetime

def main():
    
    create_db()
    
    today = datetime.today().strftime("%Y-%m-%d")
    insert_price(
        ticker = "APPL",
        date = today,
        open_p = 170.5,
        high_p = 172.2,
        low_p = 169.8,
        close_p = 171.4 
    )
    
    prices = get_prices("APPL")
    print("📈 Storico AAPL:", prices)
    
    latest = get_latest_price("APPL")
    print("🆕 Ultimo record AAPL:", latest)
    
if __name__ == "__main__":
    main()