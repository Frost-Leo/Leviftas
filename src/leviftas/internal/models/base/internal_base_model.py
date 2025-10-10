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

This module provides an internal base model that inherits from Pydantic's BaseModel.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/10 
- Modified : 2025/10/10

"""

from datetime import datetime, timezone

from pydantic import field_validator
from pydantic.alias_generators import to_snake
from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import ClassVar, Optional


class InternalBaseModel(BaseModel):
    """
    The foundational data model for internal running programs in Leviftas.

    This base model provides comprehensive configuration for all internal system models,
    ensuring strict validation, type safety, and consistent behavior throughout the system.

    Attributes:
        model_config (ClassVar[ConfigDict]): Configuration dictionary that enforces strict validation,
            type safety, and consistent behavior across all internal system models. Includes settings
            for string handling, validation modes, serialization behavior, and performance optimizations.
        version (str): The version of the model. Defaults to "1.0.0" or the value defined in Meta.version
            if not explicitly provided.
        created_at (datetime): Creation timestamp of the model in UTC timezone. Automatically set to
            the current UTC time when the instance is created.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(

        # Trim leading and trailing whitespace from string
        str_strip_whitespace=True,

        # Limit string length to prevent DoS attacks
        str_max_length=100000,

        # Prohibit adding additional fields to ensure model security
        extra="forbid",

        # After creating an instance, modifications are allowed
        frozen=False,

        # Strict mode validation
        strict=True,

        # Validation is also required when modifying model attributes
        validate_assignment=True,

        # Validate default values during validation
        validate_default=True,

        # Verify return value from validators
        validate_return=True,

        # Maintain the refresh effect at all times to prevent data tampering
        revalidate_instances="always",

        # Use enum values instead of enum objects
        use_enum_values=True,

        # Allow non-Pydantic standard types for ORM compatibility
        arbitrary_types_allowed=True,

        # Disallow infinity and NaN values
        allow_inf_nan=False,

        # Prohibit implicit conversion from number to string
        coerce_numbers_to_str=False,

        # Allow model instances to be constructed from object properties
        from_attributes=True,

        # Generate snake_case aliases for all fields
        alias_generator=to_snake,

        # Allow validation using field aliases
        validate_by_alias=True,

        # Disallow validation using original field names
        validate_by_name=False,

        # Use aliases in error locations
        loc_by_alias=True,

        # Safe byte serialization format
        ser_json_bytes="base64",

        # Matching byte deserialization format
        val_json_bytes="base64",

        # Rust regex engine is more resistant to ReDoS attacks
        regex_engine="rust-regex",

        # Enable delayed building to improve performance
        defer_build=True,

        # Cache dictionary keys for better performance
        cache_strings="keys",

        # Show error details for debugging purposes
        hide_input_in_errors=False,

        # Display the original error cause
        validation_error_cause=True,

        # Use attribute docstrings as field descriptions
        use_attribute_docstrings=True,
    )

    version: str = Field(
        default="",
        description="The version of the model"
    )

    created_at: datetime = Field(
        default_factory=lambda : datetime.now(tz=timezone.utc),
        description="Model creation timestamp",
    )

    class Meta:
        """
        Internal classes that store model metadata

        Attributes:
            version (str): Model version number
        """

        version: str = "1.0.0"

    @field_validator("version", mode="before")
    @classmethod
    def _set_version(cls, v: Optional[str]) -> str:
        """
        Set values for the version field of the model.

        Args:
            v (Optional[str]): The version of the model (can be None or empty string)

        Returns:
            str: The version of the model
        """
        if not v:
            return getattr(cls.Meta, "version", "1.0.0") if hasattr(cls, "Meta") else "1.0.0"
        return v
