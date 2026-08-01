import json
import uuid
from pathlib import Path
from typing import List, Optional

from .models import Expense, ExpenseCreate

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.json"


def _ensure_data_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")


def _read_all() -> List[dict]:
    _ensure_data_file()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def _write_all(expenses: List[dict]) -> None:
    _ensure_data_file()
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2, default=str)


def add_expense(expense: ExpenseCreate) -> Expense:
    expenses = _read_all()
    new_expense = Expense(id=str(uuid.uuid4()), **expense.model_dump())
    expenses.append(json.loads(new_expense.model_dump_json()))
    _write_all(expenses)
    return new_expense


def get_all_expenses(category: Optional[str] = None) -> List[Expense]:
    expenses = _read_all()
    if category:
        expenses = [e for e in expenses if e["category"].lower() == category.lower()]
    return [Expense(**e) for e in expenses]


def delete_expense(expense_id: str) -> bool:
    expenses = _read_all()
    filtered = [e for e in expenses if e["id"] != expense_id]
    if len(filtered) == len(expenses):
        return False
    _write_all(filtered)
    return True


def get_totals(category: Optional[str] = None) -> dict:
    expenses = _read_all()
    if category:
        total = sum(e["amount"] for e in expenses if e["category"].lower() == category.lower())
        return {"category": category, "total": round(total, 2)}

    overall_total = round(sum(e["amount"] for e in expenses), 2)
    by_category: dict = {}
    for e in expenses:
        by_category[e["category"]] = round(by_category.get(e["category"], 0) + e["amount"], 2)
    return {"overall_total": overall_total, "by_category": by_category}
