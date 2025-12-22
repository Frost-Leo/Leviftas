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

test_bootstrap_configuration.py

Tests for BootstrapConfigurationModel.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/22
- Modified : 2025/12/22
"""

import logging
import platform
import socket

import pytest
from pydantic import ValidationError

from leviftas.models.bootstrap.bootstrap_configuration_model import (
    BootstrapConfigurationModel,
)
from leviftas.models.bootstrap.config_center import (
    ConfigCenterBaseModel,
    NacosConnConfigModel,
)


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestModelConfig:
    """Tests for BootstrapConfigurationModel model_config."""

    def test_cli_parse_args_enabled(self) -> None:
        """CLI parsing should be enabled for bootstrap config."""
        logger.info("Testing cli_parse_args is enabled")
        assert BootstrapConfigurationModel.model_config.get("cli_parse_args") is True
        logger.info("cli_parse_args is enabled")

    def test_cli_prog_name(self) -> None:
        """CLI prog name should be 'leviftas'."""
        logger.info("Testing cli_prog_name")
        assert BootstrapConfigurationModel.model_config.get("cli_prog_name") == "leviftas"
        logger.info("cli_prog_name is 'leviftas'")

    def test_secrets_dir_linux(self) -> None:
        """secrets_dir should be /run/secrets for container deployment."""
        logger.info("Testing secrets_dir")
        assert BootstrapConfigurationModel.model_config.get("secrets_dir") == "/run/secrets"
        logger.info("secrets_dir is /run/secrets")

    def test_inherits_parent_config(self) -> None:
        """Should inherit configuration from InternalBaseSettings."""
        logger.info("Testing parent config inheritance")

        assert BootstrapConfigurationModel.model_config.get("env_prefix") == "LEVIFTAS_"
        assert BootstrapConfigurationModel.model_config.get("env_file") == ".env"
        assert BootstrapConfigurationModel.model_config.get("env_nested_delimiter") == "__"

        logger.info("Parent config inherited correctly")


class TestAutoDetectedFields:
    """Tests for auto-detected system information fields."""

    def test_hostname_auto_detected(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """hostname should be auto-detected from system."""
        logger.info("Testing hostname auto-detection")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.hostname == socket.gethostname()
        logger.info("hostname correctly auto-detected: %s", config.hostname)

    def test_os_type_auto_detected(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """os_type should be auto-detected from system."""
        logger.info("Testing os_type auto-detection")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.os_type == platform.system()
        logger.info("os_type correctly auto-detected: %s", config.os_type)

    def test_os_version_auto_detected(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """os_version should be auto-detected from system."""
        logger.info("Testing os_version auto-detection")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.os_version == platform.version()
        logger.info("os_version correctly auto-detected")

    def test_platform_arch_auto_detected(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """platform_arch should be auto-detected from system."""
        logger.info("Testing platform_arch auto-detection")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.platform_arch == platform.machine()
        logger.info("platform_arch correctly auto-detected: %s", config.platform_arch)

    def test_node_id_defaults_to_hostname(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """node_id should default to hostname."""
        logger.info("Testing node_id defaults to hostname")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.node_id == socket.gethostname()
        logger.info("node_id correctly defaults to hostname")

    def test_instance_id_is_uuid(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """instance_id should be a valid UUID."""
        logger.info("Testing instance_id is UUID")

        import uuid

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        # Should be parseable as UUID
        parsed_uuid = uuid.UUID(config.instance_id)
        assert str(parsed_uuid) == config.instance_id

        logger.info("instance_id is valid UUID: %s", config.instance_id)

    def test_instance_id_unique_per_instance(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Each instance should have a unique instance_id."""
        logger.info("Testing instance_id uniqueness")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config1 = BootstrapConfigurationModel(_cli_parse_args=False)
        config2 = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config1.instance_id != config2.instance_id

        logger.info("instance_id is unique per instance")


