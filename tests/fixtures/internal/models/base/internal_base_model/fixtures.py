#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fixtures

This module provides a collection of fixtures related to InternalBaseModel tests.

Copyright © 2025 Leviftas authors. All rights reserved.

SPDX-License-Identifier: GPL-3.0-or-later

For the full license text, see <https://www.gnu.org/licenses/gpl-3.0.html>

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/9/29
- Modified : 2025/9/29
"""

import pytest

from pydantic import field_validator
from pydantic import Field
from typing_extensions import Type

from leviftas.internal.models.base.models import InternalBaseModel

@pytest.fixture
def str_strip_whitespace_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests str_strip_whitespace=True defined in model_config of InternalBaseModel.

    Returns:
        Type[StrStripWhitespaceTestModel]: Data model class for testing str_strip_whitespace=True
    """

    class StrStripWhitespaceTestModel(InternalBaseModel):
        """
        Test model for str_strip_whitespace functionality.

        Attributes:
            text (str): Text field that will be stripped of whitespace
        """

        text: str = Field(
            description="Text field for whitespace stripping test",
        )

    return StrStripWhitespaceTestModel


@pytest.fixture
def str_max_length_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests str_max_length=100000 defined in model_config of InternalBaseModel.

    Returns:
        Type[StrMaxLengthTestModel]: Data model class for testing str_max_length=100000
    """

    class StrMaxLengthTestModel(InternalBaseModel):
        """
        Test model for str_max_length functionality.

        Attributes:
            text (str): Test strings with str_max_length=100000
        """

        text: str = Field(
            description="Test string with str_max_length=100000",
        )

    return StrMaxLengthTestModel


@pytest.fixture
def extra_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests extra="forbid" defined in model_config of InternalBaseModel.

    Returns:
        Type[InternalBaseModel]: Data model class for testing extra="forbid"
    """

    class ExtraTestModel(InternalBaseModel):
        """
        Test model for extra="forbid" defined in model_config of InternalBaseModel.

        Attributes:
            text (str): Test strings with extra="forbid"
            number (int): Test number with extra="forbid"
        """

        text: str = Field(
            description="Test string with extra='forbid'",
        )

        number: int = Field(
            description="Test number with extra='forbid'",
        )

    return ExtraTestModel


@pytest.fixture
def frozen_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests frozen=True defined in model_config of InternalBaseModel.

    Returns:
        Type[FrozenTestModel]: Data model class for testing frozen=True (immutability)
    """

    class FrozenTestModel(InternalBaseModel):
        """
        Test model for frozen=True functionality.

        Attributes:
            text (str): Text field for testing immutability
            number (int): Number field for testing immutability
        """

        text: str = Field(
            description="Text field for testing immutability",
        )

        number: int = Field(
            description="Number field for testing immutability",
        )

    return FrozenTestModel


@pytest.fixture
def strict_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests strict=True defined in model_config of InternalBaseModel.

    Returns:
        Type[StrictTestModel]: Data model class for testing strict=True
    """

    class StrictTestModel(InternalBaseModel):
        """
        Test model for strict=True functionality.

        Attributes:
            number (int): Integer field for testing strict type validation
            boolean (bool): Boolean field for testing strict type validation
        """

        number: int = Field(
            description="Integer field for testing strict type validation",
        )

        boolean: bool = Field(
            description="Boolean field for testing strict type validation",
        )

    return StrictTestModel


@pytest.fixture
def validate_assignment_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validate_assignment=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidateAssignmentTestModel]: Data model class for testing validate_assignment=True
    """

    class ValidateAssignmentTestModel(InternalBaseModel):
        """
        Test model for validate_assignment=True functionality.

        This model is used to test that assignment validation works properly
        even after object creation.

        Attributes:
            text (str): Text field for testing assignment validation
            number (int): Number field for testing assignment validation
        """

        text: str = Field(
            description="Text field for testing assignment validation",
        )

        number: int = Field(
            ge=0,
            description="Number field for testing assignment validation (must be >= 0)",
        )

    return ValidateAssignmentTestModel


@pytest.fixture
def version_validator_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests version field validator of InternalBaseModel.

    Returns:
        Type[VersionValidatorTestModel]: Data model class for testing version validator
    """

    class VersionValidatorTestModel(InternalBaseModel):
        """
        Test model for version field validator functionality.

        This model inherits the version field and validator from InternalBaseModel
        to test the _set_version validator behavior.

        Attributes:
            name (str): Name field for identification
        """

        name: str = Field(
            description="Name field for identification",
        )

        class Meta:
            """
            Test meta class with custom version.
            
            Attributes:
                version (str): Custom version for testing
            """
            version: str = "2.5.0"

    return VersionValidatorTestModel


