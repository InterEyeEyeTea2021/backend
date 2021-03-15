import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)

class MilestoneService:
    @staticmethod
    def mark_completed(id_):
        with session_scope() as session:
            milestone = session.query(models.Milestone).filter(models.Milestone.id == id_).update({models.Milestone.status: "completed"}, synchronize_session = False)
            return {"success": True}, 200
