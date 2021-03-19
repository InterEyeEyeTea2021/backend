from drishtee.db.models import Tender, UserSME, BankDetails, UserSHG
from drishtee.db.base import session_scope
from datetime import datetime

with session_scope() as session:
    bank_details = BankDetails(
        "kjdsfhjdshf", "sdhksjhfds"
    )
    # new_user_sme = UserSME(
    #     "name", "username", "password", "phone", "WAContact", "industry_type", "https://google.com", bank_details
    # )
    # user_sme = session.query(UserSME).filter(UserSME.id == 1).all()[0]
    # new_tender = Tender("created", "dsakjfh", [], [], new_user_sme)
    new_user_shg = UserSHG("sdjkfkdsf", "kdajsf", "adsfuhiua", "2345", "random", "sjhfjdshf", "skjdhfkjdsf", "3748", "7459", "https://reddit.com", bank_details)
    session.add(new_user_shg)
    session.add(bank_details)