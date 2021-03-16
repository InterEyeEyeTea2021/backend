from flask import abort, request
from flask_restx import Namespace, Resource, reqparse

from drishtee.api.dto import UserDto
from drishtee.api.service.user_service import UserService

user_ns = UserDto.ns

@user_ns.route("/sme")
class AllSME(Resource):
    def get(self):
        return UserService.all_sme()
  
@user_ns.route("/shg")
class AllSME(Resource):
    def get(self):
        return UserService.all_shg()