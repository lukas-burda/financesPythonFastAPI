from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionBase(BaseModel):
    date: date
    title: str
    category: str
    subcategory: Optional[str] = None
    amount: float
    wallet: str
    status: str

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
