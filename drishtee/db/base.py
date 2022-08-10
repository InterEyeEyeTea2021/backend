import os
from contextlib import contextmanager
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://ubuntu:ubuntu@5432/grameensetu")
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()


def session_factory():
    from drishtee.db.models import UserSME, UserSHG, PrevProjects, UserSHGMember, BankDetails, Media, Milestone, Order, Tender, Bid

    Base.metadata.create_all(engine)
    return _SessionFactory()


@contextmanager
def session_scope():
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception as e:
        raise
        session.rollback()
    finally:
        session.close()