class TestRequiredFields:
    """Tests for required fields."""

    def test_service_name_required(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """service_name should be required."""
        logger.info("Testing service_name is required")

        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        with pytest.raises(ValidationError) as exc_info:
            BootstrapConfigurationModel(_cli_parse_args=False)

        errors = exc_info.value.errors()
        field_names = [e["loc"][0] for e in errors]
        assert "service_name" in field_names

        logger.info("service_name is correctly required")


class TestDefaultValues:
    """Tests for default values."""

    def test_env_default_dev(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """env should default to 'dev'."""
        logger.info("Testing env default")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.env == "dev"
        logger.info("env defaults to 'dev'")

    def test_config_source_default_remote(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """config_source should default to 'remote'."""
        logger.info("Testing config_source default")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_CENTER_TYPE", "nacos")
        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.config_source == "remote"
        logger.info("config_source defaults to 'remote'")

    def test_config_dir_uses_platformdirs(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """config_dir should use platformdirs for default."""
        logger.info("Testing config_dir default")

        from platformdirs import user_config_dir

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        expected_dir = user_config_dir("leviftas")
        assert config.config_dir == expected_dir

        logger.info("config_dir correctly uses platformdirs: %s", config.config_dir)


class TestConfigSourceValidation:
    """Tests for config_source validation logic."""

    def test_remote_requires_config_center_type(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """config_source='remote' should require config_center_type."""
        logger.info("Testing remote requires config_center_type")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "remote")
        # Not setting config_center_type

        with pytest.raises(ValueError) as exc_info:
            BootstrapConfigurationModel(_cli_parse_args=False)

        assert "config_center_type is required" in str(exc_info.value)

        logger.info("remote correctly requires config_center_type")

    def test_local_does_not_require_config_center_type(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """config_source='local' should not require config_center_type."""
        logger.info("Testing local does not require config_center_type")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.config_source == "local"
        assert config.config_center_type is None
        assert config.config_center is None

        logger.info("local correctly does not require config_center_type")

    def test_config_source_literal_validation(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """config_source should only accept 'remote' or 'local'."""
        logger.info("Testing config_source literal validation")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "invalid")

        with pytest.raises(ValidationError):
            BootstrapConfigurationModel(_cli_parse_args=False)

        logger.info("config_source correctly validates literal values")


class TestConfigCenterAutoLoad:
    """Tests for automatic config_center loading."""

    def test_auto_load_nacos_config(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should auto-load NacosConnConfigModel when type is 'nacos'."""
        logger.info("Testing auto-load Nacos config")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "remote")
        monkeypatch.setenv("LEVIFTAS_CONFIG_CENTER_TYPE", "nacos")
        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "nacos.example.com:8848")
        monkeypatch.setenv("NACOS_NAMESPACE_ID", "prod")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.config_center is not None
        assert isinstance(config.config_center, NacosConnConfigModel)
        assert isinstance(config.config_center, ConfigCenterBaseModel)
        assert config.config_center.server_address == "nacos.example.com:8848"
        assert config.config_center.namespace_id == "prod"

        logger.info("Nacos config correctly auto-loaded")

    def test_unknown_config_center_type_raises(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Unknown config_center_type should raise ValueError."""
        logger.info("Testing unknown config_center_type")

        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "remote")
        monkeypatch.setenv("LEVIFTAS_CONFIG_CENTER_TYPE", "unknown")

        with pytest.raises(ValueError) as exc_info:
            BootstrapConfigurationModel(_cli_parse_args=False)

        assert "Unknown config center type" in str(exc_info.value)

        logger.info("Unknown config_center_type correctly raises ValueError")


class TestEnvLoading:
    """Tests for environment variable loading."""

    def test_all_fields_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """All fields should load from environment variables."""
        logger.info("Testing all fields from env")

        monkeypatch.setenv("LEVIFTAS_HOSTNAME", "custom-host")
        monkeypatch.setenv("LEVIFTAS_NODE_ID", "node-001")
        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "my-service")
        monkeypatch.setenv("LEVIFTAS_ENV", "production")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")
        monkeypatch.setenv("LEVIFTAS_CONFIG_DIR", "/etc/leviftas")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.hostname == "custom-host"
        assert config.node_id == "node-001"
        assert config.service_name == "my-service"
        assert config.env == "production"
        assert config.config_source == "local"
        assert config.config_dir == "/etc/leviftas"

        logger.info("All fields correctly loaded from env")

    def test_env_overrides_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Environment variables should override defaults."""
        logger.info("Testing env overrides defaults")

        original_hostname = socket.gethostname()

        monkeypatch.setenv("LEVIFTAS_HOSTNAME", "overridden-host")
        monkeypatch.setenv("LEVIFTAS_SERVICE_NAME", "test-service")
        monkeypatch.setenv("LEVIFTAS_CONFIG_SOURCE", "local")

        config = BootstrapConfigurationModel(_cli_parse_args=False)

        assert config.hostname != original_hostname
        assert config.hostname == "overridden-host"

        logger.info("Env correctly overrides defaults")

