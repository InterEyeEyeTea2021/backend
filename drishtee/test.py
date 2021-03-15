from drishtee.db.models import Tender, UserSME, BankDetails, UserSHG
from drishtee.db.base import session_scope

with session_scope() as session:
    user_sme = session.query(UserSME).filter(UserSME.id == 1).all()[0]
    new_tender = Tender("created", "dsakjfh", [], [], user_sme)
    session.add(new_tender)