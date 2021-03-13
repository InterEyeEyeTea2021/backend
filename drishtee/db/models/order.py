from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base

class Order(Base):

    id = Column(Integer, primary_key=True)
    state = Column("state", String(32))
    description = Column("description", String(64))
    
    milestones = relationship("Milestone")
    
    sme_id = Column("sme_id", ForeignKey("user_sme.id"))
    sme = relationship(
        "UserSME", backref=backref("user_sme", uselist=False)
    )

    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG", backref=backref("user_shg", uselist=False)
    )

    contract_id = Column("contract_id", ForeignKey("media.id"))
    contract = relationship(
        "Media", backref=backref("media", uselist=False)
    )