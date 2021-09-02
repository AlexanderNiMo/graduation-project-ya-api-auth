# auth_api.RoleApi

All URIs are relative to *http://localhost:5000/auth/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_role**](RoleApi.md#add_user_role) | **PATCH** /user_role/{user_id}/{role} | add user role
[**del_user_role**](RoleApi.md#del_user_role) | **DELETE** /user_role/{user_id}/{role} | delete user role

# **add_user_role**
> add_user_role(jwt_token, refresh_token, user_id, role)

add user role

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.RoleApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.
refresh_token = auth_api.Token() # Token | refresh token.
user_id = auth_api.UseiId() # UseiId | 
role = auth_api.Role() # Role | 

try:
    # add user role
    api_instance.add_user_role(jwt_token, refresh_token, user_id, role)
except ApiException as e:
    print("Exception when calling RoleApi->add_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 
 **refresh_token** | [**Token**](.md)| refresh token. | 
 **user_id** | [**UseiId**](.md)|  | 
 **role** | [**Role**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_user_role**
> del_user_role(jwt_token, refresh_token, user_id, role)

delete user role

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.RoleApi()
jwt_token = auth_api.Token() # Token | auth. jwt token.
refresh_token = auth_api.Token() # Token | refresh token.
user_id = auth_api.UseiId() # UseiId | 
role = auth_api.Role() # Role | 

try:
    # delete user role
    api_instance.del_user_role(jwt_token, refresh_token, user_id, role)
except ApiException as e:
    print("Exception when calling RoleApi->del_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | [**Token**](.md)| auth. jwt token. | 
 **refresh_token** | [**Token**](.md)| refresh token. | 
 **user_id** | [**UseiId**](.md)|  | 
 **role** | [**Role**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

