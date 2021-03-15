from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.dto import MilestoneDto
from drishtee.api.service.milestone_service import MilestoneService

milestone_ns = MilestoneDto.ns
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)


@milestone_ns.route("/markComplete")
class CompleteMilestone(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    @milestone_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        print(args)
        if args["id"]:
            return MilestoneService.mark_completed(args["id"])
        return {"success": False}, 400