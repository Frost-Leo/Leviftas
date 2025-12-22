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

test_base.py

Tests for ConfigCenterBaseModel registry pattern and configuration.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/22
- Modified : 2025/12/22
"""

import logging

import pytest

from leviftas.models.bootstrap.config_center.base import ConfigCenterBaseModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestModelConfig:
    """Tests for ConfigCenterBaseModel model_config."""

    def test_env_prefix_empty(self) -> None:
        """env_prefix should be empty to let subclasses define their own."""
        logger.info("Testing env_prefix is empty")
        assert ConfigCenterBaseModel.model_config.get("env_prefix") == ""
        logger.info("env_prefix is empty as expected")

    def test_inherits_parent_config(self) -> None:
        """Should inherit configuration from InternalBaseSettings."""
        logger.info("Testing parent config inheritance")

        # Check inherited settings
        assert ConfigCenterBaseModel.model_config.get("env_file") == ".env"
        assert ConfigCenterBaseModel.model_config.get("env_nested_delimiter") == "__"
        assert ConfigCenterBaseModel.model_config.get("cli_parse_args") is False

        logger.info("Parent config inherited correctly")


class TestMetaDefaults:
    """Tests for default Meta values."""

    def test_default_abstract_true(self) -> None:
        """Default abstract should be True."""
        logger.info("Testing default Meta.abstract")
        assert ConfigCenterBaseModel.Meta.abstract is True
        logger.info("Default Meta.abstract is True")

    def test_default_type_name_empty(self) -> None:
        """Default type_name should be empty string."""
        logger.info("Testing default Meta.type_name")
        assert ConfigCenterBaseModel.Meta.type_name == ""
        logger.info("Default Meta.type_name is empty")


class TestRegistryPattern:
    """Tests for registry pattern implementation."""

    def test_nacos_registered(self) -> None:
        """NacosConnConfigModel should be registered with type_name 'nacos'."""
        logger.info("Testing Nacos registration")

        # Import to ensure registration
        from leviftas.models.bootstrap.config_center import NacosConnConfigModel

        assert "nacos" in ConfigCenterBaseModel.registry
        assert ConfigCenterBaseModel.registry["nacos"] is NacosConnConfigModel

        logger.info("Nacos correctly registered")

    def test_get_available_types(self) -> None:
        """get_available_types should return list of registered types."""
        logger.info("Testing get_available_types")

        types = ConfigCenterBaseModel.get_available_types()

        assert isinstance(types, list)
        assert "nacos" in types

        logger.debug("Available types: %s", types)
        logger.info("get_available_types works correctly")

    def test_get_by_type_returns_instance(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """get_by_type should return an instance of the registered model."""
        logger.info("Testing get_by_type returns instance")

        # Set required env vars for Nacos
        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")

        instance = ConfigCenterBaseModel.get_by_type("nacos")

        from leviftas.models.bootstrap.config_center import NacosConnConfigModel

        assert isinstance(instance, NacosConnConfigModel)
        assert isinstance(instance, ConfigCenterBaseModel)
        assert instance.server_address == "localhost:8848"

        logger.info("get_by_type correctly returns instance")

    def test_get_by_type_unknown_raises(self) -> None:
        """get_by_type should raise ValueError for unknown types."""
        logger.info("Testing get_by_type with unknown type")

        with pytest.raises(ValueError) as exc_info:
            ConfigCenterBaseModel.get_by_type("unknown_type")

        assert "Unknown config center type" in str(exc_info.value)
        assert "unknown_type" in str(exc_info.value)

        logger.info("Unknown type correctly raises ValueError")

    def test_abstract_class_not_registered(self) -> None:
        """Abstract classes should not be registered."""
        logger.info("Testing abstract class not registered")

        class AbstractConfig(ConfigCenterBaseModel):
            class Meta:
                abstract = True
                type_name = "should_not_register"

            value: str = "test"

        assert "should_not_register" not in ConfigCenterBaseModel.registry

        logger.info("Abstract class correctly not registered")

    def test_duplicate_type_name_raises(self) -> None:
        """Duplicate type_name should raise ValueError."""
        logger.info("Testing duplicate type_name detection")

        with pytest.raises(ValueError) as exc_info:

            class DuplicateNacos(ConfigCenterBaseModel):
                class Meta:
                    abstract = False
                    type_name = "nacos"  # Already registered

                value: str = "test"

        assert "Duplicate config center type_name" in str(exc_info.value)
        assert "nacos" in str(exc_info.value)

        logger.info("Duplicate type_name correctly raises ValueError")

    def test_empty_type_name_not_registered(self) -> None:
        """Classes with empty type_name should not be registered."""
        logger.info("Testing empty type_name not registered")

        registry_size_before = len(ConfigCenterBaseModel.registry)

        class EmptyTypeName(ConfigCenterBaseModel):
            class Meta:
                abstract = False
                type_name = ""

            value: str = "test"

        registry_size_after = len(ConfigCenterBaseModel.registry)

        assert registry_size_after == registry_size_before

        logger.info("Empty type_name correctly not registered")


class TestSubclassInheritance:
    """Tests for subclass configuration inheritance."""

    def test_subclass_inherits_base_config(self) -> None:
        """Subclass should inherit base configuration."""
        logger.info("Testing subclass config inheritance")

        from leviftas.models.bootstrap.config_center import NacosConnConfigModel

        # Should inherit env_file from InternalBaseSettings
        assert NacosConnConfigModel.model_config.get("env_file") == ".env"
        # Should have its own prefix
        assert NacosConnConfigModel.model_config.get("env_prefix") == "NACOS_"

        logger.info("Subclass correctly inherits and overrides config")

