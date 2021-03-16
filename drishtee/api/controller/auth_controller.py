from drishtee.api.dto import AuthDto
from drishtee.api.service.auth_service import AuthService
from flask import abort, request
from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, get_jwt_identity, verify_jwt_in_request, jwt_required, get_jwt

auth_ns = AuthDto.ns
user_auth = AuthDto.user_auth
new_sme = AuthDto.new_sme
new_shg = AuthDto.new_shg


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
    @jwt_required(optional=True)
    def post(self):
        current_identity = get_jwt_identity()
        if current_identity is not None:
            resp = {
                'status': 'fail',
                'message': 'Already logged in'
            }
            return resp, 401

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
            additional_claims = {
                'user_type': resp[0]['user_type']
            }
            access_token = create_access_token(
                identity=resp[0]['username'], additional_claims=additional_claims)
            refresh_token = create_refresh_token(
                identity=resp[0]['username'], additional_claims=additional_claims)

            resp[0]['access_token'] = access_token
            resp[0]['refresh_token'] = refresh_token

            return resp


@auth_ns.route("/signup/sme")
class SignupSME(Resource):
    @auth_ns.doc("Signup for SME")
    @auth_ns.expect(new_sme)
    def post(self):
        return AuthService.signup_SME(request.json)


@auth_ns.route("/signup/shg")
class SignupSHG(Resource):
    @auth_ns.doc("Signup for SHG")
    @auth_ns.expect(new_shg)
    def post(self):
        return AuthService.signup_SHG(request.json)


@auth_ns.route('/refreshToken')
class RefereshJWTToken(Resource):
    @jwt_required(optional=True)
    def post(self):
        try:
            current_identity = get_jwt_identity()
            claims = get_jwt()
            print(current_identity)
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
                'user_type': claims['user_type'],
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
