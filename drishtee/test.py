from drishtee.db.models import Tender, UserSME, BankDetails, UserSHG
from drishtee.db.base import session_scope
from datetime import datetime

with session_scope() as session:
    bank_details = BankDetails(
        "hjdsfg", "hkjdsgf"
    )
    new_user_sme = UserSME(
        "name", "username", "password", "phone", "WAContact", "industry_type", bank_details
    )
    # user_sme = session.query(UserSME).filter(UserSME.id == 1).all()[0]
    # new_tender = Tender("created", "dsakjfh", [], [], new_user_sme)
    # new_user_shg = UserSHG("dsuyihfkjhf", "aisuhd", "adsfuhiua", "2345", "random", "23", "34", bank_details)
    session.add(new_user_sme)
    session.add(bank_details)