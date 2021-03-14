from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    uri = Column("uri", String(64))
    type_ = Column("type", String(32))

    milestone_id = Column(Integer, ForeignKey("milestone.id"))
    order_id = Column(Integer, ForeignKey("order.id"))
    tender_id = Column(Integer, ForeignKey("tender.id"))

    def __init__(self, uri, type_):
        self.uri = uri
        self.type_ = type_
