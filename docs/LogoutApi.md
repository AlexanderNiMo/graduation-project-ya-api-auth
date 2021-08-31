# auth.LogoutApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout_post**](LogoutApi.md#logout_post) | **POST** /logout | logout user

# **logout_post**
> logout_post(jwt_token, refresh_token)

logout user

### Example
```python
from __future__ import print_function
import time
import auth
from auth.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth.LogoutApi()
jwt_token = auth.Token() # Token | auth. jwt token.
refresh_token = auth.Token() # Token | refresh token.

try:
    # logout user
    api_instance.logout_post(jwt_token, refresh_token)
except ApiException as e:
    print("Exception when calling LogoutApi->logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 
 **refresh_token** | [**Token**](.md)| refresh token. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

