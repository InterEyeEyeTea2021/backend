from drishtee.db.models import Tender, UserSME, BankDetails, UserSHG
from drishtee.db.base import session_scope

with session_scope() as session:
    bank_details = BankDetails(
        "dsajo", "123456"
    )
    new_user_sme = UserSME(
        "sdfhj", "dsafhjsi", "dsahkjs", "123", "dslkj", bank_details   
    )
    # user_sme = session.query(UserSME).filter(UserSME.id == 1).all()[0]
    # new_tender = Tender("created", "dsakjfh", [], [], new_user_sme)
    session.add(new_user_sme)
    session.add(bank_details)