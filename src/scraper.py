import yfinance as yf
import pandas as pd

def get_daily_stock_data(ticker: str) -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    daily_data = stock.history(period="1d")

    return daily_data


if __name__ == "__main__":
    ticker = "SAN.MC"
    stock_data = get_daily_stock_data(ticker)

    print(f"Daily stock data for {ticker}:")
    print(stock_data)