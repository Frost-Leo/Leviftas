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

test_serialization.py

Tests for InternalBaseModel serialization configuration.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import json
import logging
from datetime import timedelta
from typing import Optional

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestTimedeltaSerialization:
    """Tests for ser_json_timedelta='iso8601' configuration."""

    def test_timedelta_iso8601_format(self) -> None:
        """Timedelta should serialize to ISO8601 format."""
        logger.info("Testing timedelta ISO8601 serialization")

        class DurationModel(InternalBaseModel):
            duration: timedelta

        model = DurationModel(duration=timedelta(hours=1, minutes=30))
        data = model.model_dump(mode="json")
        logger.debug("Serialized duration: %s", data["duration"])

        # ISO8601 duration format: PT1H30M
        assert data["duration"] == "PT1H30M"
        logger.info("Timedelta correctly serialized to ISO8601")

    def test_timedelta_with_days(self) -> None:
        """Timedelta with days should serialize correctly."""
        logger.info("Testing timedelta with days")

        class DurationModel(InternalBaseModel):
            duration: timedelta

        model = DurationModel(duration=timedelta(days=2, hours=3, minutes=15))
        data = model.model_dump(mode="json")
        logger.debug("Serialized duration: %s", data["duration"])

        # P2DT3H15M format
        assert "P2D" in data["duration"] or "PT51H15M" in data["duration"]
        logger.info("Timedelta with days serialized correctly")

    def test_timedelta_seconds_only(self) -> None:
        """Timedelta with only seconds should serialize correctly."""
        logger.info("Testing timedelta with seconds only")

        class DurationModel(InternalBaseModel):
            duration: timedelta

        model = DurationModel(duration=timedelta(seconds=90))
        data = model.model_dump(mode="json")
        logger.debug("Serialized duration: %s", data["duration"])

        assert "PT" in data["duration"]
        logger.info("Timedelta with seconds serialized correctly")


class TestModelDump:
    """Tests for model_dump serialization."""

    def test_model_dump_basic(self) -> None:
        """Basic model_dump should work correctly."""
        logger.info("Testing basic model_dump")

        class SimpleModel(InternalBaseModel):
            name: str
            value: int

        model = SimpleModel(name="test", value=42)
        data = model.model_dump()
        logger.debug("Dumped data: %s", data)

        assert data == {"name": "test", "value": 42}
        logger.info("Basic model_dump verified")

    def test_model_dump_with_none(self) -> None:
        """model_dump should handle None values correctly."""
        logger.info("Testing model_dump with None values")

        class OptionalModel(InternalBaseModel):
            name: str
            optional_value: Optional[int] = None

        model = OptionalModel(name="test")
        data = model.model_dump()
        logger.debug("Dumped data: %s", data)

        assert data["optional_value"] is None
        logger.info("None values handled correctly")

    def test_model_dump_exclude(self) -> None:
        """model_dump should support exclude parameter."""
        logger.info("Testing model_dump with exclude")

        class MultiFieldModel(InternalBaseModel):
            field_a: str
            field_b: str
            field_c: str

        model = MultiFieldModel(field_a="a", field_b="b", field_c="c")
        data = model.model_dump(exclude={"field_b"})
        logger.debug("Dumped data (excluding field_b): %s", data)

        assert "field_a" in data
        assert "field_b" not in data
        assert "field_c" in data
        logger.info("Exclude parameter works correctly")


class TestJsonSerialization:
    """Tests for JSON serialization."""

    def test_model_dump_json_basic(self) -> None:
        """Basic JSON serialization should work correctly."""
        logger.info("Testing basic JSON serialization")

        class SimpleModel(InternalBaseModel):
            name: str
            value: int

        model = SimpleModel(name="json_test", value=100)
        json_str = model.model_dump_json()
        logger.debug("JSON output: %s", json_str)

        parsed = json.loads(json_str)
        assert parsed == {"name": "json_test", "value": 100}
        logger.info("Basic JSON serialization verified")

    def test_json_roundtrip(self) -> None:
        """JSON serialization/deserialization roundtrip should preserve data."""
        logger.info("Testing JSON roundtrip")

        class RoundtripModel(InternalBaseModel):
            name: str
            count: int

        original = RoundtripModel(name="roundtrip", count=999)
        json_str = original.model_dump_json()
        logger.debug("Original JSON: %s", json_str)

        restored = RoundtripModel.model_validate_json(json_str)
        logger.debug("Restored model: name='%s', count=%d", restored.name, restored.count)

        assert restored.name == original.name
        assert restored.count == original.count
        logger.info("JSON roundtrip successful")


class TestNestedSerialization:
    """Tests for nested model serialization."""

    def test_nested_model_serialization(self) -> None:
        """Nested models should serialize correctly."""
        logger.info("Testing nested model serialization")

        class Inner(InternalBaseModel):
            inner_value: int

        class Outer(InternalBaseModel):
            outer_name: str
            inner: Inner

        model = Outer(outer_name="outer", inner=Inner(inner_value=42))
        data = model.model_dump()
        logger.debug("Serialized nested data: %s", data)

        assert data["outer_name"] == "outer"
        assert data["inner"]["inner_value"] == 42
        logger.info("Nested model serialization verified")

    def test_list_of_nested_models(self) -> None:
        """List of nested models should serialize correctly."""
        logger.info("Testing list of nested models serialization")

        class Item(InternalBaseModel):
            name: str
            price: int

        class Order(InternalBaseModel):
            order_id: str
            items: list[Item]

        model = Order(
            order_id="ORD-001",
            items=[
                Item(name="Widget", price=100),
                Item(name="Gadget", price=200),
            ],
        )

        data = model.model_dump()
        logger.debug("Serialized order: %s", data)

        assert len(data["items"]) == 2
        assert data["items"][0]["name"] == "Widget"
        assert data["items"][1]["price"] == 200
        logger.info("List of nested models serialized correctly")

