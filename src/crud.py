from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models import Transaction
import src.schemas as schemas
from typing import Optional
from datetime import date

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None
):
    query = db.query(Transaction)
    
    # Aplicando o filtro de data antes de limit e offset
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    # Agora aplicamos limit e offset
    query = query.offset(skip).limit(limit)

    return query.all()


def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def update_transaction(db: Session, transaction_id: int, transaction: schemas.TransactionUpdate):
    db_transaction = get_transaction(db, transaction_id)
    if db_transaction:
        for key, value in transaction.dict().items():
            setattr(db_transaction, key, value)
        db.commit()
        db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = get_transaction(db, transaction_id)
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction

def calculate_summary(db: Session, start_date=None, end_date=None):
    query = db.query(Transaction)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)

    incomes = query.filter(Transaction.amount > 0).with_entities(func.sum(Transaction.amount)).scalar() or 0
    expenses = query.filter(Transaction.amount < 0).with_entities(func.sum(Transaction.amount)).scalar() or 0
    rest = incomes + expenses

    return {"incomes": incomes, "expenses": abs(expenses), "rest": rest}
