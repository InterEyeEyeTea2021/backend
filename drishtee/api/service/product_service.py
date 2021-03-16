import json
from drishtee.db.base import session_scope
from logging import getLogger

import drishtee.db.models as models

LOG = getLogger(__name__)


def format_response(session, product):
    return {
        "product_id": product.id,
        "name": product.name,
        "description": product.description,
        "image_uri": product.image_uri,
        "min_size": product.min_size,
        "price": product.price,
        "shg_id": product.shg_id,
    }


class ProductService:

    @staticmethod
    def create_product(data, username):
        try:
            with session_scope() as session:
                user = session.query(models.UserSHG).filter(
                    models.UserSHG.username == username).first()
                if not user:
                    resp = {
                        'status': 'fail',
                        'message': 'SHG does not exist'
                    }
                    return resp, 400

                product = models.Product(data.get("name"), data.get(
                    "description"), data.get("image_uri"), data.get("min_size"), data.get("price"), user)

                session.add(product)
                resp = {
                    'status': 'success',
                    'message': 'Product added successfully'
                }
                return resp, 200

        except BaseException:
            LOG.error("Couldn't create product", exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def delete_product(id, username):
        with session_scope() as session:
            product = session.query(models.Product).filter(
                models.Product.id == id).first()
            if not product:
                resp = {
                    'status': 'fail',
                    'message': 'Product not found'
                }
                return resp, 400

            if (product.shg.username != username):
                resp = {
                    'status': 'fail',
                    'message': 'Not Authorized'
                }
                return resp, 401

            session.delete(product)
            resp = {
                'status': 'success',
                'message': 'Product Deleted'
            }
            return resp, 200

    @staticmethod
    def edit_product(id, data, username):
        with session_scope() as session:
            product = session.query(models.Product).filter(
                models.Product.id == id).first()
            if not product:
                resp = {
                    'status': 'fail',
                    'message': 'Product not found'
                }
                return resp, 400

            if (product.shg.username != username):
                resp = {
                    'status': 'fail',
                    'message': 'Not Authorized'
                }
                return resp, 401

            for k, v in data.items():
                if k == "id":
                    continue
                session.query(models.Product).filter(models.Product.id == id).update(
                    {k: v}, synchronize_session=False)

        resp = {
            'status': 'success',
            'message': 'Product Updated'
        }
        return resp, 200

    @ staticmethod
    def get_product_id(id):
        with session_scope() as session:
            product = session.query(models.Product).filter(
                models.Product.id == id).first()
            if not product:
                resp = {
                    'status': 'fail',
                    'message': 'Product not found'
                }
                return resp, 400

            resp = format_response(session, product)
            return resp, 200

    @ staticmethod
    def get_all_orders():
        with session_scope() as session:
            products = session.query(models.Product).all()
            resp = [format_response(session, product) for product in products]
            return resp, 200

    @ staticmethod
    def get_product_shg_id(id):
        with session_scope() as session:
            products = session.query(models.Product).filter(
                models.Product.shg_id == id).all()
            resp = [format_response(session, product) for product in products]
            return resp, 200
