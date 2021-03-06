from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.dto import BidDto
from drishtee.api.service.bid_service import BidService

bid_ns = BidDto.ns
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)

@bid_ns.route("/create")
class CreateBid(Resource):
    @bid_ns.doc("Create a new bid")
    def post(self):
        """
        {
            "shg_id": x,
            "amount": x,
            "tender_id": x
        }
        """
        try:
            info = request.json
            shg_id = info["shg_id"]
            amount = info["amount"]
            tender_id = info["tender_id"]
            # print(info)

            return BidService.create_bid(tender_id, amount, shg_id)
        except KeyError:
            return {"success": False}, 400

@bid_ns.route("/getTenderBids")
class TenderBids(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    @bid_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return BidService.get_tender_bids(args["id"])
        return {"success": False}, 400

@bid_ns.route("/acceptBid")
class AcceptBid(Resource):
    def post(self):
        info = request.json
        id_ = info.get("id")
        contract_uri = info.get("contract_uri")
        if id_:
            return BidService.accept_bid(id_, contract_uri)
        return {"success": False}, 400

@bid_ns.route("/shg")
class GetSHGBids(Resource):
    @bid_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return BidService.get_shg_bids(args["id"])
        return {"success": False}, 400
