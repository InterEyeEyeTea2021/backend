import json
from drishtee.db.base import session_scope
from logging import getLogger
import drishtee.db.models as models


LOG = getLogger(__name__)


def format_response(session, bid):
    return {
        "amount": bid.bid_amount,
        "shg_id": bid.shg_id,
        "tender_id": bid.tender_id
    }


class BidService:
    @staticmethod
    def create_bid(tender_id, amount, shg_id):
        # print(tender_id, amount, shg_id)
        with session_scope() as session:
            existing_bid = session.query(models.Bid).filter(
                models.Bid.shg_id == shg_id).filter(models.Bid.tender_id == tender_id).all()
            if(len(existing_bid) == 0):
                shg = session.query(models.UserSHG).filter(
                    models.UserSHG.id == shg_id).all()[0]
                tender = session.query(models.Tender).filter(
                    models.Tender.id == tender_id).all()[0]
                new_bid = models.Bid(amount, shg, tender)
                if new_bid:
                    session.add(new_bid)
                    response_data = {
                        "success": True,
                        "data": format_response(session, new_bid)
                    }
                    return response_data
                return {"success": False, "message": "Bid creation failed!"}, 400
            # print(existing_bid[0].tender_id)
            return {"success": False, "message": "Bid exists"}, 400

    @staticmethod
    def get_tender_bids(tender_id):
        with session_scope() as session:
            bids = session.query(models.Bid).filter(
                models.Bid.tender_id == tender_id).all()
            if len(bids) > 0:
                return {
                    "success": True,
                    "data": [format_response(session, b) for b in bids]
                }
            return {"success": False}, 404

    @staticmethod
    def accept_bid(bid_id, contract_uri):
        # TODO: authenticated by SME
        with session_scope() as session:
            bid = session.query(models.Bid).filter(
                models.Bid.id == bid_id).first()
            tender = session.query(models.Tender).filter(
                models.Tender.id == bid.tender_id).first()
            new_contract = models.Media(contract_uri, "image")
            new_order = models.Order(
                tender.name, "created", tender.description, tender.milestones, tender.sme, bid.shg, [
                    new_contract], tender
            )
            session.add(new_order)
            return {"success": True}, 200
        return {"success": False}, 400

    @staticmethod
    def get_shg_bids(shg_id):
        with session_scope() as session:
            bids = session.query(models.Bid).filter(
                models.Bid.shg_id == shg_id).all()
            if len(bids) > 0:
                return {
                    "success": True,
                    "data": [format_response(session, b) for b in bids]
                }
            return {"success": False}, 404
