<!-- Start SDK Example Usage [usage] -->
```python
import tmp2
from tmp2.models import operations, shared

s = tmp2.Tmp2()

req = operations.AddPropertyRequest(
    rocket_node_path='string',
    node_property=shared.NodeProperty(
        key='<key>',
        value=7039.04,
    ),
)

res = s.add_property(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->