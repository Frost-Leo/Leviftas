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

test_nacos.py

Tests for NacosConnConfigModel.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/22
- Modified : 2025/12/22
"""

import logging

import pytest
from pydantic import SecretStr, ValidationError

from leviftas.models.bootstrap.config_center import NacosConnConfigModel


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestModelConfig:
    """Tests for NacosConnConfigModel model_config."""

    def test_env_prefix_nacos(self) -> None:
        """env_prefix should be NACOS_."""
        logger.info("Testing env_prefix is NACOS_")
        assert NacosConnConfigModel.model_config.get("env_prefix") == "NACOS_"
        logger.info("env_prefix is NACOS_ as expected")

    def test_inherits_parent_config(self) -> None:
        """Should inherit configuration from parent classes."""
        logger.info("Testing parent config inheritance")

        # Check inherited settings from InternalBaseSettings
        assert NacosConnConfigModel.model_config.get("env_file") == ".env"
        assert NacosConnConfigModel.model_config.get("env_nested_delimiter") == "__"
        assert NacosConnConfigModel.model_config.get("env_file_encoding") == "utf-8"

        logger.info("Parent config inherited correctly")


class TestMeta:
    """Tests for NacosConnConfigModel Meta."""

    def test_not_abstract(self) -> None:
        """Meta.abstract should be False."""
        logger.info("Testing Meta.abstract is False")
        assert NacosConnConfigModel.Meta.abstract is False
        logger.info("Meta.abstract is False")

    def test_type_name_nacos(self) -> None:
        """Meta.type_name should be 'nacos'."""
        logger.info("Testing Meta.type_name")
        assert NacosConnConfigModel.Meta.type_name == "nacos"
        logger.info("Meta.type_name is 'nacos'")


class TestRequiredFields:
    """Tests for required fields."""

    def test_server_address_required(self) -> None:
        """server_address should be required."""
        logger.info("Testing server_address is required")

        with pytest.raises(ValidationError) as exc_info:
            NacosConnConfigModel()

        errors = exc_info.value.errors()
        field_names = [e["loc"][0] for e in errors]
        assert "server_address" in field_names

        logger.info("server_address is correctly required")

    def test_server_address_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """server_address should load from NACOS_SERVER_ADDRESS."""
        logger.info("Testing server_address from env")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "nacos.example.com:8848")
        config = NacosConnConfigModel()

        assert config.server_address == "nacos.example.com:8848"
        logger.info("server_address correctly loaded from env")


class TestDefaultValues:
    """Tests for default values."""

    def test_namespace_id_default_empty(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """namespace_id should default to empty string."""
        logger.info("Testing namespace_id default")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        config = NacosConnConfigModel()

        assert config.namespace_id == ""
        logger.info("namespace_id defaults to empty string")

    def test_username_default_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """username should default to None."""
        logger.info("Testing username default")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        config = NacosConnConfigModel()

        assert config.username is None
        logger.info("username defaults to None")

    def test_password_default_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """password should default to None."""
        logger.info("Testing password default")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        config = NacosConnConfigModel()

        assert config.password is None
        logger.info("password defaults to None")

    def test_access_key_default_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """access_key should default to None."""
        logger.info("Testing access_key default")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        config = NacosConnConfigModel()

        assert config.access_key is None
        logger.info("access_key defaults to None")

    def test_secret_key_default_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """secret_key should default to None."""
        logger.info("Testing secret_key default")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        config = NacosConnConfigModel()

        assert config.secret_key is None
        logger.info("secret_key defaults to None")


class TestSecretStrFields:
    """Tests for SecretStr field types."""

    def test_password_is_secret_str(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """password should be SecretStr type."""
        logger.info("Testing password is SecretStr")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        monkeypatch.setenv("NACOS_PASSWORD", "my_secret_password")

        config = NacosConnConfigModel()

        assert isinstance(config.password, SecretStr)
        assert config.password.get_secret_value() == "my_secret_password"
        # String representation should be masked
        assert "my_secret_password" not in str(config.password)

        logger.info("password correctly uses SecretStr")

    def test_access_key_is_secret_str(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """access_key should be SecretStr type."""
        logger.info("Testing access_key is SecretStr")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        monkeypatch.setenv("NACOS_ACCESS_KEY", "AKID12345")

        config = NacosConnConfigModel()

        assert isinstance(config.access_key, SecretStr)
        assert config.access_key.get_secret_value() == "AKID12345"

        logger.info("access_key correctly uses SecretStr")

    def test_secret_key_is_secret_str(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """secret_key should be SecretStr type."""
        logger.info("Testing secret_key is SecretStr")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        monkeypatch.setenv("NACOS_SECRET_KEY", "secret12345")

        config = NacosConnConfigModel()

        assert isinstance(config.secret_key, SecretStr)
        assert config.secret_key.get_secret_value() == "secret12345"

        logger.info("secret_key correctly uses SecretStr")

    def test_secrets_not_in_model_dump(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Secrets should be masked in model_dump output."""
        logger.info("Testing secrets masked in model_dump")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "localhost:8848")
        monkeypatch.setenv("NACOS_PASSWORD", "super_secret")

        config = NacosConnConfigModel()
        data = config.model_dump()

        # SecretStr is serialized as SecretStr object, not plain string
        assert data["password"] != "super_secret"

        logger.info("Secrets correctly masked in model_dump")


class TestEnvLoading:
    """Tests for environment variable loading."""

    def test_all_fields_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """All fields should load from environment variables."""
        logger.info("Testing all fields from env")

        monkeypatch.setenv("NACOS_SERVER_ADDRESS", "nacos.prod.example.com:8848")
        monkeypatch.setenv("NACOS_NAMESPACE_ID", "prod-namespace")
        monkeypatch.setenv("NACOS_USERNAME", "admin")
        monkeypatch.setenv("NACOS_PASSWORD", "admin123")
        monkeypatch.setenv("NACOS_ACCESS_KEY", "AKID999")
        monkeypatch.setenv("NACOS_SECRET_KEY", "secret999")

        config = NacosConnConfigModel()

        assert config.server_address == "nacos.prod.example.com:8848"
        assert config.namespace_id == "prod-namespace"
        assert config.username == "admin"
        assert config.password is not None
        assert config.password.get_secret_value() == "admin123"
        assert config.access_key is not None
        assert config.access_key.get_secret_value() == "AKID999"
        assert config.secret_key is not None
        assert config.secret_key.get_secret_value() == "secret999"

        logger.info("All fields correctly loaded from env")

    def test_case_insensitive_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Environment variables should be case insensitive."""
        logger.info("Testing case insensitive env loading")

        # Use lowercase env var names
        monkeypatch.setenv("nacos_server_address", "localhost:8848")
        monkeypatch.setenv("nacos_namespace_id", "test-ns")

        config = NacosConnConfigModel()

        assert config.server_address == "localhost:8848"
        assert config.namespace_id == "test-ns"

        logger.info("Case insensitive env loading works")

