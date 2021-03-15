from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.service.order_service import OrderService
from drishtee.api.dto import OrderDto

order_ns = OrderDto.ns
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)

@order_ns.route("/completeOrder")
class CompleteOrder(Resource):
    @order_ns.doc("Complete order by ID")
    @order_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return OrderService.complete_order(args["id"])
        return {"success": False}, 400