# auth_api.JwtTokenApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_user_post**](JwtTokenApi.md#check_user_post) | **POST** /check_user | validate jwt token
[**refresh_post**](JwtTokenApi.md#refresh_post) | **POST** /refresh | refresh jwt token

# **check_user_post**
> UserData check_user_post(jwt_token)

validate jwt token

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.JwtTokenApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.

try:
    # validate jwt token
    api_response = api_instance.check_user_post(jwt_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JwtTokenApi->check_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 

### Return type

[**UserData**](UserData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_post**
> JWTToken refresh_post(jwt_token, refresh_token)

refresh jwt token

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.JwtTokenApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.
refresh_token = auth_api.Token() # Token | refresh token.

try:
    # refresh jwt token
    api_response = api_instance.refresh_post(jwt_token, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JwtTokenApi->refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 
 **refresh_token** | [**Token**](.md)| refresh token. | 

### Return type

[**JWTToken**](JWTToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

