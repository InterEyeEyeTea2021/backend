import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)

def format_user(sme):
    return {
        "sme_id": sme.id,
        "name": sme.name,
        "phone": sme.phone,
        "WAContact": sme.WAContact,
        "industry_type": sme.industry_type,
        "image_uri": sme.image_uri
    }

class UserService:
    @staticmethod
    def all_sme():
        with session_scope() as session:
            all_sme = session.query(models.UserSME).all()
            return [format_user(s) for s in all_sme], 200
    
    @staticmethod
    def all_shg():
        with session_scope() as session:
            all_shg = session.query(models.UserSHG).all()
            return [format_user(s) for s in all_shg], 200

    