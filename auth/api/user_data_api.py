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

from auth.api_client import ApiClient


class UserDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def update_data_patch(self, jwt_token, **kwargs):  # noqa: E501
        """update user data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_patch(jwt_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :param UpdateData body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_data_patch_with_http_info(jwt_token, **kwargs)  # noqa: E501
        else:
            (data) = self.update_data_patch_with_http_info(jwt_token, **kwargs)  # noqa: E501
            return data

    def update_data_patch_with_http_info(self, jwt_token, **kwargs):  # noqa: E501
        """update user data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_patch_with_http_info(jwt_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :param UpdateData body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_data_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt_token' is set
        if ('jwt_token' not in params or
                params['jwt_token'] is None):
            raise ValueError("Missing the required parameter `jwt_token` when calling `update_data_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt_token' in params:
            header_params['jwt_token'] = params['jwt_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/update_data', 'PATCH',
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

    def user_data_get(self, jwt_token, **kwargs):  # noqa: E501
        """get user data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_data_get(jwt_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :return: UserData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_data_get_with_http_info(jwt_token, **kwargs)  # noqa: E501
        else:
            (data) = self.user_data_get_with_http_info(jwt_token, **kwargs)  # noqa: E501
            return data

    def user_data_get_with_http_info(self, jwt_token, **kwargs):  # noqa: E501
        """get user data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_data_get_with_http_info(jwt_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Token jwt_token: auth. jwt token. (required)
        :return: UserData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt_token' is set
        if ('jwt_token' not in params or
                params['jwt_token'] is None):
            raise ValueError("Missing the required parameter `jwt_token` when calling `user_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt_token' in params:
            header_params['jwt_token'] = params['jwt_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user_data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
