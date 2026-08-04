import os
from datetime import datetime

from scraper import get_daily_stock_data
from transformer import clean_stock_data


def run_pipeline(ticker: str = "SAN.MC") -> None:
    try:
        print(f"🚀 Running data pipeline for ticker: {ticker}")

        print(f"📥 Fetching daily stock data for {ticker}...")
        df = get_daily_stock_data(ticker=ticker)

        print(f"🧹 Cleaning stock data...")
        df = clean_stock_data(df=df)

        today = datetime.now().strftime("%Y-%m-%d")
        output_dir = "data"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{ticker}_{today}.parquet")

        print(f"💾 Saving cleaned data to {output_file}...")
        df.to_parquet(output_file, index=False)

        print(f"✅ Data pipeline completed successfully for ticker: {ticker}")
        print(df.head())

        return df
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    df = run_pipeline()
