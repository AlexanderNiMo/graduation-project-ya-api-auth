# graduation-project-ya-api-auth
Сервис авторизации пользователей.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.5
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import auth_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import auth_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.JwtTokenApi(auth_api.ApiClient(configuration))
jwt_token = auth_api.Token() # Token | auth. jwt token.

try:
    # validate jwt token
    api_response = api_instance.check_user_post(jwt_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JwtTokenApi->check_user_post: %s\n" % e)

# create an instance of the API class
api_instance = auth_api.JwtTokenApi(auth_api.ApiClient(configuration))
jwt_token = auth_api.Token() # Token | auth. jwt token.
refresh_token = auth_api.Token() # Token | refresh token.

try:
    # refresh jwt token
    api_response = api_instance.refresh_post(jwt_token, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JwtTokenApi->refresh_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000/auth/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JwtTokenApi* | [**check_user_post**](docs/JwtTokenApi.md#check_user_post) | **POST** /check_user | validate jwt token
*JwtTokenApi* | [**refresh_post**](docs/JwtTokenApi.md#refresh_post) | **POST** /refresh | refresh jwt token
*LoginApi* | [**login_user**](docs/LoginApi.md#login_user) | **POST** /login | Login user
*LoginApi* | [**twof_auth_check_post**](docs/LoginApi.md#twof_auth_check_post) | **POST** /twof_auth/check | check multi-factor authentication code
*LoginApi* | [**twof_auth_sync_get**](docs/LoginApi.md#twof_auth_sync_get) | **GET** /twof_auth/sync | Multi-factor authentication
*LogoutApi* | [**logout_post**](docs/LogoutApi.md#logout_post) | **POST** /logout | logout user
*OauthApi* | [**oauth_yandex_auth**](docs/OauthApi.md#oauth_yandex_auth) | **GET** /oauth/yandex/auth | callback for authorise user
*OauthApi* | [**oauth_yandex_callback**](docs/OauthApi.md#oauth_yandex_callback) | **GET** /oauth/yandex/callback | callback for authorise user
*OauthApi* | [**oauth_yandex_redirect**](docs/OauthApi.md#oauth_yandex_redirect) | **GET** /oauth/yandex/redirect | oauth user
*RegisterApi* | [**register_user**](docs/RegisterApi.md#register_user) | **POST** /register | Register user
*RoleApi* | [**add_user_role**](docs/RoleApi.md#add_user_role) | **PATCH** /user_role/{user_id}/{role} | add user role
*RoleApi* | [**del_user_role**](docs/RoleApi.md#del_user_role) | **DELETE** /user_role/{user_id}/{role} | delete user role
*UserDataApi* | [**update_data_patch**](docs/UserDataApi.md#update_data_patch) | **PATCH** /update_data | update user data
*UserDataApi* | [**user_data_get**](docs/UserDataApi.md#user_data_get) | **GET** /user_data | get user data

## Documentation For Models

 - [History](docs/History.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [JWTToken](docs/JWTToken.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [OAUTHToken](docs/OAUTHToken.md)
 - [OTP](docs/OTP.md)
 - [ProvisioningURL](docs/ProvisioningURL.md)
 - [Role](docs/Role.md)
 - [Token](docs/Token.md)
 - [UpdateData](docs/UpdateData.md)
 - [UseiId](docs/UseiId.md)
 - [User](docs/User.md)
 - [UserData](docs/UserData.md)
 - [UserShort](docs/UserShort.md)

## Documentation For Authorization


## cookieAuth

- **Type**: API key
- **API key parameter name**: SESSION_ID
- **Location**: URL query string


## Author