@pytest.fixture
def alias_generator_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests alias_generator=to_snake defined in model_config of InternalBaseModel.

    Returns:
        Type[AliasGeneratorTestModel]: Data model class for testing alias_generator=to_snake
    """

    class AliasGeneratorTestModel(InternalBaseModel):
        """
        Test model for alias_generator=to_snake functionality.

        Attributes:
            user_name (str): Field for testing camelCase to snake_case conversion
            user_age (int): Field for testing camelCase to snake_case conversion
        """

        user_name: str = Field(
            description="User name field for testing alias generation",
        )

        user_age: int = Field(
            description="User age field for testing alias generation",
        )

    return AliasGeneratorTestModel


@pytest.fixture
def from_attributes_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests from_attributes=True defined in model_config of InternalBaseModel.

    Returns:
        Type[FromAttributesTestModel]: Data model class for testing from_attributes=True
    """

    class FromAttributesTestModel(InternalBaseModel):
        """
        Test model for from_attributes=True functionality.

        Attributes:
            text (str): Text field for testing object attribute extraction
            number (int): Number field for testing object attribute extraction
        """

        text: str = Field(
            description="Text field for testing object attribute extraction",
        )

        number: int = Field(
            description="Number field for testing object attribute extraction",
        )

    return FromAttributesTestModel


@pytest.fixture
def allow_inf_nan_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests allow_inf_nan=False defined in model_config of InternalBaseModel.

    Returns:
        Type[AllowInfNanTestModel]: Data model class for testing allow_inf_nan=False
    """

    class AllowInfNanTestModel(InternalBaseModel):
        """
        Test model for allow_inf_nan=False functionality.

        Attributes:
            value (float): Float field for testing infinity and NaN rejection
        """

        value: float = Field(
            description="Float field for testing infinity and NaN rejection",
        )

    return AllowInfNanTestModel


@pytest.fixture
def coerce_numbers_to_str_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests coerce_numbers_to_str=False defined in model_config of InternalBaseModel.

    Returns:
        Type[CoerceNumbersToStrTestModel]: Data model class for testing coerce_numbers_to_str=False
    """

    class CoerceNumbersToStrTestModel(InternalBaseModel):
        """
        Test model for coerce_numbers_to_str=False functionality.

        Attributes:
            text (str): Text field for testing number to string coercion rejection
        """

        text: str = Field(
            description="Text field for testing number to string coercion rejection",
        )

    return CoerceNumbersToStrTestModel


@pytest.fixture
def validate_default_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validate_default=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidateDefaultTestModel]: Data model class for testing validate_default=True
    """

    class ValidateDefaultTestModel(InternalBaseModel):
        """
        Test model for validate_default=True functionality.

        Attributes:
            text (str): Text field with default value for testing default validation
            number (int): Number field with default value for testing default validation
        """

        text: str = Field(
            default="default_text",
            description="Text field with default value for testing default validation",
        )

        number: int = Field(
            default=42,
            ge=0,
            description="Number field with default value for testing default validation",
        )

    return ValidateDefaultTestModel


@pytest.fixture
def validate_return_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validate_return=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidateReturnTestModel]: Data model class for testing validate_return=True
    """

    class ValidateReturnTestModel(InternalBaseModel):
        """
        Test model for validate_return=True functionality.

        Attributes:
            value (str): Field with validator for testing return value validation
        """

        value: str = Field(
            description="Field with validator for testing return value validation",
        )

        @field_validator("value")
        @classmethod
        def validate_value(cls, v: str) -> str:
            """Validator that returns validated value."""
            return v.upper()

    return ValidateReturnTestModel


