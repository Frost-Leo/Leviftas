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

test_internal_base_model.py

This module provides comprehensive unit tests for InternalBaseModel.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/10 
- Modified : 2025/10/10

"""

import pytest
from logging import getLogger

from pydantic import ValidationError
from typing_extensions import Type

from leviftas.internal.models.base.models import InternalBaseModel
from tests.fixtures.internal.models.base.internal_base_model.mock_data import InternalBaseModelTestData

logger = getLogger(__name__)


@pytest.mark.internal
class TestInternalBaseModel:
    """
    InternalBaseModel's unit test class.

    This class contains comprehensive tests for all functionality
    and configuration options of InternalBaseModel.
    """

    class TestModelConfig:
        """
        Test the configuration of model_config of InternalBaseModel.

        This nested class tests all the configuration options defined
        in the model_config of InternalBaseModel.
        """

        @pytest.mark.parametrize(
            "input_text,expected_text",
            InternalBaseModelTestData.STR_STRIP_WHITESPACE_TEST_DATA
        )
        def test_str_strip_whitespace(
                self,
                input_text: str,
                expected_text: str,
                str_strip_whitespace_test_model: Type[InternalBaseModel]
        ):
            """
            Test str_strip_whitespace=True configuration.

            Args:
                input_text (str): Input string with potential whitespace
                expected_text (str): Expected string after whitespace stripping
                str_strip_whitespace_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = str_strip_whitespace_test_model(text=input_text)

            assert instance.text == expected_text

            logger.info(f"Input: '{input_text}' -> Output: '{instance.text}' (Expected: '{expected_text}')")

        @pytest.mark.parametrize(
            "input_text,expected_length",
            InternalBaseModelTestData.STR_MAX_LENGTH_VALID_TEST_DATA
        )
        def test_str_max_length_valid(
                self,
                input_text: str,
                expected_length: int,
                str_max_length_test_model: Type[InternalBaseModel]
        ):
            """
            Test str_max_length=100000 configuration with valid inputs.

            Args:
                input_text (str): Input string within length limit
                expected_length (int): Expected length of the input string
                str_max_length_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = str_max_length_test_model(text=input_text)

            assert instance.text == input_text
            assert len(instance.text) == expected_length
            assert len(instance.text) <= 100000

            logger.info(
                f"Valid length test passed: text length {len(instance.text)} equals {expected_length} characters, no more than 100,000 characters")

        @pytest.mark.parametrize(
            "input_text,expected_length",
            InternalBaseModelTestData.STR_MAX_LENGTH_INVALID_TEST_DATA
        )
        def test_str_max_length_invalid(
                self,
                input_text: str,
                expected_length: int,
                str_max_length_test_model: Type[InternalBaseModel]
        ):
            """
            Test str_max_length=100000 configuration with invalid inputs.

            Args:
                input_text (str): Input string within length limit
                expected_length (int): Expected length of the input string
                str_max_length_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            with pytest.raises(ValidationError) as exc_info:
                str_max_length_test_model(text=input_text)

            error_message = str(exc_info.value)

            assert "String should have at most 100000 characters" in error_message

            assert expected_length > 100000

            logger.info(f"Invalid length test passed: {expected_length} characters correctly rejected")

        @pytest.mark.parametrize(
            "invalid_data,expected_extra_field",
            InternalBaseModelTestData.EXTRA_FORBID_INVALID_TEST_DATA
        )
        def test_extra_forbid_invalid(
                self,
                invalid_data: dict,
                expected_extra_field: str,
                extra_test_model: Type[InternalBaseModel]
        ):
            """
            Test extra='forbid' configuration with invalid inputs containing extra fields.

            Args:
                invalid_data (dict): Dictionary containing extra fields that should be rejected
                expected_extra_field (str): The extra field name that should cause validation error
                extra_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            with pytest.raises(ValidationError) as exc_info:
                extra_test_model(**invalid_data)

            error_message = str(exc_info.value)
            assert "Extra inputs are not permitted" in error_message

            errors = exc_info.value.errors()
            extra_field_errors = [
                error for error in errors
                if expected_extra_field in str(error.get('loc', []))
            ]
            assert len(extra_field_errors) > 0

            logger.info(f"Extra field validation correctly failed for field '{expected_extra_field}': {invalid_data}")

        @pytest.mark.parametrize(
            "valid_data",
            InternalBaseModelTestData.EXTRA_FORBID_VALID_TEST_DATA
        )
        def test_extra_forbid_valid(
                self,
                valid_data: dict,
                extra_test_model: Type[InternalBaseModel]
        ):
            """
            Test extra='forbid' configuration with valid inputs containing no extra fields.

            Args:
                valid_data (dict): Dictionary containing only valid fields that should be accepted
                extra_test_model (Type[InternalBaseModel]): Test model class from fixture for testing extra field validation

            """
            instance = extra_test_model(**valid_data)

            assert instance.text == valid_data["text"]
            assert instance.number == valid_data["number"]

            if "version" in valid_data:
                assert instance.version == valid_data["version"]
            else:
                assert instance.version == "1.0.0"

            text_info = f"text(len:{len(valid_data['text'])})" if len(
                valid_data["text"]) > 50 else f"text:'{valid_data['text']}'"
            other_fields = {k: v for k, v in valid_data.items() if k != "text"}

            logger.info(f"Extra field validation passed - {text_info}, other_fields: {other_fields}")

        def test_frozen_config(
                self,
                frozen_test_model: Type[InternalBaseModel]
        ):
            """
            Test frozen=False configuration - model mutability.

            Args:
                frozen_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Create instance
            instance = frozen_test_model(text="original", number=42)

            # Modify attributes - should work because frozen=False
            instance.text = "modified"
            instance.number = 99

            # Verify values were changed
            assert instance.text == "modified"
            assert instance.number == 99

            logger.info("Frozen=False test passed - model is mutable")

        @pytest.mark.parametrize(
            "valid_data",
            InternalBaseModelTestData.STRICT_VALID_TEST_DATA
        )
        def test_strict_config_valid(
                self,
                valid_data: dict,
                strict_test_model: Type[InternalBaseModel]
        ):
            """
            Test strict=True configuration with valid inputs.

            Args:
                valid_data (dict): Valid data that should pass strict validation
                strict_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = strict_test_model(**valid_data)

            assert instance.number == valid_data["number"]
            assert instance.boolean == valid_data["boolean"]

            logger.info(f"Strict mode validation passed with valid data: {valid_data}")

        @pytest.mark.parametrize(
            "invalid_data,invalid_field",
            InternalBaseModelTestData.STRICT_INVALID_TEST_DATA
        )
        def test_strict_config_invalid(
                self,
                invalid_data: dict,
                invalid_field: str,
                strict_test_model: Type[InternalBaseModel]
        ):
            """
            Test strict=True configuration with invalid inputs.

            Args:
                invalid_data (dict): Invalid data that should fail strict validation
                invalid_field (str): The field that should cause validation error
                strict_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            with pytest.raises(ValidationError) as exc_info:
                strict_test_model(**invalid_data)

            errors = exc_info.value.errors()
            field_errors = [
                error for error in errors
                if invalid_field in str(error.get('loc', []))
            ]
            assert len(field_errors) > 0

            logger.info(f"Strict mode correctly rejected invalid type for field '{invalid_field}': {invalid_data}")

        def test_validate_assignment_config(
                self,
                validate_assignment_test_model: Type[InternalBaseModel]
        ):
            """
            Test validate_assignment=True configuration.

            Args:
                validate_assignment_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Create instance with valid data
            instance = validate_assignment_test_model(text="initial", number=5)

            # Valid assignment should work
            instance.text = "updated"
            instance.number = 10

            assert instance.text == "updated"
            assert instance.number == 10

            # Invalid assignment should raise error
            with pytest.raises(ValidationError) as exc_info:
                instance.number = -1  # violates ge=0 constraint

            error_message = str(exc_info.value)
            assert "greater than or equal to 0" in error_message

            # Value should remain unchanged after failed validation
            assert instance.number == 10

            logger.info("Validate assignment test passed - assignment validation working correctly")

        @pytest.mark.parametrize(
            "initial_data,provided_version,expected_version",
            InternalBaseModelTestData.VERSION_VALIDATOR_TEST_DATA
        )
        def test_version_validator(
                self,
                initial_data: dict,
                provided_version: str,
                expected_version: str,
                version_validator_test_model: Type[InternalBaseModel]
        ):
            """
            Test version field validator functionality.

            Args:
                initial_data (dict): Initial data for model creation
                provided_version (str): Version value provided (if any)
                expected_version (str): Expected version after validation
                version_validator_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            if provided_version is not None:
                initial_data["version"] = provided_version

            instance = version_validator_test_model(**initial_data)

            assert instance.version == expected_version

            logger.info(f"Version validator test passed - provided: {provided_version}, expected: {expected_version}")

        @pytest.mark.parametrize(
            "initial_data,provided_version,expected_version",
            InternalBaseModelTestData.VERSION_VALIDATOR_CUSTOM_META_TEST_DATA
        )
        def test_version_validator_custom_meta(
                self,
                initial_data: dict,
                provided_version: str,
                expected_version: str,
                version_validator_test_model: Type[InternalBaseModel]
        ):
            """
            Test version field validator with custom Meta.version.

            Args:
                initial_data (dict): Initial data for model creation
                provided_version (str): Version value provided (if any)
                expected_version (str): Expected version after validation
                version_validator_test_model (Type[InternalBaseModel]): Test model with custom Meta.version
            """
            if provided_version is not None:
                initial_data["version"] = provided_version

            instance = version_validator_test_model(**initial_data)

            assert instance.version == expected_version
            assert hasattr(instance, 'Meta')
            assert instance.Meta.version == "2.5.0"

            logger.info(f"Custom Meta version test passed - provided: {provided_version}, expected: {expected_version}")

        @pytest.mark.parametrize(
            "input_data,expected_data",
            InternalBaseModelTestData.ALIAS_GENERATOR_TEST_DATA
        )
        def test_alias_generator_config(
                self,
                input_data: dict,
                expected_data: dict,
                alias_generator_test_model: Type[InternalBaseModel]
        ):
            """
            Test alias_generator=to_snake configuration.

            Args:
                input_data (dict): Input data with camelCase or PascalCase keys
                expected_data (dict): Expected data after snake_case conversion
                alias_generator_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Create instance using camelCase/PascalCase aliases
            instance = alias_generator_test_model(**input_data)

            # Verify fields are accessible with snake_case names
            assert instance.user_name == expected_data["user_name"]
            assert instance.user_age == expected_data["user_age"]

            # Verify serialization uses snake_case
            serialized = instance.model_dump()
            assert "user_name" in serialized
            assert "user_age" in serialized

            logger.info(f"Alias generator test passed - input: {input_data}, output: {serialized}")

        @pytest.mark.parametrize(
            "test_object,expected_data",
            InternalBaseModelTestData.FROM_ATTRIBUTES_TEST_DATA
        )
        def test_from_attributes_config(
                self,
                test_object,
                expected_data: dict,
                from_attributes_test_model: Type[InternalBaseModel]
        ):
            """
            Test from_attributes=True configuration.

            Args:
                test_object: Object with attributes to extract
                expected_data (dict): Expected data after attribute extraction
                from_attributes_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Create instance from object attributes
            instance = from_attributes_test_model.model_validate(test_object)

            assert instance.text == expected_data["text"]
            assert instance.number == expected_data["number"]

            logger.info(f"From attributes test passed - extracted: {expected_data}")

        @pytest.mark.parametrize(
            "invalid_data",
            InternalBaseModelTestData.ALLOW_INF_NAN_INVALID_TEST_DATA
        )
        def test_allow_inf_nan_config(
                self,
                invalid_data: dict,
                allow_inf_nan_test_model: Type[InternalBaseModel]
        ):
            """
            Test allow_inf_nan=False configuration.

            Args:
                invalid_data (dict): Data containing infinity or NaN values
                allow_inf_nan_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            with pytest.raises(ValidationError) as exc_info:
                allow_inf_nan_test_model(**invalid_data)

            error_message = str(exc_info.value)
            assert "finite number" in error_message.lower()

            logger.info(f"Allow inf/nan test passed - correctly rejected: {invalid_data}")

        @pytest.mark.parametrize(
            "invalid_data",
            InternalBaseModelTestData.COERCE_NUMBERS_TO_STR_INVALID_TEST_DATA
        )
        def test_coerce_numbers_to_str_config(
                self,
                invalid_data: dict,
                coerce_numbers_to_str_test_model: Type[InternalBaseModel]
        ):
            """
            Test coerce_numbers_to_str=False configuration.

            Args:
                invalid_data (dict): Data with numbers where strings are expected
                coerce_numbers_to_str_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            with pytest.raises(ValidationError) as exc_info:
                coerce_numbers_to_str_test_model(**invalid_data)

            error_message = str(exc_info.value)
            assert "str" in error_message

            logger.info(f"Coerce numbers to str test passed - correctly rejected: {invalid_data}")

        def test_validate_default_config(
                self,
                validate_default_test_model: Type[InternalBaseModel]
        ):
            """
            Test validate_default=True configuration.

            Args:
                validate_default_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Create instance without providing values - should use validated defaults
            instance = validate_default_test_model()

            assert instance.text == "default_text"
            assert instance.number == 42

            # Create with partial data
            instance2 = validate_default_test_model(text="custom")
            assert instance2.text == "custom"
            assert instance2.number == 42

            logger.info("Validate default test passed - default values properly validated")

        def test_use_enum_values_config(
                self,
                use_enum_values_test_model: Type[InternalBaseModel]
        ):
            """
            Test use_enum_values=True configuration.

            Args:
                use_enum_values_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            from enum import Enum

            # Get the Status enum from the test model
            Status = use_enum_values_test_model.__annotations__['status']

            instance = use_enum_values_test_model(status=Status.ACTIVE)

            # Should serialize to enum value, not enum object
            serialized = instance.model_dump()
            assert serialized["status"] == "active"
            assert isinstance(serialized["status"], str)

            logger.info("Use enum values test passed - enum serialized to value")

        def test_validate_return_config(
                self,
                validate_return_test_model: Type[InternalBaseModel]
        ):
            """
            Test validate_return=True configuration.

            Args:
                validate_return_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = validate_return_test_model(value="hello")

            # Validator should return uppercase value
            assert instance.value == "HELLO"

            logger.info("Validate return test passed - validator return value validated")

        def test_revalidate_instances_config(
                self,
                revalidate_instances_test_model: Type[InternalBaseModel]
        ):
            """
            Test revalidate_instances='always' configuration.

            Args:
                revalidate_instances_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = revalidate_instances_test_model(text="test", number=42)

            # Test that instance can be created and validated multiple times
            assert instance.text == "test"
            assert instance.number == 42

            logger.info("Revalidate instances test passed - instances revalidated correctly")

        def test_arbitrary_types_allowed_config(
                self,
                arbitrary_types_allowed_test_model: Type[InternalBaseModel]
        ):
            """
            Test arbitrary_types_allowed=True configuration.

            Args:
                arbitrary_types_allowed_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            from datetime import date

            custom_obj = {"key": "value"}
            test_date = date(2025, 1, 1)

            instance = arbitrary_types_allowed_test_model(
                custom_object=custom_obj,
                date_field=test_date
            )

            assert instance.custom_object == custom_obj
            assert instance.date_field == test_date

            logger.info("Arbitrary types allowed test passed - custom types accepted")

        def test_validate_by_alias_config(
                self,
                validate_by_alias_test_model: Type[InternalBaseModel]
        ):
            """
            Test validate_by_alias=True configuration.

            Args:
                validate_by_alias_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Should work with alias
            instance = validate_by_alias_test_model(userName="Alice")
            assert instance.user_name == "Alice"

            logger.info("Validate by alias test passed - validation by alias works")

        def test_validate_by_name_config(
                self,
                validate_by_name_test_model: Type[InternalBaseModel]
        ):
            """
            Test validate_by_name=False configuration.

            Args:
                validate_by_name_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Should NOT work with field name when alias exists
            with pytest.raises(ValidationError):
                validate_by_name_test_model(user_name="Bob")

            # Should work with alias
            instance = validate_by_name_test_model(userName="Bob")
            assert instance.user_name == "Bob"

            logger.info("Validate by name=False test passed - field name validation disabled")

        def test_loc_by_alias_config(
                self,
                loc_by_alias_test_model: Type[InternalBaseModel]
        ):
            """
            Test loc_by_alias=True configuration.

            Args:
                loc_by_alias_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test error location uses alias
            with pytest.raises(ValidationError) as exc_info:
                loc_by_alias_test_model(userName="ab")  # too short

            errors = exc_info.value.errors()
            # Error location should use alias name
            assert any("userName" in str(error.get('loc', [])) for error in errors)

            logger.info("Loc by alias test passed - error locations use aliases")

        def test_ser_json_bytes_config(
                self,
                ser_json_bytes_test_model: Type[InternalBaseModel]
        ):
            """
            Test ser_json_bytes='base64' configuration.

            Args:
                ser_json_bytes_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            test_bytes = b"hello world"
            instance = ser_json_bytes_test_model(data=test_bytes)

            # Test JSON serialization uses base64
            json_str = instance.model_dump_json()
            import base64
            expected_b64 = base64.b64encode(test_bytes).decode()
            assert expected_b64 in json_str

            logger.info("Ser JSON bytes test passed - bytes serialized as base64")

        def test_val_json_bytes_config(
                self,
                val_json_bytes_test_model: Type[InternalBaseModel]
        ):
            """
            Test val_json_bytes='base64' configuration.

            Args:
                val_json_bytes_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            import base64
            test_bytes = b"hello world"
            b64_str = base64.b64encode(test_bytes).decode()

            # Test validation from base64 string
            instance = val_json_bytes_test_model(data=b64_str)
            assert instance.data == test_bytes

            logger.info("Val JSON bytes test passed - base64 string validated to bytes")

        def test_regex_engine_config(
                self,
                regex_engine_test_model: Type[InternalBaseModel]
        ):
            """
            Test regex_engine='rust-regex' configuration.

            Args:
                regex_engine_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Valid pattern should pass
            instance = regex_engine_test_model(pattern_field="abc123")
            assert instance.pattern_field == "abc123"

            # Invalid pattern should fail
            with pytest.raises(ValidationError):
                regex_engine_test_model(pattern_field="abc-123")  # contains hyphen

            logger.info("Regex engine test passed - rust regex engine working")

        def test_defer_build_config(
                self,
                defer_build_test_model: Type[InternalBaseModel]
        ):
            """
            Test defer_build=True configuration.

            Args:
                defer_build_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test that model can be created (deferred building doesn't affect functionality)
            instance = defer_build_test_model(name="test")
            assert instance.name == "test"

            logger.info("Defer build test passed - deferred building working")

        def test_cache_strings_config(
                self,
                cache_strings_test_model: Type[InternalBaseModel]
        ):
            """
            Test cache_strings='keys' configuration.

            Args:
                cache_strings_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test that model works with string caching
            instance = cache_strings_test_model(field_1="value1", field_2="value2")
            assert instance.field_1 == "value1"
            assert instance.field_2 == "value2"

            logger.info("Cache strings test passed - string caching working")

        def test_hide_input_in_errors_config(
                self,
                hide_input_in_errors_test_model: Type[InternalBaseModel]
        ):
            """
            Test hide_input_in_errors=False configuration.

            Args:
                hide_input_in_errors_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test that error shows input value (hide_input_in_errors=False)
            with pytest.raises(ValidationError) as exc_info:
                hide_input_in_errors_test_model(number=-5)

            error_str = str(exc_info.value)
            # Should show the input value since hide_input_in_errors=False
            assert "-5" in error_str

            logger.info("Hide input in errors=False test passed - input shown in errors")

        def test_validation_error_cause_config(
                self,
                validation_error_cause_test_model: Type[InternalBaseModel]
        ):
            """
            Test validation_error_cause=True configuration.

            Args:
                validation_error_cause_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test that validation errors show cause
            with pytest.raises(ValidationError) as exc_info:
                validation_error_cause_test_model(value="abc")  # too short

            # Should have detailed error information
            assert len(exc_info.value.errors()) > 0

            logger.info("Validation error cause test passed - error causes displayed")

        def test_use_attribute_docstrings_config(
                self,
                use_attribute_docstrings_test_model: Type[InternalBaseModel]
        ):
            """
            Test use_attribute_docstrings=True configuration.

            Args:
                use_attribute_docstrings_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            # Test that model can be created
            instance = use_attribute_docstrings_test_model(documented_field="test")
            assert instance.documented_field == "test"

            # Test that field info includes docstring description
            field_info = use_attribute_docstrings_test_model.model_fields['documented_field']
            assert field_info.description is not None

            logger.info("Use attribute docstrings test passed - docstrings used as descriptions")

    class TestInternalBaseModelFields:
        """
        Test the built-in fields of InternalBaseModel.

        This class tests the version and created_at fields that are
        inherited by all models extending InternalBaseModel.
        """

        def test_created_at_field(self):
            """
            Test created_at field functionality.
            """
            from datetime import datetime, timezone, timedelta

            # Test default creation time
            before_creation = datetime.now(tz=timezone.utc)
            instance = InternalBaseModel()
            after_creation = datetime.now(tz=timezone.utc)

            # Verify created_at is set and within expected range
            assert before_creation <= instance.created_at <= after_creation
            assert instance.created_at.tzinfo == timezone.utc

            # Test explicit creation time
            explicit_time = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
            instance2 = InternalBaseModel(created_at=explicit_time)
            assert instance2.created_at == explicit_time

            logger.info("Created_at field test passed")

        def test_version_field(self):
            """
            Test version field functionality.
            """
            # Test default version
            instance = InternalBaseModel()
            assert instance.version == "1.0.0"

            # Test explicit version
            instance2 = InternalBaseModel(version="2.0.0")
            assert instance2.version == "2.0.0"

            # Test empty version defaults to Meta.version
            instance3 = InternalBaseModel(version="")
            assert instance3.version == "1.0.0"

            logger.info("Version field test passed")

    class TestInternalBaseModelSerialization:
        """
        Test serialization and deserialization functionality.

        This class tests JSON serialization, model_dump, and related features.
        """

        def test_json_serialization(self):
            """
            Test JSON serialization with various configurations.
            """
            from datetime import datetime, timezone

            instance = InternalBaseModel(
                version="1.2.3",
                created_at=datetime(2025, 1, 15, 10, 30, 0, tzinfo=timezone.utc)
            )

            # Test model_dump
            dumped = instance.model_dump()
            assert dumped["version"] == "1.2.3"
            assert isinstance(dumped["created_at"], datetime)

            # Test JSON serialization
            json_str = instance.model_dump_json()
            assert '"version":"1.2.3"' in json_str
            assert "2025-01-15" in json_str

            # Test JSON deserialization
            loaded = InternalBaseModel.model_validate_json(json_str)
            assert loaded.version == instance.version
            assert loaded.created_at == instance.created_at

            logger.info("JSON serialization test passed")

        def test_by_alias_serialization(
                self,
                validate_by_alias_test_model: Type[InternalBaseModel]
        ):
            """
            Test serialization with by_alias parameter.

            Args:
                validate_by_alias_test_model (Type[InternalBaseModel]): Test model class from fixture
            """
            instance = validate_by_alias_test_model(userName="John")

            # Default serialization uses field names
            dumped = instance.model_dump()
            assert "user_name" in dumped

            # By alias serialization uses aliases
            dumped_alias = instance.model_dump(by_alias=True)
            assert "userName" in dumped_alias
            assert "user_name" not in dumped_alias

            logger.info("By alias serialization test passed")

    class TestInternalBaseModelInheritance:
        """
        Test inheritance behavior of InternalBaseModel.

        This class ensures that all configurations are properly inherited
        by child classes.
        """

        def test_config_inheritance(self):
            """
            Test that model_config is properly inherited.
            """

            class ChildModel(InternalBaseModel):
                """Child model for testing inheritance."""
                name: str

            # Verify config is inherited
            assert ChildModel.model_config.get("frozen") == False
            assert ChildModel.model_config.get("strict") == True
            assert ChildModel.model_config.get("extra") == "forbid"

            # Test that config works in child
            with pytest.raises(ValidationError):
                ChildModel(name="test", extra_field="not_allowed")

            logger.info("Config inheritance test passed")

        def test_field_inheritance(self):
            """
            Test that fields are properly inherited.
            """

            class ChildModel(InternalBaseModel):
                """Child model with additional fields."""
                name: str
                age: int

            instance = ChildModel(name="Alice", age=30)

            # Verify inherited fields exist
            assert hasattr(instance, "version")
            assert hasattr(instance, "created_at")
            assert instance.version == "1.0.0"

            # Verify new fields work
            assert instance.name == "Alice"
            assert instance.age == 30

            logger.info("Field inheritance test passed")

        def test_meta_class_inheritance(self):
            """
            Test Meta class inheritance and override.
            """

            class ChildWithMeta(InternalBaseModel):
                """Child model with custom Meta."""
                name: str

                class Meta:
                    """Custom meta class."""
                    version: str = "3.0.0"

            class ChildWithoutMeta(InternalBaseModel):
                """Child model without Meta."""
                name: str

            # Test with custom Meta
            instance1 = ChildWithMeta(name="test1")
            assert instance1.version == "3.0.0"

            # Test without Meta (should use parent's default)
            instance2 = ChildWithoutMeta(name="test2")
            assert instance2.version == "1.0.0"

            logger.info("Meta class inheritance test passed")