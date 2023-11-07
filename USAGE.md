<!-- Start SDK Example Usage -->


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

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->