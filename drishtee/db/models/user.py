from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint

from drishtee.db.base import Base

class UserSME(Base):
    __tablename__ = "user_sme"
    
    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)
    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    phone = Column("phone", String(13))
    industry_type = Column("industry_type", String(32))
    bank_details_id = Column("bank_details_id", ForeignKey("User_bank_details.id"))

    bank_details = relationship(
        "BankDetails", backref=backref("user_sme", uselist=False)
    )
    
class UserSHG(Base):
    __tablename__ = "user_shg"

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)
    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    phone = Column("phone", String(13))
    industry_type = Column("industry_type", String(32))
    bank_details_id = Column("bank_details_id", ForeignKey("User_bank_details.id"))
    prod_capacity = Column("prod_capacity", String(32))
    order_size = Column("order_size", String(32))

    bank_details = relationship(
        "BankDetails", backref=backref("user_sme", uselist=False)
    )
