import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)


class MilestoneService:
    @staticmethod
    def mark_completed(id_):
        with session_scope() as session:
            milestone = session.query(models.Milestone).filter(models.Milestone.id == id_).update(
                {models.Milestone.status: "completed"}, synchronize_session=False)
            return {"success": True}, 200

    def create_milestone(tender_id, name, description, image_uri):
        with session_scope() as session:
            image = models.Media(image_uri, "image")
            new_milestone = models.Milestone(
                name, description, "created", [image])
            session.flush()
            tender = session.query(models.Tender).filter(
                models.Tender.id == tender_id).first()
            tender.milestones.append(new_milestone)
            return {"success": True, "milestone_id": new_milestone.id}, 200

    def update_milestone(milestone_id, name, description, image_uri, status):
        with session_scope() as session:
            if name:
                session.query(models.Milestone).filter(
                    models.Milestone.id == milestone_id).update({models.Milestone.description: name}, synchronize_session=False)

            if description:
                session.query(models.Milestone).filter(
                    models.Milestone.id == milestone_id).update({models.Milestone.description: description}, synchronize_session=False)

            if image_uri:
                session.query(models.Media).filter(
                    models.Media.milestone_id == milestone_id).update({models.Media.uri: image_uri}, synchronize_session=False)

            if status:
                session.query(models.Media).filter(
                    models.Media.milestone_id == milestone_id).update({models.Milestone.status: status}, synchronize_session=False)

            return {"success": True}, 200
