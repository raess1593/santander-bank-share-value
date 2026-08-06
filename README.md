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

## ☁️ Optional: S3 / Cloud storage (configuration)

The project can be extended to upload generated Parquet files to an S3 bucket. The repository includes an example environment file with the variables commonly needed for S3 configuration.

- See the example file: [`.env.example`](.env.example#L1-L4)

Example variables (from `.env.example`):

```
TICKER=SAN.MC
S3_BUCKET_NAME=my-s3-bucket-name
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
```

Notes:

- The current codebase saves files to the local `data/` directory. Uploading to S3 is optional and requires implementing an upload step (e.g. using `boto3` or another client) that reads the above environment variables.
- If you add S3 upload functionality, prefer to keep credentials out of source control and use environment variables or a secrets manager.

If you want, I can add a minimal S3 upload helper and example integration into `src/main.py` on the `s3` branch.
