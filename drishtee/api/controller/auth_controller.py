from drishtee.api.dto import AuthDto
from drishtee.api.service.auth_service import AuthService
from flask import abort, request
from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, get_jwt_identity, verify_jwt_in_request, jwt_required
from flask_login import current_user, login_required

auth_ns = AuthDto.ns
user_auth = AuthDto.user_auth


def get_identity_if_logedin():
    try:
        verify_jwt_in_request()
        return get_jwt_identity()
    except Exception:
        pass


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
    @jwt_required(optional=True)
    def post(self):
        try:
            current_identity = get_jwt_identity()
            if not current_identity:
                response_object = {
                    'status': 'fail',
                    'message': 'Not Authorized. '
                }
                return response_object, 401

            access_token = create_access_token(identity=current_identity)
            refresh_token = create_refresh_token(identity=current_identity)

            response_object = {
                'username': current_identity,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response_object, 200

        except BaseException:
            response_object = {
                'status': 'fail',
                'message': 'Could not refresh token. '
            }
            return response_object, 500
