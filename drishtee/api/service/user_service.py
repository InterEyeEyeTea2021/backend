import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)

def format_user_sme(sme):
    return {
        "sme_id": sme.id,
        "name": sme.name,
        "phone": sme.phone,
        "WAContact": sme.WAContact,
        "industry_type": sme.industry_type,
        "image_uri": sme.image_uri
    }

def format_user_shg(shg):
    return {
        "shg_id": shg.id,
        "name": shg.name,
        "phone": shg.phone,
        "WAContact": shg.WAContact,
        "industry_type": shg.industry_type,
        "image_uri": shg.image_uri
    }

class UserService:
    @staticmethod
    def all_sme():
        with session_scope() as session:
            all_sme = session.query(models.UserSME).all()
            return [format_user_sme(s) for s in all_sme], 200
    
    @staticmethod
    def all_shg():
        with session_scope() as session:
            all_shg = session.query(models.UserSHG).all()
            return [format_user_shg(s) for s in all_shg], 200

    
