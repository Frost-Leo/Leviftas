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

fixtures.py

Test fixtures for InternalBaseModel tests.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)


class SampleModel(InternalBaseModel):
    """Sample model for testing basic functionality."""

    name: str
    value: int


class CustomMetaModel(InternalBaseModel):
    """Sample model with custom Meta configuration."""

    class Meta:
        version: str = "2.0.0"
        category: str = "config"
        tags: set[str] = {"test", "sample"}
        labels: dict[str, str] = {"env": "test"}

    title: str


@pytest.fixture
def sample_model_class() -> type[SampleModel]:
    """Return SampleModel class for testing."""
    logger.debug("Providing SampleModel class fixture")
    return SampleModel


@pytest.fixture
def custom_meta_model_class() -> type[CustomMetaModel]:
    """Return CustomMetaModel class for testing."""
    logger.debug("Providing CustomMetaModel class fixture")
    return CustomMetaModel


@pytest.fixture
def sample_model_instance() -> SampleModel:
    """Return a SampleModel instance for testing."""
    instance = SampleModel(name="test", value=42)
    logger.debug("Created SampleModel instance: name='%s', value=%d", instance.name, instance.value)
    return instance


@pytest.fixture
def custom_meta_model_instance() -> CustomMetaModel:
    """Return a CustomMetaModel instance for testing."""
    instance = CustomMetaModel(title="Test Title")
    logger.debug("Created CustomMetaModel instance: title='%s'", instance.title)
    return instance
