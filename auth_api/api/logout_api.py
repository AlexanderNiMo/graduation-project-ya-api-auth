# coding: utf-8

"""
    Auth

    Сервис авторизации пользователей.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from auth_api.api_client import ApiClient


class LogoutApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def logout_post(self, jwt_token, refresh_token, **kwargs):  # noqa: E501
        """logout user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_post(jwt_token, refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :param Token refresh_token: refresh token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_post_with_http_info(jwt_token, refresh_token, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_post_with_http_info(jwt_token, refresh_token, **kwargs)  # noqa: E501
            return data

    def logout_post_with_http_info(self, jwt_token, refresh_token, **kwargs):  # noqa: E501
        """logout user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_post_with_http_info(jwt_token, refresh_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :param Token refresh_token: refresh token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt_token', 'refresh_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt_token' is set
        if ('jwt_token' not in params or
                params['jwt_token'] is None):
            raise ValueError("Missing the required parameter `jwt_token` when calling `logout_post`")  # noqa: E501
        # verify the required parameter 'refresh_token' is set
        if ('refresh_token' not in params or
                params['refresh_token'] is None):
            raise ValueError("Missing the required parameter `refresh_token` when calling `logout_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt_token' in params:
            header_params['jwt_token'] = params['jwt_token']  # noqa: E501
        if 'refresh_token' in params:
            header_params['refresh_token'] = params['refresh_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
