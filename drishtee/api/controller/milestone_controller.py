from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.dto import MilestoneDto
from drishtee.api.service.milestone_service import MilestoneService

milestone_ns = MilestoneDto.ns
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)



@milestone_ns.route("/create")
class CreateMilestone(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("id", type=int)
    # @milestone_ns.expect(parser)
    def post(self):
        data = request.json
        tender_id = data["tender_id"]
        description = data["description"]
        image_uri = data["image_uri"]
        return MilestoneService.create_milestone(tender_id, description, image_uri)

@milestone_ns.route("/update")
class UpdateMilestone(Resource):
    def post(self):
        data = request.json
        milestone_id = data.get("milestone_id")
        description = data.get("description")
        image_uri = data.get("image_uri")
        status = data.get("status")
        return MilestoneService.update_milestone(milestone_id, description, image_uri, status)