import os

from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.dto import DataDto
from drishtee.api.service.data_service import DataService

data_ns = DataDto.ns

parser = reqparse.RequestParser()



@data_ns.route("/post")
@data_ns.header("whoami")
class SampleEndpoint(Resource):
    @data_ns.doc("Sample")
    def post(self):
        response, status = DataService.UpdateOrCreate(request.data)
        if status != 200:
            abort(403, response)
        else:
            return response, status

