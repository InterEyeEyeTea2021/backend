from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base

class Tender(Base):

    id = Column(Integer, primary_key=True)
    state = Column("state", String(32))
    description = Column("description", String(64))
    
    media = relationship("Media")
    milestones = relationship("Milestone")
    sme_id = Column("sme_id", ForeignKey("user_sme.id"))
    sme = relationship(
        "UserSME", backref=backref("user_sme", uselist=False)
    )

class Bid(Base):

    id = Column(Integer, primary_key=True)
    bid_amount = Column("bid_amount", Integer)
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG", backref=backref("user_shg", uselist=False)
    )