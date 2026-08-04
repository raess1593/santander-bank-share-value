# santander-bank-share-value

📘 A work-in-progress pipeline to download Santander stock data, clean it, and store it in Parquet files under the `data/` directory.

## ✅ Current status

The project currently performs the following steps:

1. Downloads daily market data using `yfinance`.
2. Cleans the dataframe and normalizes its columns.
3. Saves the result as `data/<ticker>_<date>.parquet`.

## 🧩 Project structure

- `src/scraper.py`: fetches the daily data for the `SAN.MC` ticker.
- `src/transformer.py`: cleans and prepares the dataframe for storage.
- `src/main.py`: orchestrates the full pipeline execution.
- `data/`: directory where generated Parquet files are stored.

## ▶️ Run locally

From the project root:

```bash
uv run src/main.py
```

If the virtual environment is already activated, you can also run:

```bash
python src/main.py
```

## 🐳 Run with Docker

The project can also be executed with Docker Compose:

```bash
docker compose up --build
```

The container mounts the local `data/` directory so the generated files remain available on the host machine.

## 🧪 Code quality

To format the source code:

```bash
make lint
```

## 📦 Requirements

- Python 3.12+
- `uv` for local dependency management
- Docker and Docker Compose if you want to run the project in containers

## 📚 Main dependencies

- `pandas`
- `pyarrow`
- `yfinance`

## 🚀 Next steps

1. Improve the data extraction flow for broader history or higher frequency.
2. Add a more robust persistence layer.
3. Automate the ingestion and storage process end to end.
