from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
import src.models as models
import src.crud as crud
import src.schemas as schemas
from datetime import date
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


# Dependência de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD completo
@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

@app.get("/transactions/", response_model=list[schemas.Transaction])
def read_transactions(
    skip: int = 0, 
    limit: int = 10, 
    start_date: Optional[date] = None,  # Parâmetro de data inicial (opcional)
    end_date: Optional[date] = None,    # Parâmetro de data final (opcional)
    db: Session = Depends(get_db)
):
    return crud.get_transactions(db, skip=skip, limit=limit, start_date=start_date, end_date=end_date)

@app.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@app.put("/transactions/{transaction_id}", response_model=schemas.Transaction)
def update_transaction(transaction_id: int, transaction: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    return crud.update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)

@app.delete("/transactions/{transaction_id}", response_model=schemas.Transaction)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db=db, transaction_id=transaction_id)

# Endpoint para cálculo de incomes, expenses e rest
@app.get("/summary/")
def calculate_summary(start_date: Optional[date] = None, end_date: Optional[date] = None, db: Session = Depends(get_db)):
    return crud.calculate_summary(db=db, start_date=start_date, end_date=end_date)
