import json
from drishtee.db.base import session_scope
from logging import getLogger
from drishtee.db.models import Tender, Media, Milestone, UserSME, UserSHG, Bid

LOG = getLogger(__name__)

def format_response(session, bid: Bid):
    return {
        "amount": bid.bid_amount,
        "shg_id": bid.shg_id,
        "tender_id": bid.tender_id
    }


class BidService:
    @staticmethod
    def create_bid(tender_id, amount, shg_id):
        with session_scope() as session:
            existing_bid = session.query(Bid).filter(Bid.shg_id == shg_id and Bid.tender_id == tender_id).all()
            if not existing_bid:
                shg = session.query(UserSHG).filter(UserSHG.id == shg_id).all()[0]
                tender = session.query(Tender).filter(Tender.id == tender_id).all()[0]
                new_bid = Bid(amount, shg, tender)
                if new_bid:
                    session.add(new_bid)
                    response_data = {
                        "success": True,
                        "data": format_response(session, new_bid)
                    }
                    return response_data
                return {"success": False, "message": "Bid creation failed!"}, 400
            return {"success": False, "message": "Bid exists"}, 400 

    @staticmethod
    def get_tender_bids(tender_id):
        with session_scope() as session:
            bids = session.query(Bid).filter(Bid.tender_id == tender_id).all()
            if bids:
                return {
                    "success": True,
                    "data": [format_response(session, b) for b in bids]
                }
            return {"success": False}, 404
