from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Milestone(Base):

    __tablename__ = "milestone"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(64))
    description = Column("description", String(256))
    status = Column("status", String(256))

    media = relationship("Media", backref="milestone")

    tender_id = Column(Integer, ForeignKey("tender.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))

    def __init__(self, name, description, status, media=None):
        self.name = name
        self.description = description
        self.status = status
        self.media = media