@pytest.fixture
def revalidate_instances_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests revalidate_instances="always" defined in model_config of InternalBaseModel.

    Returns:
        Type[RevalidateInstancesTestModel]: Data model class for testing revalidate_instances="always"
    """

    class RevalidateInstancesTestModel(InternalBaseModel):
        """
        Test model for revalidate_instances="always" functionality.

        Attributes:
            text (str): Text field for testing revalidation
            number (int): Number field for testing revalidation
        """

        text: str = Field(
            description="Text field for testing revalidation",
        )

        number: int = Field(
            description="Number field for testing revalidation",
        )

    return RevalidateInstancesTestModel


@pytest.fixture
def use_enum_values_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests use_enum_values=True defined in model_config of InternalBaseModel.

    Returns:
        Type[UseEnumValuesTestModel]: Data model class for testing use_enum_values=True
    """

    from enum import Enum

    class Status(str, Enum):
        ACTIVE = "active"
        INACTIVE = "inactive"

    class UseEnumValuesTestModel(InternalBaseModel):
        """
        Test model for use_enum_values=True functionality.

        Attributes:
            status (Status): Enum field for testing enum value serialization
        """

        status: Status = Field(
            description="Enum field for testing enum value serialization",
        )

    return UseEnumValuesTestModel


@pytest.fixture
def arbitrary_types_allowed_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests arbitrary_types_allowed=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ArbitraryTypesAllowedTestModel]: Data model class for testing arbitrary_types_allowed=True
    """

    from datetime import date

    class ArbitraryTypesAllowedTestModel(InternalBaseModel):
        """
        Test model for arbitrary_types_allowed=True functionality.

        Attributes:
            custom_object (object): Custom object field for testing arbitrary type support
            date_field (date): Date field for testing arbitrary type support
        """

        custom_object: object = Field(
            description="Custom object field for testing arbitrary type support",
        )

        date_field: date = Field(
            description="Date field for testing arbitrary type support",
        )

    return ArbitraryTypesAllowedTestModel


@pytest.fixture
def validate_by_alias_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validate_by_alias=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidateByAliasTestModel]: Data model class for testing validate_by_alias=True
    """

    class ValidateByAliasTestModel(InternalBaseModel):
        """
        Test model for validate_by_alias=True functionality.

        Attributes:
            user_name (str): Field with alias for testing alias validation
        """

        user_name: str = Field(
            alias="userName",
            description="Field with alias for testing alias validation",
        )

    return ValidateByAliasTestModel


@pytest.fixture
def validate_by_name_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validate_by_name=False defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidateByNameTestModel]: Data model class for testing validate_by_name=False
    """

    class ValidateByNameTestModel(InternalBaseModel):
        """
        Test model for validate_by_name=False functionality.

        Attributes:
            user_name (str): Field with alias for testing name validation rejection
        """

        user_name: str = Field(
            alias="userName",
            description="Field with alias for testing name validation rejection",
        )

    return ValidateByNameTestModel


@pytest.fixture
def loc_by_alias_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests loc_by_alias=True defined in model_config of InternalBaseModel.

    Returns:
        Type[LocByAliasTestModel]: Data model class for testing loc_by_alias=True
    """

    class LocByAliasTestModel(InternalBaseModel):
        """
        Test model for loc_by_alias=True functionality.

        Attributes:
            user_name (str): Field with alias for testing error location reporting
        """

        user_name: str = Field(
            alias="userName",
            min_length=3,
            description="Field with alias for testing error location reporting",
        )

    return LocByAliasTestModel


@pytest.fixture
def ser_json_bytes_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests ser_json_bytes="base64" defined in model_config of InternalBaseModel.

    Returns:
        Type[SerJsonBytesTestModel]: Data model class for testing ser_json_bytes="base64"
    """

    class SerJsonBytesTestModel(InternalBaseModel):
        """
        Test model for ser_json_bytes="base64" functionality.

        Attributes:
            data (bytes): Bytes field for testing base64 serialization
        """

        data: bytes = Field(
            description="Bytes field for testing base64 serialization",
        )

    return SerJsonBytesTestModel


@pytest.fixture
def val_json_bytes_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests val_json_bytes="base64" defined in model_config of InternalBaseModel.

    Returns:
        Type[ValJsonBytesTestModel]: Data model class for testing val_json_bytes="base64"
    """

    class ValJsonBytesTestModel(InternalBaseModel):
        """
        Test model for val_json_bytes="base64" functionality.

        Attributes:
            data (bytes): Bytes field for testing base64 deserialization
        """

        data: bytes = Field(
            description="Bytes field for testing base64 deserialization",
        )

        @field_validator("data", mode="before")
        @classmethod
        def validate_data(cls, v):
            """Custom validator to handle base64 strings."""
            if isinstance(v, str):
                import base64
                try:
                    return base64.b64decode(v)
                except Exception:
                    pass
            return v

    return ValJsonBytesTestModel


