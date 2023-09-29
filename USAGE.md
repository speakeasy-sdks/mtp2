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
    rocket_node_path='Passenger',
)

res = s.add_property(req)

if res.add_property_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->