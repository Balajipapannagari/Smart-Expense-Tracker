# Smart-Expense-Tracker
A simple REST API to manage personal expenses, built with FastAPI. 


# Smart Expense Tracker API

A simple REST API to manage personal expenses, built with FastAPI. Data is stored in a local JSON file (`data/expenses.json`), no database required.

## Features

- Add an expense (title, amount, category, date)
- View all expenses
- Filter expenses by category
- Get total expenses (overall, by category, or for one category)
- Delete an expense

## Requirements

- Python 3.10+

## Install dependencies

```
pip install -r requirements.txt
```

## Run the server

```
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs (Swagger UI) are available at `http://127.0.0.1:8000/docs`.

## Run the tests

```
pytest tests/ -v
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | List all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/total` | Get overall total + total by category |
| GET | `/expenses/total?category=Food` | Get total for one category |
| DELETE | `/expenses/{id}` | Delete an expense by id |

### Example: Add an expense

```
curl -X POST http://127.0.0.1:8000/expenses \
  -H "Content-Type: application/json" \
  -d '{"title": "Groceries", "amount": 45.50, "category": "Food", "date": "2026-07-01"}'
```

## Project Structure

```
expense-tracker/
  README.md
  AI_NOTES.md
  requirements.txt
  src/
    __init__.py
    main.py        # FastAPI app and routes
    models.py       # Pydantic models
    storage.py      # JSON file read/write logic
  tests/
    test_api.py
  data/
    expenses.json   # created automatically on first run
```
