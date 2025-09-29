#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mock_data

This module provides all the test data required to test InternalBaseModel.

Copyright © 2025 Leviftas authors. All rights reserved.

SPDX-License-Identifier: GPL-3.0-or-later

For the full license text, see <https://www.gnu.org/licenses/gpl-3.0.html>

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/9/29
- Modified : 2025/9/29
"""

import pytest
from datetime import datetime, timezone

from typing_extensions import List


class InternalBaseModelTestData:
    """
    Data classes required for InternalBaseModel testing.

    This class contains all test data sets used for validating
    InternalBaseModel functionality and configuration options.

    Attributes:
        STR_STRIP_WHITESPACE_TEST_DATA (List[pytest.param]): Test data for str_strip_whitespace=True validation
        STR_MAX_LENGTH_VALID_TEST_DATA (List[pytest.param]): Test data for valid string length validation (≤100000)
        STR_MAX_LENGTH_INVALID_TEST_DATA (List[pytest.param]): Test data for invalid string length validation (>100000)
        EXTRA_FORBID_INVALID_TEST_DATA (List[pytest.param]): Test data for extra="forbid" validation with invalid inputs
        EXTRA_FORBID_VALID_TEST_DATA (List[pytest.param]): Test data for extra="forbid" validation with valid inputs
        FROZEN_VALID_TEST_DATA (List[pytest.param]): Test data for frozen=False validation (model creation)
        FROZEN_MODIFICATION_TEST_DATA (List[pytest.param]): Test data for frozen=False validation (field modification)
        STRICT_VALID_TEST_DATA (List[pytest.param]): Test data for strict=True validation with valid types
        STRICT_INVALID_TEST_DATA (List[pytest.param]): Test data for strict=True validation with invalid types
        VALIDATE_ASSIGNMENT_VALID_TEST_DATA (List[pytest.param]): Test data for validate_assignment=True with valid values
        VALIDATE_ASSIGNMENT_INVALID_TEST_DATA (List[pytest.param]): Test data for validate_assignment=True with invalid values
        VERSION_VALIDATOR_TEST_DATA (List[pytest.param]): Test data for version field validator with default Meta
        VERSION_VALIDATOR_CUSTOM_META_TEST_DATA (List[pytest.param]): Test data for version field validator with custom Meta
        ALIAS_GENERATOR_TEST_DATA (List[pytest.param]): Test data for alias_generator=to_snake configuration
        FROM_ATTRIBUTES_TEST_DATA (List[pytest.param]): Test data for from_attributes=True configuration
        ALLOW_INF_NAN_INVALID_TEST_DATA (List[pytest.param]): Test data for allow_inf_nan=False validation
        COERCE_NUMBERS_TO_STR_INVALID_TEST_DATA (List[pytest.param]): Test data for coerce_numbers_to_str=False validation
        VALIDATE_DEFAULT_TEST_DATA (List[pytest.param]): Test data for validate_default=True configuration
        REVALIDATE_INSTANCES_TEST_DATA (List[pytest.param]): Test data for revalidate_instances='always' configuration
    """

    STR_STRIP_WHITESPACE_TEST_DATA: List[pytest.param] = [
        pytest.param("    Tom    ", "Tom", id="str_strip_whitespace_both_sides"),
        pytest.param("Tom", "Tom", id="str_strip_whitespace_no_change"),
        pytest.param("    Hello World", "Hello World", id="str_strip_whitespace_leading_only"),
        pytest.param("Hello World    ", "Hello World", id="str_strip_whitespace_trailing_only"),
        pytest.param("\n\tJohn\r\n", "John", id="str_strip_whitespace_mixed_chars"),
        pytest.param("  Multiple   Spaces  ", "Multiple   Spaces", id="str_strip_whitespace_preserve_internal"),
        pytest.param("", "", id="str_strip_whitespace_empty_string"),
        pytest.param("   ", "", id="str_strip_whitespace_only_spaces"),
    ]

    STR_MAX_LENGTH_VALID_TEST_DATA: List[pytest.param] = [
        pytest.param("a" * 100000, 100000, id="str_max_length_valid_at_limit"),
        pytest.param("a" * 99999, 99999, id="str_max_length_valid_near_limit"),
        pytest.param("a" * 50000, 50000, id="str_max_length_valid_half_limit"),
        pytest.param("a" * 1000, 1000, id="str_max_length_valid_small"),
        pytest.param("", 0, id="str_max_length_valid_empty"),
        pytest.param("Hello", 5, id="str_max_length_valid_simple_text"),
        pytest.param("Test123", 7, id="str_max_length_valid_alphanumeric"),
    ]

    STR_MAX_LENGTH_INVALID_TEST_DATA: List[pytest.param] = [
        pytest.param("a" * 100001, 100001, id="str_max_length_invalid_over_by_one"),
        pytest.param("a" * 150000, 150000, id="str_max_length_invalid_significantly_over"),
        pytest.param("a" * 200000, 200000, id="str_max_length_invalid_double_limit"),
    ]

    EXTRA_FORBID_INVALID_TEST_DATA: List[pytest.param] = [
        # Single extra field test
        pytest.param(
            {"text": "valid_text", "number": 42, "extra_field": "not_allowed"},
            "extra_field",
            id="extra_forbid_single_extra_field"
        ),

        # Multiple extra fields test
        pytest.param(
            {"text": "valid_text", "number": 42, "field1": "extra1", "field2": "extra2"},
            "field1",
            id="extra_forbid_multiple_extra_fields"
        ),

        # Extra field with None value test
        pytest.param(
            {"text": "valid_text", "number": 42, "unknown_field": None},
            "unknown_field",
            id="extra_forbid_none_value_extra"
        ),

        # Extra field with empty string test
        pytest.param(
            {"text": "valid_text", "number": 42, "empty_field": ""},
            "empty_field",
            id="extra_forbid_empty_string_extra"
        ),

        # Extra field with numeric value test
        pytest.param(
            {"text": "valid_text", "number": 42, "numeric_extra": 999},
            "numeric_extra",
            id="extra_forbid_numeric_extra"
        ),

        # Extra field with list value test
        pytest.param(
            {"text": "valid_text", "number": 42, "list_extra": [1, 2, 3]},
            "list_extra",
            id="extra_forbid_list_extra"
        ),

        # Extra field with dict value test
        pytest.param(
            {"text": "valid_text", "number": 42, "dict_extra": {"key": "value"}},
            "dict_extra",
            id="extra_forbid_dict_extra"
        ),

        # Extra field with boolean value test
        pytest.param(
            {"text": "valid_text", "number": 42, "bool_extra": True},
            "bool_extra",
            id="extra_forbid_boolean_extra"
        ),

        # Common typo field simulation
        pytest.param(
            {"text": "valid_text", "number": 42, "txt": "typo"},
            "txt",
            id="extra_forbid_typo_field"
        ),

        # Version field typo simulation
        pytest.param(
            {"text": "valid_text", "number": 42, "versoin": "1.0.0"},
            "versoin",
            id="extra_forbid_version_typo"
        ),

        # Created field typo simulation
        pytest.param(
            {"text": "valid_text", "number": 42, "created": "2025-01-01"},
            "created",
            id="extra_forbid_created_typo"
        ),

        # Case sensitivity test
        pytest.param(
            {"text": "valid_text", "number": 42, "TEXT": "uppercase"},
            "TEXT",
            id="extra_forbid_case_sensitive"
        ),
    ]

    EXTRA_FORBID_VALID_TEST_DATA: List[pytest.param] = [
        # Valid data with required fields only
        pytest.param(
            {"text": "valid_text", "number": 42},
            id="extra_forbid_valid_required_only"
        ),

        # Valid data with inherited fields
        pytest.param(
            {"text": "valid_text", "number": 42, "version": "2.0.0"},
            id="extra_forbid_valid_with_version"
        ),

        # Valid data with all legal fields
        pytest.param(
            {
                "text": "valid_text",
                "number": 42,
                "version": "1.0.0",
                "created_at": datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            },
            id="extra_forbid_valid_all_fields"
        ),

        # Boundary values test
        pytest.param(
            {"text": "", "number": 0},
            id="extra_forbid_valid_boundary_values"
        ),

        # Maximum length string test
        pytest.param(
            {"text": "a" * 100000, "number": 999999},
            id="extra_forbid_valid_max_length"
        ),
    ]

    FROZEN_VALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": "immutable_text", "number": 42},
            id="frozen_valid_creation"
        ),
        pytest.param(
            {"text": "test", "number": 0},
            id="frozen_valid_boundary"
        ),
    ]

    FROZEN_MODIFICATION_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": "original", "number": 1},
            "text",
            "modified",
            id="frozen_modify_text_field"
        ),
        pytest.param(
            {"text": "original", "number": 1},
            "number",
            999,
            id="frozen_modify_number_field"
        ),
    ]

    STRICT_VALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"number": 42, "boolean": True},
            id="strict_valid_correct_types"
        ),
        pytest.param(
            {"number": 0, "boolean": False},
            id="strict_valid_boundary_values"
        ),
        pytest.param(
            {"number": -999, "boolean": True},
            id="strict_valid_negative_number"
        ),
    ]

    STRICT_INVALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"number": "42", "boolean": True},
            "number",
            id="strict_invalid_string_as_number"
        ),
        pytest.param(
            {"number": 42, "boolean": "true"},
            "boolean",
            id="strict_invalid_string_as_boolean"
        ),
        pytest.param(
            {"number": 42.5, "boolean": True},
            "number",
            id="strict_invalid_float_as_int"
        ),
        pytest.param(
            {"number": 42, "boolean": 1},
            "boolean",
            id="strict_invalid_int_as_boolean"
        ),
        pytest.param(
            {"number": None, "boolean": True},
            "number",
            id="strict_invalid_none_as_number"
        ),
    ]

    VALIDATE_ASSIGNMENT_VALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": "valid", "number": 5},
            "text",
            "new_valid_text",
            id="validate_assignment_valid_text_change"
        ),
        pytest.param(
            {"text": "valid", "number": 5},
            "number",
            10,
            id="validate_assignment_valid_number_change"
        ),
    ]

    VALIDATE_ASSIGNMENT_INVALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": "valid", "number": 5},
            "number",
            -1,
            id="validate_assignment_invalid_negative_number"
        ),
        pytest.param(
            {"text": "valid", "number": 5},
            "text",
            "",
            id="validate_assignment_invalid_empty_text"
        ),
    ]

    VERSION_VALIDATOR_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"name": "test1"},
            None,
            "2.5.0",
            id="version_validator_default_meta_version"
        ),
        pytest.param(
            {"name": "test2", "version": ""},
            "",
            "2.5.0",
            id="version_validator_empty_string_version"
        ),
        pytest.param(
            {"name": "test3", "version": "3.0.0"},
            "3.0.0",
            "3.0.0",
            id="version_validator_explicit_version"
        ),
    ]

    VERSION_VALIDATOR_CUSTOM_META_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"name": "test_custom"},
            None,
            "2.5.0",
            id="version_validator_custom_meta_version"
        ),
        pytest.param(
            {"name": "test_custom", "version": ""},
            "",
            "2.5.0",
            id="version_validator_custom_meta_empty_override"
        ),
    ]

    ALIAS_GENERATOR_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"user_name": "john", "user_age": 25},
            {"user_name": "john", "user_age": 25},
            id="alias_generator_snake_case_input"
        ),
    ]

    FROM_ATTRIBUTES_TEST_DATA: List[pytest.param] = [
        pytest.param(
            type("TestObj", (), {"text": "attr_text", "number": 42})(),
            {"text": "attr_text", "number": 42},
            id="from_attributes_object_properties"
        ),
    ]

    ALLOW_INF_NAN_INVALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"value": float("inf")},
            id="allow_inf_nan_infinity"
        ),
        pytest.param(
            {"value": float("-inf")},
            id="allow_inf_nan_negative_infinity"
        ),
        pytest.param(
            {"value": float("nan")},
            id="allow_inf_nan_not_a_number"
        ),
    ]

    COERCE_NUMBERS_TO_STR_INVALID_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": 123},
            id="coerce_numbers_to_str_int_as_string"
        ),
        pytest.param(
            {"text": 45.67},
            id="coerce_numbers_to_str_float_as_string"
        ),
    ]

    VALIDATE_DEFAULT_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {},
            id="validate_default_use_defaults"
        ),
    ]

    REVALIDATE_INSTANCES_TEST_DATA: List[pytest.param] = [
        pytest.param(
            {"text": "test", "number": 42},
            id="revalidate_instances_basic_data"
        ),
    ]