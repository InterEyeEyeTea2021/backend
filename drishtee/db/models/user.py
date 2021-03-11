from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import UniqueConstraint

from drishtee.db.base import Base

class User(Base):
    __tablename__ = "user"
    # Columns
    id = Column(Integer, primary_key=True)
    name = Column("name", String(32), nullable=False)
    facebook_id = Column("facebook_id", String, unique=True)
    image = Column("image", String(160))
    post_count = Column("post_count", Integer)
    liked_count = Column("liked_count", Integer)
    likes_count = Column("likes_count", Integer)
    __table_args__ = (UniqueConstraint("id", "facebook_id", name="user_id"),)

    def __init__(self, name, facebook_id, image):
        self.name = name
        self.facebook_id = facebook_id
        self.image = image
