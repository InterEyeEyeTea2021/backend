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

@order_ns.route("/getOrder")
class GetOrderById(Resource):
    @order_ns.doc("Get order by ID")
    @order_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return OrderService.get_order(args["id"])
        return {"success": False}, 400

@order_ns.route("/sme")
class GetSMEOrder(Resource):
    @order_ns.doc("Get order by sme ID")
    @order_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return OrderService.get_sme_orders(args["id"])
        return {"success": False}, 400

@order_ns.route("/shg")
class GetSHGOrder(Resource):
    @order_ns.doc("Get order by shg ID")
    @order_ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        if args["id"]:
            return OrderService.get_shg_orders(args["id"])
        return {"success": False}, 400