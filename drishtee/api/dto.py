# Data Transfer Object- Responsible for carrying data between processes
from flask import current_app
from flask_restx import Namespace
from marshmallow import Schema, fields


class DataDto:
    ns = Namespace("Data", description="Data Related operations")

class TenderDto:
    ns = Namespace("Tender", description="Tender operations")

# class PostDto(Schema):
#     caption = fields.String()
#     share_date = fields.DateTime()
#     likes_count = fields.Integer()
#     permalink_url = fields.String()


# post_dto = PostDto()
