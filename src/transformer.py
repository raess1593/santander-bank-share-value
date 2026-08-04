import pandas as pd


def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    cleaned_df = cleaned_df.reset_index()
    cleaned_df["Date"] = cleaned_df["Date"].dt.date
    cleaned_df.columns = cleaned_df.columns.str.replace(" ", "_").str.lower()
    cleaned_df = cleaned_df[["date", "open", "high", "low", "close", "volume"]]

    return cleaned_df


if __name__ == "__main__":
    from scraper import get_daily_stock_data

    df = get_daily_stock_data("SAN.MC")
    cleaned_df = clean_stock_data(df)
    print(cleaned_df)
