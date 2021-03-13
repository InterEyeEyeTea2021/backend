from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint

from drishtee.db.base import Base

class UserSME(Base):
    
    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)
    
    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    password = Column("password", String(32), nullable=False)
    phone = Column("phone", String(13))
    
    industry_type = Column("industry_type", String(32))
    
    bank_details_id = Column("bank_details_id", ForeignKey("bank_details.id"))
    bank_details = relationship(
        "BankDetails", backref=backref("user_sme", uselist=False)
    )
    
class UserSHG(Base):

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)
    
    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    password = Column("password", String(32), nullable=False)
    phone = Column("phone", String(13))
    
    industry_type = Column("industry_type", String(32))
    prod_capacity = Column("prod_capacity", String(32))
    order_size = Column("order_size", String(32))
    
    bank_details_id = Column("bank_details_id", ForeignKey("bank_details.id"))
    bank_details = relationship(
        "BankDetails", backref=backref("user_sme", uselist=False)
    )

class UserSHGMember(Base):

    id = Column(Integer, primary_key=True)
    
    name = Column("name", String(32))
    password = Column("password", String(32), nullable=False)
    aadhar_details = Column("aadhar_details", String(32))
    contact = Column("contact", String(32))
    skills = Column("skills", String(32))
    
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG", backref=backref("user_sme", uselist=False)
    )

class PrevProjects(Base):
    
    id = Column(Integer, primary_key=True)
    description = Column("description", String(64))
    tags = Column("tags", String(32))
    skills = Column("skills", String(32))
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG", backref=backref("user_shg", uselist=False)
    )