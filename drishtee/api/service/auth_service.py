from flask import abort
from flask import current_app as app

from logging import getLogger
from functools import wraps

from drishtee.db.base import session_scope

import drishtee.db.models as models

LOG = getLogger(__name__)


def format_user_sme(session, sme):
    return {
        "user_type": "SME",
        "sme_id": sme.id,
        "name": sme.name,
        "username": sme.username,
        "phone": sme.phone,
        "WAContact": sme.WAContact,
        "industry_type": sme.industry_type,
        "account_number": sme.bank_details.account_no,
        "branch_code": sme.bank_details.ifsc_code
    }


def format_user_shg(session, shg):
    return {
        "user_type": "SHG",
        "shg_id": shg.id,
        "name": shg.name,
        "username": shg.username,
        "phone": shg.phone,
        "WAContact": shg.WAContact,
        "industry_type": shg.industry_type,
        "name_SHG": shg.SHG_Name,
        "production_cap": shg.prod_capacity,
        "order_size": shg.order_size,
        "account_number": shg.bank_details.account_no,
        "branch_code": shg.bank_details.ifsc_code
    }


class AuthService:

    @staticmethod
    def login_user_SHG(data):
        try:
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
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                        }

                        login_info = format_user_shg(session, user)
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

                        login_info = format_user_sme(session, user)
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
