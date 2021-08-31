# auth_api.UserDataApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_data_patch**](UserDataApi.md#update_data_patch) | **PATCH** /update_data | update user data
[**user_data_get**](UserDataApi.md#user_data_get) | **GET** /user_data | get user data

# **update_data_patch**
> update_data_patch(jwt_token, body=body)

update user data

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.UserDataApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.
body = auth_api.UpdateData() # UpdateData |  (optional)

try:
    # update user data
    api_instance.update_data_patch(jwt_token, body=body)
except ApiException as e:
    print("Exception when calling UserDataApi->update_data_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 
 **body** | [**UpdateData**](UpdateData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_data_get**
> UserData user_data_get(jwt_token)

get user data

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.UserDataApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.

try:
    # get user data
    api_response = api_instance.user_data_get(jwt_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserDataApi->user_data_get: %s\n" % e)
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

