from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.service.tender_service import TenderService
from drishtee.api.dto import TenderDto

tender_ns = TenderDto.ns
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)

@tender_ns.route("/id")
class TenderById(Resource):
    @tender_ns.doc("Get tender by ID")
    @tender_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return TenderService.get_tender_by_id(args["id"])
        return {"success": False}, 400

@tender_ns.route("/create")
class CreateTender(Resource):
    @tender_ns.doc("Create tender")
    def post(self):
        """
        {
            "sme_id": x,
            "description": xx,
            "media": [
                {
                    "uri": "xxxx",
                    "type": image/video 
                },
            ]
            "milestones": [
                {
                    "description": "XX",
                    "media": []
                }
            ]
        }
        """
        try:
            info = request.json
            sme_id = info["sme_id"]
            description = info["description"]
            media = info["media"]
            milestones = info["milestones"]
            return TenderService.create_tender(sme_id, description, media, milestones)
        except KeyError:
            abort(400)

        