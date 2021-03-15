from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    state = Column("state", String(32))
    description = Column("description", String(64))

    milestones = relationship("Milestone", backref="order")

    sme_id = Column("sme_id", ForeignKey("user_sme.id"))
    sme = relationship(
        "UserSME"
    )

    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )
    contract = relationship("Media", backref="order")

    def __init__(self, state, description, milestones, sme, shg, contract):
        self.state = state
        self.description = description
        self.milestones = milestones
        self.sme = sme
        self.shg = shg
        self.contract = contract
