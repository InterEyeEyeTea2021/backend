import json
from drishtee.db.base import session_scope
from logging import getLogger
from drishtee.db.models import Tender, Media, Milestone, UserSME

LOG = getLogger(__name__)

def format_response(session, tender: Tender):
    # media = session.query(Media).filter(Media.tender_id == tender.id).all()
    # milestones = session.query(Milestone).filter(Milestone.tender_id == tender.id).all()

    return {
        "id": tender.id,
        "state": tender.state,
        "description": tender.description,
        "media": [],
        "milestones": [],
        "sme": {
            "id": tender.sme_id,
            "name": tender.sme.name
        } 
    }

class TenderService:

    @staticmethod
    def get_tender_by_id(id_):
        with session_scope() as session:
            tender = session.query(Tender).filter(Tender.id == id_).all()
            if tender:
                data = {
                    "success": True,
                    "tender": format_response(session, tender[0])
                }
                return data, 200
            return {"success": False}, 404

    @staticmethod
    def create_tender(sme_id, description):
        with session_scope() as session:
            user_sme = session.query(UserSME).filter(UserSME.id == sme_id).all()[0]
            new_tender = Tender("created", description, [], [], user_sme)
            if new_tender:
                session.add(new_tender)
                return format_response(new_tender), 200
            return {"success": False}, 400
                
