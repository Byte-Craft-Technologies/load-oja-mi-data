# load-oja-mi-data

Data loading script that imports a product catalog from an Excel file into PostgreSQL.

## What it does

Reads categories, products, and variations (including embedded images) from an Excel file and inserts them into a PostgreSQL database — skipping rows that already exist.

## Stack

- **Python** — pandas, openpyxl, psycopg2
- **PostgreSQL** — connection pooling via `psycopg2.SimpleConnectionPool`

## Environment variables

Required:
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `SERVICE_ACCOUNT_FILE`

Optional:
- `SERVER_ADDRESS` — base URL for image URLs 
- `EXCEL_FILE` — path to the Excel file (default: `output_with_images.xlsx`)

Place your Excel file in the project root and run:

```bash
python main.py
```
