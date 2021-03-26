from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Tender(Base):
    __tablename__ = "tender"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(256))
    state = Column("state", String(256))
    description = Column("description", String(256))

    media = relationship("Media")
    milestones = relationship("Milestone")
    bids = relationship("Bid", back_populates="tender")
    sme_id = Column("sme_id", ForeignKey("user_sme.id"))
    sme = relationship("UserSME")

    def __init__(self, name, state, description, media, milestones, sme):
        self.name = name
        self.state = state
        self.description = description
        self.media = media
        self.milestones = milestones
        self.sme = sme
        self.bids = []


class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    bid_amount = Column("bid_amount", Integer)
    tender_id = Column(Integer, ForeignKey("tender.id"))
    tender = relationship("Tender", back_populates="bids")
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship("UserSHG")

    def __init__(self, bid_amount, shg, tender):
        self.bid_amount = bid_amount
        self.shg = shg
        self.tender = tender
