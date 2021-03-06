# Data Transfer Object- Responsible for carrying data between processes
from flask import current_app
from flask_restx import Namespace, fields


class UserDto:
    ns = Namespace("User", description="User related operations")


class DataDto:
    ns = Namespace("Data", description="Data Related operations")


class TenderDto:
    ns = Namespace("Tender", description="Tender operations")


class AuthDto:
    ns = Namespace("Auth", description="Auth Related operations")

    user_auth = ns.model('auth_details', {
        'user_type': fields.String(required=True, description="SHG or SME"),
        'username': fields.String(required=True, description='Login Username'),
        'password': fields.String(required=True, description='Login Password'),
        'remember': fields.String(description='Stay Logged In')
    })

    new_sme = ns.model('sme_details', {
        'name': fields.String(required=True, description="Name of User signing up"),
        'username': fields.String(required=True, description="Username of User signing up"),
        'password': fields.String(required=True, description='Signup Password'),
        'phone': fields.String(required=True, description="Phone Number"),
        'WAContact': fields.String(required=True, description="Whatsapp Phone Number"),
        'industry_type': fields.String(required=True, description="Type of Industry"),
        'account_number': fields.String(required=True),
        'branch_code': fields.String(required=True),
    })

    new_shg = ns.model('shg_details', {
        'name': fields.String(required=True, description="Name of User signing up"),
        'username': fields.String(required=True, description="Username of User signing up"),
        'password': fields.String(required=True, description='Signup Password'),
        'phone': fields.String(required=True, description="Phone Number"),
        'WAContact': fields.String(required=True, description="Whatsapp Phone Number"),
        'industry_type': fields.String(required=True, description="Type of Industry"),
        'account_number': fields.String(required=True),
        'branch_code': fields.String(required=True),
        'name_SHG': fields.String(required=True),
        'production_cap': fields.String(required=True),
        'order_size': fields.String(required=True)
    })


class BidDto:
    ns = Namespace("Bids", description="Bid operations")


class MilestoneDto:
    ns = Namespace("Milestones", description="Milestone operations")


class OrderDto:
    ns = Namespace("Orders", description="Order operations")


class ProductDto:
    ns = Namespace("Products", description="Product operations")
    new_product = ns.model('product_details', {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
        'image_uri': fields.String(required=True),
        'min_size': fields.String(required=True),
        'price': fields.String(required=True)
    })

# class PostDto(Schema):
#     caption = fields.String()
#     share_date = fields.DateTime()
#     likes_count = fields.Integer()
#     permalink_url = fields.String()


# post_dto = PostDto()
