# Tmp2 SDK


## Overview

Node Management API: Create and manage rocket nodes..

### Available Operations

* [add_property](#add_property) - Add property to target node.
* [create_node](#create_node) - Create node at the specified path.
* [get_subtree](#get_subtree) - Return subtree of target node.

## add_property

Add property to target node.

### Example Usage

```python
import tmp2
from tmp2.models import operations, shared

s = tmp2.Tmp2()

req = operations.AddPropertyRequest(
    node_property=shared.NodeProperty(
        key='<key>',
        value=7039.04,
    ),
    rocket_node_path='string',
)

res = s.add_property(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AddPropertyRequest](../../models/operations/addpropertyrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.AddPropertyResponse](../../models/operations/addpropertyresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.AddPropertyResponseBody         | 400                                    | application/json                       |
| errors.AddPropertyResponseResponseBody | 404                                    | application/json                       |
| errors.SDKError                        | 4x-5xx                                 | */*                                    |

## create_node

Create node at the specified path.

### Example Usage

```python
import tmp2
from tmp2.models import operations

s = tmp2.Tmp2()

req = operations.CreateNodeRequest(
    rocket_node_path='string',
)

res = s.create_node(req)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateNodeRequest](../../models/operations/createnoderequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateNodeResponse](../../models/operations/createnoderesponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.CreateNodeResponseBody | 400                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

## get_subtree

Return subtree of target node.

### Example Usage

```python
import tmp2
from tmp2.models import operations

s = tmp2.Tmp2()

req = operations.GetSubtreeRequest(
    rocket_node_path='string',
)

res = s.get_subtree(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetSubtreeRequest](../../models/operations/getsubtreerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetSubtreeResponse](../../models/operations/getsubtreeresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GetSubtreeResponseBody | 404                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |
