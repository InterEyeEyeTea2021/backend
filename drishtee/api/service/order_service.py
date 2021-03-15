import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)

class OrderService:
    @staticmethod
    def complete_order(order_id):
        with session_scope() as session:
            order = session.query(models.Order).filter(models.Order.id == order_id).update({models.Order.state: "completed"}, synchronize_session = False)
            return {"success": True}, 200