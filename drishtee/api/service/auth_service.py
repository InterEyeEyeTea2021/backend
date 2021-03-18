from flask import abort
from flask import current_app as app
from flask_login import current_user
from flask_login import login_user as flask_login_user
from flask_login import logout_user as logout

from logging import getLogger
from functools import wraps

from drishtee.db.base import session_scope

import drishtee.db.models as models

LOG = getLogger(__name__)


class AuthService:

    @staticmethod
    def isSuperUser(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not current_user.is_authenticated:
                LOG.error("User isn't logged in.", exc_info=True)
                abort(403)

            if current_user.username != app.config['SUPERUSER_NAME']:
                LOG.error("The user doesn't have superuser access.",
                          exc_info=True)
                abort(403)
            return f(*args, **kwargs)
        return

    @staticmethod
    def login_user_SHG(data):
        try:
            if current_user.is_authenticated:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Already Logged In',
                }
                return response_object, 300
            with session_scope() as session:
                user = session.query(models.UserSHG).filter(
                    models.UserSHG.username == data.get("username")).all()

                if len(user) == 0:
                    user = None
                else:
                    user = user[0]

                if user is None:
                    response_object = {
                        'status': 'fail',
                        'message': 'User does not exist. '
                    }
                    return response_object, 403

                if user and user.check_password(data.get('password')):
                    if True:
                        # if user.is_verified: // TODO: Add verification
                        # convert string to bool
                        if data.get('remember').lower() == 'true' or data.get(
                                'remember').lower() == 'yes':
                            remem = True
                        else:
                            remem = False
                        flask_login_user(user, remember=remem)
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                        }

                        login_info = {
                            'id': current_user.id,
                            'username': current_user.username,
                            'user_type': "SHG"
                        }
                        return login_info, 200
                    else:
                        response_object = {
                            'status': 'fail',
                            'message': 'Please verify your Username before first login',
                        }
                        return response_object, 402
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'Username or password does not match.',
                    }
                    return response_object, 401

        except BaseException:
            LOG.error('Login Failed', exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def login_user_SME(data):
        try:
            if current_user.is_authenticated:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Already Logged In',
                }
                return response_object, 300
            with session_scope() as session:
                user = session.query(models.UserSME).filter(
                    models.UserSME.username == data.get("username")).first()
                if user is None:
                    response_object = {
                        'status': 'fail',
                        'message': 'User does not exist. '
                    }
                    return response_object, 403

                if user and user.check_password(data.get('password')):
                    if True:
                        # if user.is_verified: // TODO: Add verification
                        # convert string to bool
                        if data.get('remember').lower() == 'true' or data.get(
                                'remember').lower() == 'yes':
                            remem = True
                        else:
                            remem = False

                        flask_login_user(user, remember=remem)

                        login_info = {
                            'id': user.id,
                            'username': user.username,
                            'user_type': "SME"
                        }
                        return login_info, 200
                    else:
                        response_object = {
                            'status': 'fail',
                            'message': 'Please verify your Username before first login',
                        }
                        return response_object, 402
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'Username or password does not match.',
                    }
                    return response_object, 401

        except BaseException:
            LOG.error('Login Failed', exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def signup_SME(data):
        try:
            with session_scope() as session:
                user = session.query(models.UserSME).filter(
                    models.UserSME.username == data.get("username")).first()

                if user is not None:
                    response_object = {
                        'status': 'invalid',
                        'message': 'Username Already Registered',
                    }
                    LOG.info(
                        'Username already present in database. Redirect to Login Page')
                    return response_object, 401

                bank = models.BankDetails(
                    data.get("account_number"), data.get("branch_code"))

                user = models.UserSME(data.get("name"), data.get("username"), data.get(
                    "password"), data.get("phone"), data.get("WAContact"), data.get("industry_type"), data.get("image_uri"), bank)

                session.add(user)
            response_object = {
                'status': 'success',
                'message': 'User added Successfully',
            }

            return response_object, 200
        except BaseException as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def signup_SHG(data):
        try:
            with session_scope() as session:
                user = session.query(models.UserSHG).filter(
                    models.UserSHG.username == data.get("username")).first()

                if user is not None:
                    response_object = {
                        'status': 'invalid',
                        'message': 'Username Already Registered',
                    }
                    LOG.info(
                        'Username already present in database. Redirect to Login Page')
                    return response_object, 401

                bank = models.BankDetails(
                    data.get("account_number"), data.get("branch_code"))

                user = models.UserSHG(data.get("name"), data.get("username"), data.get(
                    "password"), data.get("phone"), data.get("WAContact"), data.get("name_SHG"),
                    data.get("industry_type"), data.get("production_cap"), data.get("order_size"), data.get("image_uri"), bank)

                session.add(user)
            response_object = {
                'status': 'success',
                'message': 'User added Successfully',
            }

            return response_object, 200
        except BaseException as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500
