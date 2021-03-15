"""Register all namespaces and import API's from  controllers."""
from flask import Blueprint
from flask_restx import Api

from drishtee.api.controller.tender_controller import tender_ns

api_bp = Blueprint("api", __name__)

api = Api(
    api_bp,
    title="Flask-RESTPlus common backend for LTT-KGP",
    version="1.0",
    description="a boilerplate for flask restplus web service",
)
api.add_namespace(tender_ns, path="/tender")

# api.add_namespace(feed_ns, path="/v1/feed")
# api.add_namespace(data_ns, path="/v1/data")
# api.add_namespace(health_ns, path="/v1/health")
