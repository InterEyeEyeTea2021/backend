from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class BankDetails(Base):
    __tablename__ = "bank_details"

    id = Column(Integer, primary_key=True)
    ifsc_code = Column("ifsc_code", String(32))
    account_no = Column("account_no", String(32))

    def __init__(self, ifsc_code, account_no):
        self.ifsc_code = ifsc_code
        self.account_no = account_no
