import json
from drishtee.db.base import session_scope
from logging import getLogger
from drishtee.db.models import Tender, Media, Milestone, UserSME

LOG = getLogger(__name__)

class MilestoneService:
    @staticmethod
    def mark_completed(id_):
        with session_scope() as session:
            milestone = session.query(Milestone).filter(Milestone.id == id_).update({Milestone.status: "completed"}, synchronize_session = False)
            return {"success": True}, 200
            