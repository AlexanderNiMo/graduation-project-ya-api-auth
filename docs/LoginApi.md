# auth_api.LoginApi

All URIs are relative to *http://localhost:5000/auth/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](LoginApi.md#login_user) | **POST** /login | Login user
[**twof_auth_check_post**](LoginApi.md#twof_auth_check_post) | **POST** /twof_auth/check | check multi-factor authentication code
[**twof_auth_sync_get**](LoginApi.md#twof_auth_sync_get) | **GET** /twof_auth/sync | Multi-factor authentication

# **login_user**
> login_user(body)

Login user

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.LoginApi()
body = auth_api.LoginRequest() # LoginRequest | Credential data.

try:
    # Login user
    api_instance.login_user(body)
except ApiException as e:
    print("Exception when calling LoginApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)| Credential data. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twof_auth_check_post**
> JWTToken twof_auth_check_post(body)

check multi-factor authentication code

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieAuth
configuration = auth_api.Configuration()
configuration.api_key['SESSION_ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SESSION_ID'] = 'Bearer'

# create an instance of the API class
api_instance = auth_api.LoginApi(auth_api.ApiClient(configuration))
body = auth_api.OTP() # OTP | Credential data.

try:
    # check multi-factor authentication code
    api_response = api_instance.twof_auth_check_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->twof_auth_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OTP**](OTP.md)| Credential data. | 

### Return type

[**JWTToken**](JWTToken.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twof_auth_sync_get**
> ProvisioningURL twof_auth_sync_get()

Multi-factor authentication

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieAuth
configuration = auth_api.Configuration()
configuration.api_key['SESSION_ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SESSION_ID'] = 'Bearer'

# create an instance of the API class
api_instance = auth_api.LoginApi(auth_api.ApiClient(configuration))

try:
    # Multi-factor authentication
    api_response = api_instance.twof_auth_sync_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->twof_auth_sync_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProvisioningURL**](ProvisioningURL.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

