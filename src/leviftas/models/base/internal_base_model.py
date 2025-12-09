#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright © 2025 Leviftas authors. All rights reserved.

Licensed under the GNU General Public License v3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

internal_base_model.py

Internal base model for Leviftas system components. This module provides
a strictly configured Pydantic BaseModel designed for internal use only,
with security-hardened settings and consistent validation behavior.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_snake
from typing_extensions import ClassVar


class InternalBaseModel(BaseModel):
    """
    Base model for all internal Leviftas system components.

    This class provides a security-hardened, strictly-typed foundation for
    internal data models. It enforces consistent validation, serialization,
    and security policies across all internal system components.

    Attributes:
        model_config (ConfigDict): Pydantic model configuration with
            security-hardened settings for internal system use.

    Note:
        This model is intended for internal system use only. For public-facing
        APIs or user-defined models, use the appropriate public model classes.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(
        # Strip leading and trailing whitespace for str types
        str_strip_whitespace=True,
        # Preventing memory issues caused by malicious submission of excessively long strings
        str_max_length=10000,
        # Providing extra data is not permitted
        extra="forbid",
        # Modification is allowed, but it must be validated during modification in conjunction with validate_assignment
        frozen=False,
        # Populate models with the value property of enums
        use_enum_values=True,
        # Validate the data when the model is changed
        validate_assignment=True,
        # Arbitrary types are not allowed for field types
        arbitrary_types_allowed=False,
        # Allows instances to be converted into data models to improve operational flexibility
        from_attributes=True,
        # Using the Python naming conventions of to_snake
        alias_generator=to_snake,
        # Infinity and NaN are prohibited to prevent computational anomalies
        allow_inf_nan=False,
        # Strict mode reduces unexpected runtime errors
        strict=True,
        # To prevent internal data tampering, enable re-authentication
        revalidate_instances="always",
        # Use standard format for timedelta serialization
        ser_json_timedelta="iso8601",
        # Validate default values to ensure the safety of model definitions
        validate_default=True,
        # Verify the return value to ensure that the data returned by the method meets expectations
        validate_return=True,
        # Build immediately to ensure issues are detected at startup
        defer_build=False,
        # Non-backtracking, preventing ReDoS attacks
        regex_engine="rust-regex",
        # Prevent number type casting (avoid type confusion attacks)
        coerce_numbers_to_str=False,
        # Allow validation by field name (flexibility)
        validate_by_name=True,
        # Allow validation by alias (works with alias_generator)
        validate_by_alias=True,
        # Use original field names during serialization (internal system consistency)
        serialize_by_alias=False,
        # Cache strings to improve performance
        cache_strings=True,
        # Show complete error information for internal system debugging
        hide_input_in_errors=False,
        # Show validation error causes for debugging
        validation_error_cause=True,
        # Safe byte serialization
        ser_json_inf_nan="null",
        # Protect internal methods and private attributes
        protected_namespaces=('model_', '_'),
        # Use attribute docstrings for documentation
        use_attribute_docstrings=True,
        # Use actual key provided in data for error locations
        loc_by_alias=True,
        # JSON schema serialization defaults not required
        json_schema_serialization_defaults_required=False,
        # Preserve empty URL paths
        url_preserve_empty_path=False,
    )

    class Meta:
        """
        Model metadata for classification, versioning and observability.

        Attributes:
            version: Semantic version string for the model (e.g., "1.0.0")
            category: Classification category for the model (e.g., "internal", "config", "event")
            tags: Simple string tags for filtering and grouping (e.g., {"critical", "auth"})
            labels: Key-value pairs for structured metadata (e.g., {"env": "prod", "team": "platform"})
        """
        # Semantic version string for the model
        version: str = "0.1.0"
        # Classification category for the model
        category: str = "internal"
        # Simple string tags for filtering and grouping
        tags: set[str] = set()
        # Key-value pairs for structured metadata
        labels: dict[str, str] = {}
