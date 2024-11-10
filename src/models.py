from sqlalchemy import Column, Integer, String, Float, Date
from src.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True)
    subcategory = Column(String, index=True, nullable=True)
    amount = Column(Float)
    wallet = Column(String, index=True)
    status = Column(String, index=True)
