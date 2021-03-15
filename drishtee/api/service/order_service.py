import json
from drishtee.db.base import session_scope
from logging import getLogger
from drishtee.db.models import Tender, Media, Milestone, UserSME, UserSHG, Bid, Order

LOG = getLogger(__name__)

class OrderService:
    @staticmethod
    def complete_order(order_id):
        with session_scope() as session:
            order = session.query(Order).filter(Order.id == order_id).update({Order.state: "completed"}, synchronize_session = False)
            return {"success": True}, 200