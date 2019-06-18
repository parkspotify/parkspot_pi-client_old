# swagger_client.PrometheusApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics**](PrometheusApi.md#metrics) | **GET** /metrics | Prometheus endpoint


# **metrics**
> metrics()

Prometheus endpoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrometheusApi()

try:
    # Prometheus endpoint
    api_instance.metrics()
except ApiException as e:
    print("Exception when calling PrometheusApi->metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

