# coding: utf-8

# flake8: noqa

"""
    Auth

    Сервис авторизации пользователей.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.jwt_token_api import JwtTokenApi
from swagger_client.api.login_api import LoginApi
from swagger_client.api.logout_api import LogoutApi
from swagger_client.api.oauth_api import OauthApi
from swagger_client.api.register_api import RegisterApi
from swagger_client.api.role_api import RoleApi
from swagger_client.api.user_data_api import UserDataApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.history import History
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.jwt_token import JWTToken
from swagger_client.models.login_request import LoginRequest
from swagger_client.models.oauth_token import OAUTHToken
from swagger_client.models.otp import OTP
from swagger_client.models.provisioning_url import ProvisioningURL
from swagger_client.models.role import Role
from swagger_client.models.token import Token
from swagger_client.models.update_data import UpdateData
from swagger_client.models.usei_id import UseiId
from swagger_client.models.user import User
from swagger_client.models.user_data import UserData