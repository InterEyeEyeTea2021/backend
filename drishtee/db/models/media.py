from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base

class Media(Base):

    id = Column(Integer, primary_key=True)
    uri = Column("uri", String(64))
    type_ = Column("type", String(32))

    milestone_id = Column(Integer, ForeignKey("milestone.id"))
    tender_id = Column(Integer, ForeignKey("tender.id"))