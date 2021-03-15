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
class CreateTender(resource):
    @tender_ns.doc("Create tender")
    def post(self):
        info = request.json
        