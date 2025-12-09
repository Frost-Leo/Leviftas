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

test_meta.py

Tests for InternalBaseModel Meta class.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/9 
- Modified : 2025/12/9
"""

import logging

import pytest

from leviftas.models.base import InternalBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestMetaDefaults:
    """Tests for default Meta values."""

    def test_default_version(self) -> None:
        """Default version should be 0.1.0."""
        logger.info("Testing default Meta version")
        version = InternalBaseModel.Meta.version
        logger.debug("Default version: %s", version)
        assert version == "0.1.0"
        logger.info("Default version verified: %s", version)

    def test_default_category(self) -> None:
        """Default category should be 'internal'."""
        logger.info("Testing default Meta category")
        category = InternalBaseModel.Meta.category
        logger.debug("Default category: %s", category)
        assert category == "internal"
        logger.info("Default category verified: %s", category)

    def test_default_tags(self) -> None:
        """Default tags should be empty set."""
        logger.info("Testing default Meta tags")
        tags = InternalBaseModel.Meta.tags
        logger.debug("Default tags: %s", tags)
        assert tags == set()
        logger.info("Default tags verified: empty set")

    def test_default_labels(self) -> None:
        """Default labels should be empty dict."""
        logger.info("Testing default Meta labels")
        labels = InternalBaseModel.Meta.labels
        logger.debug("Default labels: %s", labels)
        assert labels == {}
        logger.info("Default labels verified: empty dict")


class TestMetaInheritance:
    """Tests for Meta inheritance behavior."""

    def test_subclass_inherits_meta(self) -> None:
        """Subclass without Meta should inherit parent Meta."""
        logger.info("Testing Meta inheritance for subclass without custom Meta")

        class ChildModel(InternalBaseModel):
            name: str

        logger.debug("ChildModel.Meta.version: %s", ChildModel.Meta.version)
        logger.debug("ChildModel.Meta.category: %s", ChildModel.Meta.category)

        assert ChildModel.Meta.version == "0.1.0"
        assert ChildModel.Meta.category == "internal"
        logger.info("Subclass correctly inherited parent Meta")

    def test_subclass_can_override_meta(self) -> None:
        """Subclass can override Meta attributes."""
        logger.info("Testing Meta override in subclass")

        class CustomModel(InternalBaseModel):
            class Meta:
                version: str = "2.0.0"
                category: str = "config"
                tags: set[str] = {"custom", "test"}
                labels: dict[str, str] = {"env": "prod"}

            name: str

        logger.debug("CustomModel.Meta.version: %s", CustomModel.Meta.version)
        logger.debug("CustomModel.Meta.category: %s", CustomModel.Meta.category)
        logger.debug("CustomModel.Meta.tags: %s", CustomModel.Meta.tags)
        logger.debug("CustomModel.Meta.labels: %s", CustomModel.Meta.labels)

        assert CustomModel.Meta.version == "2.0.0"
        assert CustomModel.Meta.category == "config"
        assert CustomModel.Meta.tags == {"custom", "test"}
        assert CustomModel.Meta.labels == {"env": "prod"}
        logger.info("Subclass Meta override verified")

    def test_meta_access_from_instance(self) -> None:
        """Meta should be accessible from model instance."""
        logger.info("Testing Meta access from instance")

        class SampleModel(InternalBaseModel):
            class Meta:
                version: str = "1.5.0"

            value: int

        instance = SampleModel(value=42)
        logger.debug("Instance value: %d", instance.value)
        logger.debug("Instance Meta.version: %s", instance.Meta.version)

        assert instance.Meta.version == "1.5.0"
        logger.info("Meta correctly accessible from instance")

    def test_meta_isolation_between_subclasses(self) -> None:
        """Different subclasses should have isolated Meta."""
        logger.info("Testing Meta isolation between subclasses")

        class ModelA(InternalBaseModel):
            class Meta:
                version: str = "1.0.0"
                category: str = "type_a"

            name: str

        class ModelB(InternalBaseModel):
            class Meta:
                version: str = "2.0.0"
                category: str = "type_b"

            name: str

        logger.debug("ModelA.Meta.version: %s", ModelA.Meta.version)
        logger.debug("ModelB.Meta.version: %s", ModelB.Meta.version)

        assert ModelA.Meta.version == "1.0.0"
        assert ModelB.Meta.version == "2.0.0"
        assert ModelA.Meta.category == "type_a"
        assert ModelB.Meta.category == "type_b"
        logger.info("Meta isolation between subclasses verified")


class TestMetaObservability:
    """Tests for Meta observability features."""

    def test_meta_tags_for_filtering(self) -> None:
        """Meta tags should support filtering use cases."""
        logger.info("Testing Meta tags for filtering")

        class CriticalModel(InternalBaseModel):
            class Meta:
                tags: set[str] = {"critical", "auth", "security"}

            token: str

        class NormalModel(InternalBaseModel):
            class Meta:
                tags: set[str] = {"normal", "user"}

            name: str

        logger.debug("CriticalModel tags: %s", CriticalModel.Meta.tags)
        logger.debug("NormalModel tags: %s", NormalModel.Meta.tags)

        assert "critical" in CriticalModel.Meta.tags
        assert "critical" not in NormalModel.Meta.tags
        logger.info("Meta tags filtering capability verified")

    def test_meta_labels_for_metadata(self) -> None:
        """Meta labels should support structured metadata."""
        logger.info("Testing Meta labels for structured metadata")

        class ProductionModel(InternalBaseModel):
            class Meta:
                labels: dict[str, str] = {
                    "env": "production",
                    "team": "platform",
                    "service": "auth",
                }

            data: str

        labels = ProductionModel.Meta.labels
        logger.debug("ProductionModel labels: %s", labels)

        assert labels["env"] == "production"
        assert labels["team"] == "platform"
        assert labels["service"] == "auth"
        logger.info("Meta labels structured metadata verified")
