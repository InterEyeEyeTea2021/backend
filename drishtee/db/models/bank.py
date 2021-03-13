from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base

class BankDetails(Base):
    
    id = Column(Integer, primary_key=True)
    ifsc_code = Column("ifsc_code", String(32))
    account_no = Column("account_no", String(32))