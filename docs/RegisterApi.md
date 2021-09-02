# auth_api.RegisterApi

All URIs are relative to *http://localhost:5000/auth/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_user**](RegisterApi.md#register_user) | **POST** /register | Register user

# **register_user**
> register_user(body)

Register user

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.RegisterApi()
body = auth_api.User() # User | User data.

try:
    # Register user
    api_instance.register_user(body)
except ApiException as e:
    print("Exception when calling RegisterApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| User data. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

