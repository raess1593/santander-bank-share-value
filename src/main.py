import os
from datetime import datetime

from dotenv import load_dotenv

from loader import upload_stock_data_to_s3
from scraper import get_daily_stock_data
from transformer import clean_stock_data


def run_pipeline(s3_bucket_name: str, ticker: str = "SAN.MC") -> None:
    try:
        print(f"🚀 Running data pipeline for ticker: {ticker}")

        print(f"📥 Fetching daily stock data for {ticker}...")
        df = get_daily_stock_data(ticker=ticker)

        print(f"🧹 Cleaning stock data...")
        df = clean_stock_data(df=df)

        today = datetime.now().strftime("%Y-%m-%d")
        output_dir = "data"
        output_name = f"{ticker}_{today}.parquet"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, output_name)

        print(f"📤 Uploading cleaned data to S3 bucket: {s3_bucket_name}...")
        df.to_parquet(output_file, index=False)
        try:
            upload_stock_data_to_s3(file_path=output_file, s3_bucket_name=s3_bucket_name, key_name=output_name)
        except Exception as e:
            print(f"❌ An error occurred while uploading to S3: {e}")
            raise e
        os.remove(output_file)

        print(f"✅ Data pipeline completed successfully for ticker: {ticker}")
        print(df.head())

        return df
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    load_dotenv()

    s3_bucket_name = os.getenv("S3_BUCKET_NAME")
    if not s3_bucket_name:
        print("❌ S3_BUCKET_NAME environment variable is not set.")
    else:
        df = run_pipeline(s3_bucket_name=s3_bucket_name, ticker="SAN.MC")
