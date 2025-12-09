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

test_alias.py

Tests for InternalBaseModel alias handling.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestAliasGenerator:
    """Tests for alias_generator=to_snake configuration."""

    def test_snake_case_alias_accepted(self) -> None:
        """Fields should accept snake_case aliases from to_snake generator."""
        logger.info("Testing snake_case alias acceptance")

        class AliasModel(InternalBaseModel):
            userName: str  # noqa: N815

        # Should work with snake_case input (generated alias)
        model = AliasModel(user_name="test_user")
        logger.debug("Input: user_name='test_user', Field value: '%s'", model.userName)

        assert model.userName == "test_user"
        logger.info("Snake_case alias correctly accepted")

    def test_original_name_still_works(self) -> None:
        """Original field names should still be accepted (validate_by_name=True)."""
        logger.info("Testing original field name acceptance")

        class AliasModel(InternalBaseModel):
            userName: str  # noqa: N815

        model = AliasModel(userName="original_name")
        logger.debug("Input: userName='original_name', Field value: '%s'", model.userName)

        assert model.userName == "original_name"
        logger.info("Original field name correctly accepted")

    def test_camel_to_snake_conversion(self) -> None:
        """CamelCase field names should generate snake_case aliases."""
        logger.info("Testing CamelCase to snake_case conversion")

        class CamelModel(InternalBaseModel):
            firstName: str  # noqa: N815
            lastName: str  # noqa: N815
            emailAddress: str  # noqa: N815

        model = CamelModel(
            first_name="John",
            last_name="Doe",
            email_address="john@example.com",
        )

        logger.debug("firstName: '%s'", model.firstName)
        logger.debug("lastName: '%s'", model.lastName)
        logger.debug("emailAddress: '%s'", model.emailAddress)

        assert model.firstName == "John"
        assert model.lastName == "Doe"
        assert model.emailAddress == "john@example.com"
        logger.info("CamelCase to snake_case conversion verified")


class TestSerializationByAlias:
    """Tests for serialize_by_alias=False configuration."""

    def test_serialization_uses_original_names(self) -> None:
        """Serialization should use original field names, not aliases."""
        logger.info("Testing serialization uses original field names")

        class SerModel(InternalBaseModel):
            userName: str  # noqa: N815
            itemCount: int  # noqa: N815

        model = SerModel(user_name="test", item_count=42)
        data = model.model_dump()
        logger.debug("Serialized data: %s", data)

        # serialize_by_alias=False means original names are used
        assert "userName" in data
        assert "itemCount" in data
        assert "user_name" not in data
        assert "item_count" not in data
        logger.info("Serialization correctly uses original field names")

    def test_json_serialization_uses_original_names(self) -> None:
        """JSON serialization should use original field names."""
        logger.info("Testing JSON serialization uses original field names")

        class SerModel(InternalBaseModel):
            userName: str  # noqa: N815

        model = SerModel(user_name="json_test")
        json_str = model.model_dump_json()
        logger.debug("JSON output: %s", json_str)

        assert "userName" in json_str
        assert "user_name" not in json_str
        logger.info("JSON serialization correctly uses original field names")


class TestValidateByNameAndAlias:
    """Tests for validate_by_name and validate_by_alias configuration."""

    def test_both_name_and_alias_work(self) -> None:
        """Both original name and alias should be accepted for validation."""
        logger.info("Testing both name and alias validation")

        class FlexModel(InternalBaseModel):
            userId: str  # noqa: N815

        # Using alias
        model1 = FlexModel(user_id="by_alias")
        logger.debug("Created with alias: %s", model1.userId)

        # Using original name
        model2 = FlexModel(userId="by_name")
        logger.debug("Created with name: %s", model2.userId)

        assert model1.userId == "by_alias"
        assert model2.userId == "by_name"
        logger.info("Both name and alias validation confirmed")


class TestAliasInNestedModels:
    """Tests for alias handling in nested models."""

    def test_nested_model_aliases(self) -> None:
        """Alias handling should work in nested models."""
        logger.info("Testing alias handling in nested models")

        class InnerModel(InternalBaseModel):
            innerValue: int  # noqa: N815

        class OuterModel(InternalBaseModel):
            outerName: str  # noqa: N815
            nested: InnerModel

        model = OuterModel(
            outer_name="outer",
            nested=InnerModel(inner_value=99),
        )

        logger.debug("outerName: '%s'", model.outerName)
        logger.debug("nested.innerValue: %d", model.nested.innerValue)

        assert model.outerName == "outer"
        assert model.nested.innerValue == 99
        logger.info("Nested model alias handling verified")

    def test_nested_serialization(self) -> None:
        """Nested model serialization should use original names."""
        logger.info("Testing nested model serialization")

        class InnerModel(InternalBaseModel):
            innerValue: int  # noqa: N815

        class OuterModel(InternalBaseModel):
            outerName: str  # noqa: N815
            nested: InnerModel

        model = OuterModel(
            outer_name="test",
            nested=InnerModel(inner_value=42),
        )

        data = model.model_dump()
        logger.debug("Serialized data: %s", data)

        assert "outerName" in data
        assert "innerValue" in data["nested"]
        logger.info("Nested serialization uses original names")

