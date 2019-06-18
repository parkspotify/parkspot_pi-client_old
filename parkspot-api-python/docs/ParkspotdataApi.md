# swagger_client.ParkspotdataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_parkspotnode**](ParkspotdataApi.md#create_parkspotnode) | **POST** /parkspotnodes | Create a new parkspot node
[**delete_parkspot_node**](ParkspotdataApi.md#delete_parkspot_node) | **DELETE** /parkspotnodes/{parkspotID} | Delete a parkspot node
[**get_parkspot_node_by_id**](ParkspotdataApi.md#get_parkspot_node_by_id) | **GET** /parkspotnodes/{parkspotID} | Get an existing parkspot node by ID
[**get_parkspotnodes**](ParkspotdataApi.md#get_parkspotnodes) | **GET** /parkspotnodes | Get the list of user&#39;s parkspot nodes
[**update_parkspotnodes_status**](ParkspotdataApi.md#update_parkspotnodes_status) | **PUT** /parkspotnodes/{parkspotID} | Update parkspot node&#39;s status to the cloud


# **create_parkspotnode**
> InlineResponse2004 create_parkspotnode(x_api_key, parkspotdata)

Create a new parkspot node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ParkspotdataApi(swagger_client.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | User's API-Key
parkspotdata = swagger_client.NewParkspotData() # NewParkspotData | Parkspot data to create a new database entry

try:
    # Create a new parkspot node
    api_response = api_instance.create_parkspotnode(x_api_key, parkspotdata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParkspotdataApi->create_parkspotnode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| User&#39;s API-Key | 
 **parkspotdata** | [**NewParkspotData**](NewParkspotData.md)| Parkspot data to create a new database entry | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parkspot_node**
> ParkspotData delete_parkspot_node(x_api_key, parkspot_id)

Delete a parkspot node



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ParkspotdataApi(swagger_client.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | User's API-Key
parkspot_id = 'parkspot_id_example' # str | ID of the parkspot node to update

try:
    # Delete a parkspot node
    api_response = api_instance.delete_parkspot_node(x_api_key, parkspot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParkspotdataApi->delete_parkspot_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| User&#39;s API-Key | 
 **parkspot_id** | **str**| ID of the parkspot node to update | 

### Return type

[**ParkspotData**](ParkspotData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parkspot_node_by_id**
> ParkspotData get_parkspot_node_by_id(x_api_key, parkspot_id)

Get an existing parkspot node by ID

Returns a single parkspot node object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ParkspotdataApi(swagger_client.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | User's API-Key
parkspot_id = 'parkspot_id_example' # str | ID of the parkspot node to update

try:
    # Get an existing parkspot node by ID
    api_response = api_instance.get_parkspot_node_by_id(x_api_key, parkspot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParkspotdataApi->get_parkspot_node_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| User&#39;s API-Key | 
 **parkspot_id** | **str**| ID of the parkspot node to update | 

### Return type

[**ParkspotData**](ParkspotData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parkspotnodes**
> InlineResponse2003 get_parkspotnodes(x_api_key)

Get the list of user's parkspot nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ParkspotdataApi(swagger_client.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | User's API-Key

try:
    # Get the list of user's parkspot nodes
    api_response = api_instance.get_parkspotnodes(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParkspotdataApi->get_parkspotnodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| User&#39;s API-Key | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parkspotnodes_status**
> JSONResponse update_parkspotnodes_status(x_api_key, parkspotdata, parkspot_id)

Update parkspot node's status to the cloud

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ParkspotdataApi(swagger_client.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | User's API-Key
parkspotdata = swagger_client.UpdateParkspotStatus() # UpdateParkspotStatus | Parkspot node's status data object
parkspot_id = 'parkspot_id_example' # str | ID of the parkspot node to update

try:
    # Update parkspot node's status to the cloud
    api_response = api_instance.update_parkspotnodes_status(x_api_key, parkspotdata, parkspot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParkspotdataApi->update_parkspotnodes_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| User&#39;s API-Key | 
 **parkspotdata** | [**UpdateParkspotStatus**](UpdateParkspotStatus.md)| Parkspot node&#39;s status data object | 
 **parkspot_id** | **str**| ID of the parkspot node to update | 

### Return type

[**JSONResponse**](JSONResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

