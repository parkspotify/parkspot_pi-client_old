# swagger_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UserApi.md#add_user) | **POST** /users | Add a new user to the system
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{userId} | Delete a user
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /users/{userId} | Get an existing user by ID
[**get_users**](UserApi.md#get_users) | **GET** /users | Get existing users list
[**modify_user**](UserApi.md#modify_user) | **POST** /users/{userId} | Modify an existing user
[**user_login**](UserApi.md#user_login) | **POST** /users/login | Logs user into the system
[**user_register**](UserApi.md#user_register) | **POST** /users/register | Allows a guest to register in the system


# **add_user**
> InlineResponse200 add_user(body)

Add a new user to the system

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.User() # User | Created user object

try:
    # Add a new user to the system
    api_response = api_instance.add_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| Created user object | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | User id to delete

try:
    # Delete a user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User id to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> User get_user_by_id(user_id)

Get an existing user by ID

Returns a single user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | ID of user to return

try:
    # Get an existing user by ID
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user to return | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User] get_users(x_api_key)

Get existing users list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
x_api_key = 'x_api_key_example' # str | 

try:
    # Get existing users list
    api_response = api_instance.get_users(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user**
> InlineResponse2001 modify_user(user_id, body)

Modify an existing user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | ID of the user to modify
body = swagger_client.NewUserRegistration() # NewUserRegistration | Modified user object

try:
    # Modify an existing user
    api_response = api_instance.modify_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->modify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user to modify | 
 **body** | [**NewUserRegistration**](NewUserRegistration.md)| Modified user object | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login**
> InlineResponse2002 user_login(body)

Logs user into the system



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.Login() # Login | Login data

try:
    # Logs user into the system
    api_response = api_instance.user_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| Login data | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_register**
> InlineResponse2002 user_register(body)

Allows a guest to register in the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.NewUserRegistration() # NewUserRegistration | Created user object

try:
    # Allows a guest to register in the system
    api_response = api_instance.user_register(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewUserRegistration**](NewUserRegistration.md)| Created user object | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

