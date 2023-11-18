"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import nodeproperty as shared_nodeproperty
from dataclasses_json import Undefined, dataclass_json
from tmp2 import utils
from typing import List, Optional


@dataclasses.dataclass
class AddPropertyRequest:
    rocket_node_path: str = dataclasses.field(metadata={'path_param': { 'field_name': 'rocketNodePath', 'style': 'simple', 'explode': False }})
    r"""Target node."""
    node_property: Optional[shared_nodeproperty.NodeProperty] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddPropertyResponseBody:
    r"""Property added successfully."""
    node_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nodeName'), 'exclude': lambda f: f is None }})
    node_properties: Optional[List[shared_nodeproperty.NodeProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nodeProperties'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class AddPropertyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[AddPropertyResponseBody] = dataclasses.field(default=None)
    r"""Property added successfully."""
    

