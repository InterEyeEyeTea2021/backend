from flask import abort, request
from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, get_jwt_identity, verify_jwt_in_request, jwt_required, get_jwt

from drishtee.api.service.product_service import ProductService
from drishtee.api.dto import ProductDto

product_ns = ProductDto.ns
new_product = ProductDto.new_product
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)


@product_ns.route("/")
class CompleteOrder(Resource):
    @product_ns.doc("Create a new product")
    @product_ns.expect(new_product)
    @jwt_required(optional=True)
    def post(self):
        current_identity = get_jwt_identity()
        claims = get_jwt()
        if not current_identity:
            response_object = {
                'status': 'fail',
                'message': 'Not Authorized'
            }
            return response_object, 401

        if claims['user_type'] != "SHG":
            response_object = {
                'status': 'fail',
                'message': 'Not SHG User'
            }
            return response_object, 401

        username = current_identity
        return ProductService.create_product(request.json, username)


@product_ns.route("/all")
class CompleteOrder(Resource):
    @product_ns.doc("Fetch all products")
    def get(self):
        resp = ProductService.get_all_orders()
        return resp


@product_ns.route("/<id>")
class CompleteOrder(Resource):
    @product_ns.doc("Fetch product by id")
    def get(self, id):
        resp = ProductService.get_product_id(id)
        return resp

    @product_ns.doc("Delete product by ID")
    @jwt_required(optional=True)
    def delete(self, id):
        current_identity = get_jwt_identity()
        claims = get_jwt()
        if not current_identity:
            response_object = {
                'status': 'fail',
                'message': 'Not Authorized'
            }
            return response_object, 401

        if claims['user_type'] != "SHG":
            response_object = {
                'status': 'fail',
                'message': 'Not SHG User'
            }
            return response_object, 401

        username = current_identity
        resp = ProductService.delete_product(id, username)
        return resp

    @product_ns.doc("Delete product by ID")
    @jwt_required(optional=True)
    def put(self, id):
        current_identity = get_jwt_identity()
        claims = get_jwt()
        if not current_identity:
            response_object = {
                'status': 'fail',
                'message': 'Not Authorized'
            }
            return response_object, 401

        if claims['user_type'] != "SHG":
            response_object = {
                'status': 'fail',
                'message': 'Not SHG User'
            }
            return response_object, 401

        username = current_identity
        resp = ProductService.edit_product(id, request.json, username)
        return resp


@product_ns.route("/shg/<id>")
class CompleteOrder(Resource):
    @product_ns.doc("Fetch products by shg ID")
    def get(self, id):
        resp = ProductService.get_product_shg_id(id)
        return resp
