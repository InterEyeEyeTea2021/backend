"""
Entrypoint of the application.

Manager is set up and the blueprint for the
application is created.
"""
import os
from logging import getLogger

from flask import Flask, current_app
from flask_cors import CORS

from drishtee.config.app_config import config_by_name
from drishtee.config.logging_config import setup_logger

setup_logger()
LOG = getLogger(__name__)


def register_blueprints(app):
    from drishtee.api import api_bp

    app.register_blueprint(api_bp)
    LOG.info("API blueprint registered!")


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    LOG.info("app loaded with configuration {}!".format(config_name))

    CORS(app)
    LOG.info("Flask CORS setup successfully")
    with app.app_context():
        register_blueprints(app)

    return app


app = create_app(os.getenv("FLASK_ENV") or "development")
