from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint
from datetime import datetime

from drishtee.db.base import Base

class UserSME(Base):
    
    __tablename__ = "user_sme"

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)
    
    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    password = Column("password", String(32), nullable=False)
    phone = Column("phone", String(13))
    
    industry_type = Column("industry_type", String(32))
    
    bank_details_id = Column("bank_details_id", ForeignKey("bank_details.id"))
    bank_details = relationship("BankDetails")

    def __init__(self, name, username, password, phone, industry_type, bank_details=None):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.industry_type = industry_type
        self.bank_details = bank_details
        self.created_at = datetime.now()
    
class UserSHG(Base):

    __tablename__ = "user_shg"

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
    bank_details = relationship("BankDetails")

    def __init__(self, name, username, password, phone, industry_type, prod_capacity, order_size, bank_details=None):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.industry_type = industry_type
        self.prod_capacity = prod_capacity
        self.order_size = order_size
        self.bank_details = bank_details
        self.created_at = datetime.now()


class UserSHGMember(Base):
    __tablename__ = "user_shg_member"

    id = Column(Integer, primary_key=True)
    
    name = Column("name", String(32))
    password = Column("password", String(32), nullable=False)
    aadhar_details = Column("aadhar_details", String(32))
    contact = Column("contact", String(32))
    skills = Column("skills", String(32))
    
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )

    def __init__(self, name, password, aadhar_details, contact, skills, shg):
        self.name = name
        self.password = password
        self.aadhar_details = aadhar_details
        self.contact = contact
        self.skills = skills
        self.shg = shg

class PrevProjects(Base):

    __tablename__ = "prev_projects"
    
    id = Column(Integer, primary_key=True)
    description = Column("description", String(64))
    tags = Column("tags", String(32))
    skills = Column("skills", String(32))
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )

    def __init__(description, tags, skills, shg):
        self.description = description
        self.tags = tags
        self.skills = skills
        self.shg = shg