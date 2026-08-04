# santander-bank-share-value

📘 A work-in-progress project to fetch Santander stock price data and, later on, automate storing it in the cloud.

## 📌 Current status

For now, the project only retrieves daily market data using `yfinance` and prints it to the console. The current goal is to keep the implementation small and clear while the data collection flow is being shaped.

## ▶️ Run it

The script can be executed directly from the project root.

```bash
python src/scraper.py
```

## 📦 Dependencies

The project currently depends on:

- Python 3.12+
- `pandas`
- `yfinance`

## 🚧 Next steps

This README will keep evolving as the project grows:

1. Improve the data extraction flow.
2. Add persistent storage for the retrieved values.
3. Automate the full process end to end.