@pytest.fixture
def regex_engine_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests regex_engine="rust-regex" defined in model_config of InternalBaseModel.

    Returns:
        Type[RegexEngineTestModel]: Data model class for testing regex_engine="rust-regex"
    """

    from pydantic import StringConstraints
    from typing_extensions import Annotated

    class RegexEngineTestModel(InternalBaseModel):
        """
        Test model for regex_engine="rust-regex" functionality.

        Attributes:
            pattern_field (str): String field with regex pattern for testing rust regex engine
        """

        pattern_field: Annotated[str, StringConstraints(pattern=r'^[a-zA-Z0-9]+$')] = Field(
            description="String field with regex pattern for testing rust regex engine",
        )

    return RegexEngineTestModel


@pytest.fixture
def defer_build_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests defer_build=True defined in model_config of InternalBaseModel.

    Returns:
        Type[DeferBuildTestModel]: Data model class for testing defer_build=True
    """

    class DeferBuildTestModel(InternalBaseModel):
        """
        Test model for defer_build=True functionality.

        Attributes:
            name (str): Simple field for testing deferred building
        """

        name: str = Field(
            description="Simple field for testing deferred building",
        )

    return DeferBuildTestModel


@pytest.fixture
def cache_strings_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests cache_strings="keys" defined in model_config of InternalBaseModel.

    Returns:
        Type[CacheStringsTestModel]: Data model class for testing cache_strings="keys"
    """

    class CacheStringsTestModel(InternalBaseModel):
        """
        Test model for cache_strings="keys" functionality.

        Attributes:
            field1 (str): First string field for testing string caching
            field2 (str): Second string field for testing string caching
        """

        field_1: str = Field(
            description="First string field for testing string caching",
        )

        field_2: str = Field(
            description="Second string field for testing string caching",
        )

    return CacheStringsTestModel


@pytest.fixture
def hide_input_in_errors_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests hide_input_in_errors=False defined in model_config of InternalBaseModel.

    Returns:
        Type[HideInputInErrorsTestModel]: Data model class for testing hide_input_in_errors=False
    """

    class HideInputInErrorsTestModel(InternalBaseModel):
        """
        Test model for hide_input_in_errors=False functionality.

        Attributes:
            number (int): Integer field for testing error input visibility
        """

        number: int = Field(
            ge=0,
            description="Integer field for testing error input visibility",
        )

    return HideInputInErrorsTestModel


@pytest.fixture
def validation_error_cause_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests validation_error_cause=True defined in model_config of InternalBaseModel.

    Returns:
        Type[ValidationErrorCauseTestModel]: Data model class for testing validation_error_cause=True
    """

    class ValidationErrorCauseTestModel(InternalBaseModel):
        """
        Test model for validation_error_cause=True functionality.

        Attributes:
            value (str): String field for testing error cause display
        """

        value: str = Field(
            min_length=5,
            description="String field for testing error cause display",
        )

    return ValidationErrorCauseTestModel


@pytest.fixture
def use_attribute_docstrings_test_model() -> Type[InternalBaseModel]:
    """
    Provide a test model that tests use_attribute_docstrings=True defined in model_config of InternalBaseModel.

    Returns:
        Type[UseAttributeDocstringsTestModel]: Data model class for testing use_attribute_docstrings=True
    """

    class UseAttributeDocstringsTestModel(InternalBaseModel):
        """
        Test model for use_attribute_docstrings=True functionality.

        Attributes:
            documented_field (str): Field with docstring for testing attribute documentation
        """

        documented_field: str
        """This field has a docstring that should be used as description."""

    return UseAttributeDocstringsTestModel


