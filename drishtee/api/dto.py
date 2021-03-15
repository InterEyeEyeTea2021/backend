# Data Transfer Object- Responsible for carrying data between processes
from flask import current_app
from flask_restx import Namespace, fields


class DataDto:
    ns = Namespace("Data", description="Data Related operations")


class AuthDto:
    ns = Namespace("Auth", description="Auth Related operations")

    user_auth = ns.model('auth_details', {
        'user_type': fields.String(required=True, description="SHG or SME"),
        'username': fields.String(required=True, description='Login Username'),
        'password': fields.String(required=True, description='Login Password'),
        'remember': fields.String(description='Stay Logged In')
    })


# class PostDto(Schema):
#     caption = fields.String()
#     share_date = fields.DateTime()
#     likes_count = fields.Integer()
#     permalink_url = fields.String()


# post_dto = PostDto()
