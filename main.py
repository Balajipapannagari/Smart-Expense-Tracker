from fastapi import FastAPI, HTTPException, Query
from typing import Optional

from .models import Expense, ExpenseCreate
from . import storage

app = FastAPI(title="Smart Expense Tracker API")


@app.post("/expenses", response_model=Expense, status_code=201)
def add_expense(expense: ExpenseCreate):
    return storage.add_expense(expense)


@app.get("/expenses", response_model=list[Expense])
def list_expenses(category: Optional[str] = Query(None, description="Filter by category")):
    return storage.get_all_expenses(category=category)


@app.get("/expenses/total")
def total_expenses(category: Optional[str] = Query(None, description="Get total for a specific category")):
    return storage.get_totals(category=category)


@app.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: str):
    deleted = storage.delete_expense(expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return None
