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

test_enum_handling.py

Tests for InternalBaseModel enum handling (use_enum_values=True).

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging
from enum import Enum, IntEnum

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class Status(Enum):
    """String enum for testing."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class Priority(IntEnum):
    """Integer enum for testing."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


class TestEnumValues:
    """Tests for use_enum_values=True configuration."""

    def test_string_enum_stored_as_value(self) -> None:
        """String enum fields should store the value, not the enum member."""
        logger.info("Testing string enum value storage")

        class EnumModel(InternalBaseModel):
            status: Status

        model = EnumModel(status=Status.ACTIVE)
        logger.debug("Input: Status.ACTIVE, Stored: %s (type: %s)", model.status, type(model.status).__name__)

        assert model.status == "active"
        assert isinstance(model.status, str)
        logger.info("String enum correctly stored as value")

    def test_int_enum_stored_as_value(self) -> None:
        """Integer enum fields should store the value, not the enum member."""
        logger.info("Testing integer enum value storage")

        class EnumModel(InternalBaseModel):
            priority: Priority

        model = EnumModel(priority=Priority.HIGH)
        logger.debug("Input: Priority.HIGH, Stored: %s (type: %s)", model.priority, type(model.priority).__name__)

        assert model.priority == 3
        assert isinstance(model.priority, int)
        logger.info("Integer enum correctly stored as value")

    def test_enum_serialization(self) -> None:
        """Enum values should serialize correctly."""
        logger.info("Testing enum serialization")

        class EnumModel(InternalBaseModel):
            status: Status
            priority: Priority

        model = EnumModel(status=Status.PENDING, priority=Priority.MEDIUM)
        data = model.model_dump()
        logger.debug("Serialized data: %s", data)

        assert data["status"] == "pending"
        assert data["priority"] == 2
        logger.info("Enum values serialized correctly")

    def test_enum_json_serialization(self) -> None:
        """Enum values should JSON serialize correctly."""
        logger.info("Testing enum JSON serialization")

        class EnumModel(InternalBaseModel):
            status: Status

        model = EnumModel(status=Status.INACTIVE)
        json_data = model.model_dump_json()
        logger.debug("JSON output: %s", json_data)

        assert '"inactive"' in json_data
        logger.info("Enum JSON serialization verified")


class TestEnumValidation:
    """Tests for enum validation behavior."""

    def test_enum_member_accepted(self) -> None:
        """Enum member should be accepted as input."""
        logger.info("Testing enum member acceptance")

        class EnumModel(InternalBaseModel):
            status: Status

        model = EnumModel(status=Status.ACTIVE)
        logger.debug("Created model with enum member: %s", model.status)

        assert model.status == "active"
        logger.info("Enum member correctly accepted")

    def test_multiple_enum_fields(self) -> None:
        """Model with multiple enum fields should work correctly."""
        logger.info("Testing multiple enum fields")

        class MultiEnumModel(InternalBaseModel):
            status: Status
            priority: Priority

        model = MultiEnumModel(status=Status.ACTIVE, priority=Priority.HIGH)
        logger.debug("status: %s, priority: %s", model.status, model.priority)

        assert model.status == "active"
        assert model.priority == 3
        logger.info("Multiple enum fields handled correctly")

    def test_enum_assignment_after_creation(self) -> None:
        """Enum assignment after creation should store value."""
        logger.info("Testing enum assignment after creation")

        class EnumModel(InternalBaseModel):
            status: Status

        model = EnumModel(status=Status.ACTIVE)
        logger.debug("Initial status: %s", model.status)

        model.status = Status.INACTIVE  # type: ignore[assignment]
        logger.debug("Updated status: %s", model.status)

        assert model.status == "inactive"
        logger.info("Enum assignment correctly stored value")

