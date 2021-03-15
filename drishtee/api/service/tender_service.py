import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models


LOG = getLogger(__name__)

def format_response(session, tender):
    media = session.query(models.Media).filter(models.Media.tender_id == tender.id).all()
    milestones = session.query(models.Milestone).filter(models.Milestone.tender_id == tender.id).all()

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
            tender = session.query(models.Tender).filter(models.Tender.id == id_).all()
            if len(tender) > 0:
                data = {
                    "success": True,
                    "data": format_response(session, tender[0])
                }
                return data, 200
            return {"success": False}, 404

    @staticmethod
    def create_tender(sme_id, description, media, milestones):
        with session_scope() as session:
            user_sme = session.query(models.UserSME).filter(models.UserSME.id == sme_id).first()
            media_obj = []
            milestone_obj = []
            for m in media:
                new_media = models.Media(m["uri"], m["type"])
                media_obj.append(new_media)
                session.add(new_media)
            for milestone in milestones:
                milestone_media = []
                for milestone_m in milestone["media"]:
                    new_mile_media = models.Media(m["uri"], m["type"])
                    milestone_media.append(new_mile_media)
                    session.add(new_mile_media)
                session.flush()
                new_milestone = models.Milestone(milestone["description"], "pending", milestone_media)
                session.add(new_milestone)
            session.flush()
            new_tender = models.Tender("created", description, media_obj, milestone_obj, user_sme)
            if new_tender:
                session.add(new_tender)
                response_data = {
                    "success": True,
                    "data": format_response(session, new_tender)
                }
                return response_data, 200
            return {"success": False}, 400

