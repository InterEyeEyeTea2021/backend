from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin

from flask_jwt_extended import decode_token


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from datetime import datetime

from drishtee.manage import login_manager
from drishtee.db.base import Base, session_scope


class UserSME(UserMixin, Base):

    __tablename__ = "user_sme"

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)

    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    password = Column("password", String(32), nullable=False)
    phone = Column("phone", String(13))

    industry_type = Column("industry_type", String(32))

    bank_details_id = Column("bank_details_id", ForeignKey("bank_details.id"))
    bank_details = relationship("BankDetails")

    def __init__(self, name, username, password, phone, industry_type, bank_details=None):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.industry_type = industry_type
        self.bank_details = bank_details
        self.created_at = datetime.now()

    def check_password(self, password):
        return self.password == password
        # return check_password_hash(self.password, password)

    @staticmethod
    @login_manager.user_loader
    def load_user(id):
        with session_scope() as session:
            user = session.query(UserSME).filter(UserSME.id == id).first()
            return user

    @staticmethod
    @login_manager.request_loader
    def load_user_from_request(request):
        print("Yo it reached the login manager")
        try:
            with session_scope() as session:
                token = request.headers.get('Authorization')
                if token:
                    user_id = decode_token(token)
                    username = user_id['identity']
                    user = session.query(UserSME).filter(
                        UserSME.username == username).first()
                    if user:
                        print(user)
                        return user

        except Exception as e:
            return None


class UserSHG(UserMixin, Base):

    __tablename__ = "user_shg"

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", DateTime)

    name = Column("name", String(32), nullable=False)
    username = Column("username", String(32), nullable=False)
    password = Column("password", String(32), nullable=False)
    phone = Column("phone", String(13))

    industry_type = Column("industry_type", String(32))
    prod_capacity = Column("prod_capacity", String(32))
    order_size = Column("order_size", String(32))

    bank_details_id = Column("bank_details_id", ForeignKey("bank_details.id"))
    bank_details = relationship("BankDetails")

    def __init__(self, name, username, password, phone, industry_type, prod_capacity, order_size, bank_details=None):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.industry_type = industry_type
        self.prod_capacity = prod_capacity
        self.order_size = order_size
        self.bank_details = bank_details
        self.created_at = datetime.now()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    @login_manager.user_loader
    def load_user(id):
        with session_scope() as session:
            return session.query(UserSHG).filter(UserSHG.id == id).first()

    @staticmethod
    @login_manager.request_loader
    def load_user_from_request(request):
        try:
            with session_scope() as session:
                token = request.headers.get('Authorization')
                if token:
                    user_id = decode_token(token)
                    username = user_id['identity']
                    user = session.query(UserSHG).filter(
                        UserSHG.username == username).first()
                    if user:
                        return user

        except Exception as e:
            return None


class UserSHGMember(Base):
    __tablename__ = "user_shg_member"

    id = Column(Integer, primary_key=True)

    name = Column("name", String(32))
    password = Column("password", String(32), nullable=False)
    aadhar_details = Column("aadhar_details", String(32))
    contact = Column("contact", String(32))
    skills = Column("skills", String(32))

    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )

    def __init__(self, name, password, aadhar_details, contact, skills, shg):
        self.name = name
        self.password = password
        self.aadhar_details = aadhar_details
        self.contact = contact
        self.skills = skills
        self.shg = shg


class PrevProjects(Base):

    __tablename__ = "prev_projects"

    id = Column(Integer, primary_key=True)
    description = Column("description", String(64))
    tags = Column("tags", String(32))
    skills = Column("skills", String(32))
    shg_id = Column("shg_id", ForeignKey("user_shg.id"))
    shg = relationship(
        "UserSHG"
    )

    def __init__(self, description, tags, skills, shg):
        self.description = description
        self.tags = tags
        self.skills = skills
        self.shg = shg
