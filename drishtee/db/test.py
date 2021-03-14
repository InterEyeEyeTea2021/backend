from drishtee.db.models import UserSME
from drishtee.db.base import session_scope
from datetime import datetime

with session_scope() as session:
    new_user = UserSME("random", "random", "random", "1234567890", "bakchodi", None)
    session.add(new_user)

user = session.query(UserSME).first()
print(user)