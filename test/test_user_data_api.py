# coding: utf-8

"""
    Auth

    Сервис авторизации пользователей.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import auth
from auth.api.user_data_api import UserDataApi  # noqa: E501
from auth.rest import ApiException


class TestUserDataApi(unittest.TestCase):
    """UserDataApi unit test stubs"""

    def setUp(self):
        self.api = UserDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_update_data_patch(self):
        """Test case for update_data_patch

        update user data  # noqa: E501
        """
        pass

    def test_user_data_get(self):
        """Test case for user_data_get

        get user data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
