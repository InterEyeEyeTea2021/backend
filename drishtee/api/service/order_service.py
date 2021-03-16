import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)

def format_response(session, order):
    return {
        "order_id": order.id,
        "state": order.state,
        "description": order.description,
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
            } for mi in order.milestones
        ],
        "sme_id": order.sme_id,
        "shg_id": order.shg_id,
        "contract": order.contract[0].uri
    }

class OrderService:
    @staticmethod
    def complete_order(order_id):
        with session_scope() as session:
            order = session.query(models.Order).filter(models.Order.id == order_id).update({models.Order.state: "completed"}, synchronize_session = False)
            return {"success": True}, 200

    def get_order(order_id):
        with session_scope() as session:
            order = session.query(models.Order).first()
            if order:
                return {"success": True, "data": format_response(order)}, 200
            return {"success": False}, 404

    @staticmethod
    def get_sme_orders(sme_id):
        with session_scope() as session:
            orders = session.query(models.Order).filter(models.Order.sme_id == sme_id).all()
            return [format_response(session, o) for o in orders], 200

    @staticmethod
    def get_shg_orders(shg_id):
        with session_scope() as session:
            orders = session.query(models.Order).filter(models.Order.shg_id == shg_id).all()
            return [format_response(session, o) for o in orders], 200