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

test_from_attributes.py

Tests for InternalBaseModel from_attributes configuration.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging
from dataclasses import dataclass
from typing import NamedTuple

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestFromAttributes:
    """Tests for from_attributes=True configuration."""

    def test_create_from_simple_object(self) -> None:
        """Model should be creatable from object with matching attributes."""
        logger.info("Testing model creation from simple object")

        class DataHolder:
            def __init__(self) -> None:
                self.name = "test_name"
                self.value = 42

        class AttrModel(InternalBaseModel):
            name: str
            value: int

        obj = DataHolder()
        logger.debug("Source object: name='%s', value=%d", obj.name, obj.value)

        model = AttrModel.model_validate(obj)
        logger.debug("Created model: name='%s', value=%d", model.name, model.value)

        assert model.name == "test_name"
        assert model.value == 42
        logger.info("Model correctly created from object attributes")

    def test_create_from_dataclass(self) -> None:
        """Model should be creatable from dataclass instance."""
        logger.info("Testing model creation from dataclass")

        @dataclass
        class UserData:
            username: str
            age: int

        class UserModel(InternalBaseModel):
            username: str
            age: int

        data = UserData(username="john_doe", age=30)
        logger.debug("Source dataclass: username='%s', age=%d", data.username, data.age)

        model = UserModel.model_validate(data)
        logger.debug("Created model: username='%s', age=%d", model.username, model.age)

        assert model.username == "john_doe"
        assert model.age == 30
        logger.info("Model correctly created from dataclass")

    def test_create_from_namedtuple(self) -> None:
        """Model should be creatable from NamedTuple instance."""
        logger.info("Testing model creation from NamedTuple")

        class Point(NamedTuple):
            x: int
            y: int

        class PointModel(InternalBaseModel):
            x: int
            y: int

        point = Point(x=10, y=20)
        logger.debug("Source NamedTuple: x=%d, y=%d", point.x, point.y)

        model = PointModel.model_validate(point)
        logger.debug("Created model: x=%d, y=%d", model.x, model.y)

        assert model.x == 10
        assert model.y == 20
        logger.info("Model correctly created from NamedTuple")

    def test_create_from_another_pydantic_model(self) -> None:
        """Model should be creatable from another Pydantic model instance."""
        logger.info("Testing model creation from another Pydantic model")

        class SourceModel(InternalBaseModel):
            name: str
            count: int

        class TargetModel(InternalBaseModel):
            name: str
            count: int

        source = SourceModel(name="source", count=100)
        logger.debug("Source model: name='%s', count=%d", source.name, source.count)

        target = TargetModel.model_validate(source)
        logger.debug("Target model: name='%s', count=%d", target.name, target.count)

        assert target.name == "source"
        assert target.count == 100
        logger.info("Model correctly created from another Pydantic model")


class TestFromAttributesWithProperties:
    """Tests for from_attributes with computed properties."""

    def test_create_from_object_with_property(self) -> None:
        """Model should read from object properties."""
        logger.info("Testing model creation from object with property")

        class ComputedObject:
            def __init__(self) -> None:
                self._internal_value = 50

            @property
            def value(self) -> int:
                return self._internal_value * 2

        class ValueModel(InternalBaseModel):
            value: int

        obj = ComputedObject()
        logger.debug("Source object property value: %d", obj.value)

        model = ValueModel.model_validate(obj)
        logger.debug("Created model value: %d", model.value)

        assert model.value == 100
        logger.info("Model correctly read from object property")


class TestFromAttributesValidation:
    """Tests for validation when creating from attributes."""

    def test_validation_applied_to_attributes(self) -> None:
        """Validation should be applied when creating from attributes."""
        logger.info("Testing validation applied to object attributes")

        class DataHolder:
            def __init__(self) -> None:
                self.name = "  spaced name  "

        class NameModel(InternalBaseModel):
            name: str

        obj = DataHolder()
        logger.debug("Source object name: '%s'", obj.name)

        model = NameModel.model_validate(obj)
        logger.debug("Created model name: '%s'", model.name)

        # str_strip_whitespace should apply
        assert model.name == "spaced name"
        logger.info("Validation (whitespace strip) correctly applied")

