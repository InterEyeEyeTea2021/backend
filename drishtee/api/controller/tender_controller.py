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
    def post(self):
        try:
            print(request.json)
            info = request.json
            name = info["tender_name"]
            sme_id = info["sme_id"]
            description = info["description"]
            media = info["media"]
            milestones = info["milestones"]
            plan = info["plan"]
            return TenderService.create_tender(name, sme_id, description, media, milestones, plan)
        except KeyError:
            abort(400)


@tender_ns.route("/sme")
class GetSMETenders(Resource):
    @tender_ns.doc("Get tender by sme ID")
    @tender_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return TenderService.get_sme_tenders(args["id"])
        return {"success": False}, 400


@tender_ns.route("/all")
class GetAllTenders(Resource):
    def get(self):
        return TenderService.get_all_tenders()
