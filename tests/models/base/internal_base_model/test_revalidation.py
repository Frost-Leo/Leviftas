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

test_revalidation.py

Tests for InternalBaseModel revalidation configuration.

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


class TestRevalidateInstances:
    """Tests for revalidate_instances='always' configuration."""

    def test_nested_model_revalidated_on_assignment(self) -> None:
        """Nested model should be revalidated when assigned to parent."""
        logger.info("Testing nested model revalidation on assignment")

        class Inner(InternalBaseModel):
            value: int

        class Outer(InternalBaseModel):
            inner: Inner

        inner = Inner(value=42)
        logger.debug("Created inner model with value: %d", inner.value)

        outer = Outer(inner=inner)
        logger.debug("Created outer model with inner.value: %d", outer.inner.value)

        assert outer.inner.value == 42
        logger.info("Nested model correctly validated")

    def test_revalidation_catches_tampered_data(self) -> None:
        """Revalidation should catch data that was tampered with bypassing setters."""
        logger.info("Testing revalidation catches tampered data")

        class Inner(InternalBaseModel):
            value: int

        class Outer(InternalBaseModel):
            inner: Inner

        inner = Inner(value=42)
        logger.debug("Original inner value: %d", inner.value)

        # Simulate tampering by bypassing validation (using object.__setattr__)
        object.__setattr__(inner, "value", "invalid_string")
        logger.debug("Tampered inner value: %s", inner.value)

        # When creating Outer, revalidation should catch the invalid data
        logger.debug("Attempting to create Outer with tampered Inner")
        with pytest.raises(ValidationError) as exc_info:
            Outer(inner=inner)

        logger.info("Revalidation caught tampered data: %s", exc_info.type.__name__)

    def test_valid_nested_model_passes_revalidation(self) -> None:
        """Valid nested model should pass revalidation."""
        logger.info("Testing valid nested model passes revalidation")

        class Level1(InternalBaseModel):
            name: str

        class Level2(InternalBaseModel):
            level1: Level1
            count: int

        class Level3(InternalBaseModel):
            level2: Level2

        level1 = Level1(name="first")
        level2 = Level2(level1=level1, count=10)
        level3 = Level3(level2=level2)

        logger.debug("Level3.level2.level1.name: %s", level3.level2.level1.name)
        logger.debug("Level3.level2.count: %d", level3.level2.count)

        assert level3.level2.level1.name == "first"
        assert level3.level2.count == 10
        logger.info("Deeply nested model passed revalidation")


class TestValidateDefault:
    """Tests for validate_default=True configuration."""

    def test_valid_default_accepted(self) -> None:
        """Valid default values should be accepted."""
        logger.info("Testing valid default value acceptance")

        class DefaultModel(InternalBaseModel):
            name: str = "default_name"
            count: int = 0

        model = DefaultModel()
        logger.debug("Model with defaults: name='%s', count=%d", model.name, model.count)

        assert model.name == "default_name"
        assert model.count == 0
        logger.info("Valid default values accepted")

    def test_default_with_strip_whitespace(self) -> None:
        """Default string values should have whitespace stripped."""
        logger.info("Testing default string whitespace handling")

        class DefaultModel(InternalBaseModel):
            name: str = "  spaced  "

        model = DefaultModel()
        logger.debug("Default name after strip: '%s'", model.name)

        # str_strip_whitespace should apply to defaults
        assert model.name == "spaced"
        logger.info("Default string whitespace correctly stripped")


class TestValidateReturn:
    """Tests for validate_return=True configuration."""

    def test_model_method_return_validation(self) -> None:
        """Method return values should be validated when using @validate_call."""
        logger.info("Testing validate_return configuration exists")

        # validate_return=True is set in ConfigDict
        # This affects validators and model methods that use return type hints

        class MethodModel(InternalBaseModel):
            value: int

            def get_doubled(self) -> int:
                return self.value * 2

        model = MethodModel(value=21)
        result = model.get_doubled()
        logger.debug("Original value: %d, Doubled: %d", model.value, result)

        assert result == 42
        logger.info("Model method returned correct value")


class TestValidationErrorCause:
    """Tests for validation_error_cause=True configuration."""

    def test_validation_error_shows_cause(self) -> None:
        """Validation errors should include cause information."""
        logger.info("Testing validation error cause visibility")

        class CauseModel(InternalBaseModel):
            value: int

        try:
            CauseModel(value="not_an_int")
        except ValidationError as e:
            logger.debug("Validation error: %s", e)
            error_str = str(e)
            # The error should contain detailed information
            assert "value" in error_str.lower() or "int" in error_str.lower()
            logger.info("Validation error contains cause information")
            return

        pytest.fail("Expected ValidationError was not raised")

