from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from drishtee.db.base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(128))
    description = Column("description", String(512))
    image_uri = Column("image_uri", String(128))
    min_size = Column("min_size", String(128))
    price = Column("price", String(128))

    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship("UserSHG")

    def __init__(self, name, description, image_uri=None, min_size=None, price=None, shg=None):
        self.name = name
        self.description = description
        self.image_uri = image_uri
        self.min_size = min_size
        self.price = price
        self.shg = shg
