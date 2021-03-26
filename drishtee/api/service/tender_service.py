import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models


LOG = getLogger(__name__)


def format_bid(session, bid):
    return {
        "id": bid.id,
        "amount": bid.bid_amount,
        "shg_id": bid.shg_id,
        "tender_id": bid.tender_id
    }


def format_response(session, tender):
    media = session.query(models.Media).filter(
        models.Media.tender_id == tender.id).all()
    milestones = session.query(models.Milestone).filter(
        models.Milestone.tender_id == tender.id).all()

    return {
        "id": tender.id,
        "name": tender.name,
        "state": tender.state,
        "description": tender.description,
        "media": [
            {"uri": m.uri, "type": m.type_} for m in media
        ],
        "milestones": [
            {
                "id": mi.id,
                "name": mi.name,
                "description": mi.description,
                "status": mi.status,
                "media": [
                    {
                        "uri": mmedia.uri,
                        "type": mmedia.type_
                    } for mmedia in mi.media
                ]
            } for mi in milestones
        ],
        "plan_uri": tender.plan_uri,
        "sme": {
            "id": tender.sme_id,
            "name": tender.sme.name,
            "profile_image_uri": tender.sme.image_uri,
            "phone": tender.sme.phone
        },
        "bids": [format_bid(session, bid) for bid in tender.bids]
    }


class TenderService:

    @staticmethod
    def get_tender_by_id(id_):
        with session_scope() as session:
            tender = session.query(models.Tender).filter(
                models.Tender.id == id_).all()
            if len(tender) > 0:
                data = {
                    "success": True,
                    "data": format_response(session, tender[0])
                }
                return data, 200
            return {"success": False}, 404

    @staticmethod
    def create_tender(name, sme_id, description, media, milestones, plan_uri):
        with session_scope() as session:
            user_sme = session.query(models.UserSME).filter(
                models.UserSME.id == sme_id).first()
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

                new_milestone = models.Milestone(milestone["name"],
                                                 milestone["description"], "pending", milestone_media)
                milestone_obj.append(new_milestone)
                session.add(new_milestone)
            new_tender = models.Tender(
                name, "created", description, media_obj, milestone_obj, user_sme, plan_uri)
            if new_tender:
                session.add(new_tender)
                response_data = {
                    "success": True,
                    "data": format_response(session, new_tender)
                }
                return response_data, 200
            return {"success": False}, 400

    @staticmethod
    def get_sme_tenders(sme_id):
        with session_scope() as session:
            tenders = session.query(models.Tender).filter(
                models.Tender.sme_id == sme_id).all()
            return [format_response(session, t) for t in tenders], 200

    @staticmethod
    def get_all_tenders():
        with session_scope() as session:
            all_tenders = session.query(models.Tender).all()
            return [format_response(session, t) for t in all_tenders], 200
