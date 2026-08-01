from datetime import date
from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(gt=0, description="Expense amount, must be positive")
    category: str
    date: date


class Expense(ExpenseCreate):
    id: str
