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

test_config.py

Tests for InternalBaseModel ConfigDict settings.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging

import pytest
from pydantic import ValidationError

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestStrictMode:
    """Tests for strict mode configuration."""

    def test_strict_type_validation(self) -> None:
        """Strict mode should reject wrong types without coercion."""
        logger.info("Testing strict mode type validation")

        class StrictModel(InternalBaseModel):
            value: int

        logger.debug("Attempting to create model with string value '123'")
        with pytest.raises(ValidationError) as exc_info:
            StrictModel(value="123")  # String should not coerce to int

        logger.info("ValidationError raised as expected: %s", exc_info.type.__name__)

    def test_strict_accepts_correct_types(self) -> None:
        """Strict mode should accept correct types."""
        logger.info("Testing strict mode accepts correct types")

        class StrictModel(InternalBaseModel):
            value: int

        model = StrictModel(value=123)
        logger.debug("Created model with value: %d", model.value)
        assert model.value == 123
        logger.info("Strict mode correctly accepted integer value")


class TestExtraForbid:
    """Tests for extra='forbid' configuration."""

    def test_extra_fields_rejected(self) -> None:
        """Extra fields should be rejected."""
        logger.info("Testing extra fields rejection")

        class SimpleModel(InternalBaseModel):
            name: str

        logger.debug("Attempting to create model with extra field 'extra_field'")
        with pytest.raises(ValidationError) as exc_info:
            SimpleModel(name="test", extra_field="not allowed")

        logger.info("Extra field correctly rejected: %s", exc_info.type.__name__)


class TestStringHandling:
    """Tests for string handling configuration."""

    def test_string_whitespace_stripped(self) -> None:
        """Leading and trailing whitespace should be stripped."""
        logger.info("Testing string whitespace stripping")

        class StringModel(InternalBaseModel):
            name: str

        input_value = "  hello world  "
        model = StringModel(name=input_value)
        logger.debug("Input: '%s' -> Output: '%s'", input_value, model.name)
        assert model.name == "hello world"
        logger.info("Whitespace correctly stripped from string")

    def test_string_max_length_enforced(self) -> None:
        """Strings exceeding max length should be rejected."""
        logger.info("Testing string max length enforcement (10000 chars)")

        class StringModel(InternalBaseModel):
            name: str

        long_string = "x" * 10001
        logger.debug("Attempting to create model with string of length %d", len(long_string))
        with pytest.raises(ValidationError) as exc_info:
            StringModel(name=long_string)

        logger.info("Long string correctly rejected: %s", exc_info.type.__name__)

    def test_string_at_max_length_accepted(self) -> None:
        """Strings at exactly max length should be accepted."""
        logger.info("Testing string at max length boundary")

        class StringModel(InternalBaseModel):
            name: str

        max_string = "x" * 10000
        model = StringModel(name=max_string)
        logger.debug("Created model with string of length %d", len(model.name))
        assert len(model.name) == 10000
        logger.info("String at max length correctly accepted")


class TestValidateAssignment:
    """Tests for validate_assignment configuration."""

    def test_assignment_validated(self) -> None:
        """Assignment should trigger validation."""
        logger.info("Testing assignment validation")

        class AssignModel(InternalBaseModel):
            value: int

        model = AssignModel(value=1)
        logger.debug("Created model with value: %d", model.value)

        logger.debug("Attempting to assign invalid string value")
        with pytest.raises(ValidationError) as exc_info:
            model.value = "not an int"  # type: ignore[assignment]

        logger.info("Invalid assignment correctly rejected: %s", exc_info.type.__name__)

    def test_valid_assignment_accepted(self) -> None:
        """Valid assignment should be accepted."""
        logger.info("Testing valid assignment")

        class AssignModel(InternalBaseModel):
            value: int

        model = AssignModel(value=1)
        model.value = 42
        logger.debug("Updated value from 1 to %d", model.value)
        assert model.value == 42
        logger.info("Valid assignment correctly accepted")


class TestInfNanForbidden:
    """Tests for allow_inf_nan=False configuration."""

    def test_infinity_rejected(self) -> None:
        """Infinity values should be rejected."""
        logger.info("Testing infinity rejection")

        class FloatModel(InternalBaseModel):
            value: float

        logger.debug("Attempting to create model with float('inf')")
        with pytest.raises(ValidationError) as exc_info:
            FloatModel(value=float("inf"))

        logger.info("Infinity correctly rejected: %s", exc_info.type.__name__)

    def test_negative_infinity_rejected(self) -> None:
        """Negative infinity values should be rejected."""
        logger.info("Testing negative infinity rejection")

        class FloatModel(InternalBaseModel):
            value: float

        logger.debug("Attempting to create model with float('-inf')")
        with pytest.raises(ValidationError) as exc_info:
            FloatModel(value=float("-inf"))

        logger.info("Negative infinity correctly rejected: %s", exc_info.type.__name__)

    def test_nan_rejected(self) -> None:
        """NaN values should be rejected."""
        logger.info("Testing NaN rejection")

        class FloatModel(InternalBaseModel):
            value: float

        logger.debug("Attempting to create model with float('nan')")
        with pytest.raises(ValidationError) as exc_info:
            FloatModel(value=float("nan"))

        logger.info("NaN correctly rejected: %s", exc_info.type.__name__)

    def test_valid_float_accepted(self) -> None:
        """Valid float values should be accepted."""
        logger.info("Testing valid float acceptance")

        class FloatModel(InternalBaseModel):
            value: float

        model = FloatModel(value=3.14159)
        logger.debug("Created model with value: %f", model.value)
        assert model.value == 3.14159
        logger.info("Valid float correctly accepted")


class TestFrozenFalse:
    """Tests for frozen=False configuration."""

    def test_model_is_mutable(self) -> None:
        """Model should be mutable (not frozen)."""
        logger.info("Testing model mutability")

        class MutableModel(InternalBaseModel):
            name: str
            value: int

        model = MutableModel(name="original", value=1)
        logger.debug("Created model: name='%s', value=%d", model.name, model.value)

        model.name = "modified"
        model.value = 99
        logger.debug("Modified model: name='%s', value=%d", model.name, model.value)

        assert model.name == "modified"
        assert model.value == 99
        logger.info("Model mutability confirmed")
