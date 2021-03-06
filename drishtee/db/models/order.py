from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(256))
    state = Column("state", String(256))
    description = Column("description", String(256))

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
    tender = relationship("Tender")
    tender_id = Column("tender_id", ForeignKey("tender.id"))
    plan_uri = Column("plan_uri", String(256))

    def __init__(self, name, state, description, milestones, sme, shg, contract, tender, plan_uri):
        self.name = name
        self.state = state
        self.description = description
        self.milestones = milestones
        self.sme = sme
        self.shg = shg
        self.contract = contract
        self.tender = tender
        self.plan_uri = plan_uri
