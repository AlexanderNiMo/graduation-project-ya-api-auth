# auth_api.OauthApi

All URIs are relative to *http://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_yandex_auth**](OauthApi.md#oauth_yandex_auth) | **GET** /oauth/yandex/auth | callback for authorise user
[**oauth_yandex_callback**](OauthApi.md#oauth_yandex_callback) | **GET** /oauth/yandex/callback | callback for authorise user
[**oauth_yandex_redirect**](OauthApi.md#oauth_yandex_redirect) | **GET** /oauth/yandex/redirect | oauth user

# **oauth_yandex_auth**
> JWTToken oauth_yandex_auth()

callback for authorise user

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.OauthApi()

try:
    # callback for authorise user
    api_response = api_instance.oauth_yandex_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthApi->oauth_yandex_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JWTToken**](JWTToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_yandex_callback**
> OAUTHToken oauth_yandex_callback(code)

callback for authorise user

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.OauthApi()
code = 'code_example' # str | code for get oauth token

try:
    # callback for authorise user
    api_response = api_instance.oauth_yandex_callback(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthApi->oauth_yandex_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code for get oauth token | 

### Return type

[**OAUTHToken**](OAUTHToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_yandex_redirect**
> InlineResponse200 oauth_yandex_redirect()

oauth user

### Example
```python
from __future__ import print_function
import time
import auth_api
from auth_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = auth_api.OauthApi()

try:
    # oauth user
    api_response = api_instance.oauth_yandex_redirect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthApi->oauth_yandex_redirect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

