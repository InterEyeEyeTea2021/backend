from drishtee.api.dto import AuthDto
from drishtee.api.service.auth_service import AuthService
from flask import abort, request
from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from flask_login import current_user, login_required

auth_ns = AuthDto.ns
user_auth = AuthDto.user_auth


@auth_ns.route("/login")
class LoginUser(Resource):
    @auth_ns.doc("Login an existing user")
    @auth_ns.expect(user_auth)
    def post(self):
        data = request.json

        if data['user_type'] == "SHG":
            resp = AuthService.login_user_SHG(data)
        elif data['user_type'] == "SME":
            resp = AuthService.login_user_SME(data)
        else:
            return {'success': False}, 400

        if resp[1] != 200:
            return resp
        else:
            access_token = create_access_token(identity=resp[0]['username'])
            refresh_token = create_refresh_token(identity=resp[0]['username'])

            resp[0]['access_token'] = access_token
            resp[0]['refresh_token'] = refresh_token

            return resp


@auth_ns.route('/refreshToken')
class RefereshJWTToken(Resource):
    @login_required
    def post(self):
        try:
            token = request.headers['Authorization']
            user_id = decode_token(token)
            username = user_id['identity']
            response_object = {
                'username': username,
                'access_token': create_access_token(identity=username),
                'refresh_token': create_refresh_token(identity=username)
            }
            return response_object, 200

        except BaseException:
            response_object = {
                'status': 'fail',
                'message': 'Could not refresh token. '
            }
            return response_object, 500
