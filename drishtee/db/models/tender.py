from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Tender(Base):
    __tablename__ = "tender"

    id = Column(Integer, primary_key=True)
    state = Column("state", String(32))
    description = Column("description", String(64))

    media = relationship("Media")
    milestones = relationship("Milestone")
    sme_id = Column("sme_id", ForeignKey("user_sme.id"))
    sme = relationship("UserSME")

    def __init__(self, state, description, media, milestones, sme):
        self.state = state
        self.description = description
        self.media = media
        self.milestones = milestones
        self.sme = sme


class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    bid_amount = Column("bid_amount", Integer)
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )

    def __init__(bid_amount, shg):
        self.bid_amount = bid_amount
        self.shg = shg
