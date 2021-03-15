import json
from drishtee.db.base import session_scope
from logging import getLogger
from drishtee.db.models import Tender, Media, Milestone, UserSME

LOG = getLogger(__name__)

def format_response(session, tender: Tender):
    media = session.query(Media).filter(Media.tender_id == tender.id).all()
    milestones = session.query(Milestone).filter(Milestone.tender_id == tender.id).all()

    return {
        "id": tender.id,
        "state": tender.state,
        "description": tender.description,
        "media": [
            {"uri": m.uri, "type": m.uri} for m in media
        ],
        "milestones": [
            {
                "description": mi.description, 
                "status": mi.status, 
                "media": [
                    {
                        "uri": mmedia.uri, 
                        "type": mmedia.type
                    } for mmedia in mi.media
                ]
            } for mi in milestones
        ],
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
    def create_tender(sme_id, description, media, milestones):
        with session_scope() as session:
            user_sme = session.query(UserSME).filter(UserSME.id == sme_id).all()[0]
            media_obj = []
            milestone_obj = []
            for m in media:
                new_media = Media(m["uri"], m["type"])
                media_obj.append(new_media)
                session.add(new_media)
            for milestone in milestones:
                milestone_media = []
                for milestone_m in milestone["media"]:
                    new_mile_media = Media(m["uri"], m["type"])
                    milestone_media.append(new_mile_media)
                    session.add(new_mile_media)
                session.flush()
                new_milestone = Milestone(milestone["description"], "pending", milestone_media)
            session.flush()
            new_tender = Tender("created", description, media_obj, milestone_obj, user_sme)
            if new_tender:
                session.add(new_tender)
                return format_response(session, new_tender), 200
            return {"success": False}, 400
                
