from drishtee.db.models import Tender, UserSME, BankDetails, UserSHG
from drishtee.db.base import session_scope
from datetime import datetime

with session_scope() as session:
    bank_details = BankDetails(
        "ajkdsjf", "dshfsdif"
    )
    # user_sme = session.query(UserSME).filter(UserSME.id == 1).all()[0]
    # new_tender = Tender("created", "dsakjfh", [], [], new_user_sme)
    new_user_shg = UserSHG("djsfh", "sdfhdsisdhf", "hdsfghj", "98068476", "98347598", "jshfjdshf", "random", "837429", "100", "https://google.com", bank_details)
    session.add(new_user_shg)
    session.add(bank_details)
