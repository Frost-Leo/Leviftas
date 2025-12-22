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

test_config.py

Tests for InternalBaseSettings configuration.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/22
- Modified : 2025/12/22
"""

import logging

import pytest

from leviftas.models.base.internal_base_settings import InternalBaseSettings


logger = logging.getLogger(__name__)

pytestmark = pytest.mark.internal


class TestModelConfigDefaults:
    """Tests for default model_config values."""

    def test_env_prefix_default(self) -> None:
        """Default env_prefix should be LEVIFTAS_."""
        logger.info("Testing default env_prefix")
        assert InternalBaseSettings.model_config.get("env_prefix") == "LEVIFTAS_"
        logger.info("Default env_prefix is LEVIFTAS_")

    def test_env_nested_delimiter_default(self) -> None:
        """Default env_nested_delimiter should be __."""
        logger.info("Testing default env_nested_delimiter")
        assert InternalBaseSettings.model_config.get("env_nested_delimiter") == "__"
        logger.info("Default env_nested_delimiter is __")

    def test_cli_parse_args_disabled(self) -> None:
        """CLI parsing should be disabled by default."""
        logger.info("Testing cli_parse_args default")
        assert InternalBaseSettings.model_config.get("cli_parse_args") is False
        logger.info("cli_parse_args is disabled by default")

    def test_secrets_dir_none(self) -> None:
        """secrets_dir should be None by default for cross-platform support."""
        logger.info("Testing secrets_dir default")
        assert InternalBaseSettings.model_config.get("secrets_dir") is None
        logger.info("secrets_dir is None by default")

    def test_env_file_default(self) -> None:
        """Default env_file should be .env."""
        logger.info("Testing default env_file")
        assert InternalBaseSettings.model_config.get("env_file") == ".env"
        logger.info("Default env_file is .env")

    def test_env_file_encoding_utf8(self) -> None:
        """env_file_encoding should be utf-8."""
        logger.info("Testing env_file_encoding")
        assert InternalBaseSettings.model_config.get("env_file_encoding") == "utf-8"
        logger.info("env_file_encoding is utf-8")

    def test_case_insensitive(self) -> None:
        """case_sensitive should be False."""
        logger.info("Testing case_sensitive")
        assert InternalBaseSettings.model_config.get("case_sensitive") is False
        logger.info("case_sensitive is False")


class TestEnvVariableLoading:
    """Tests for environment variable loading."""

    def test_load_from_env_with_prefix(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should load values from environment variables with LEVIFTAS_ prefix."""
        logger.info("Testing env variable loading with prefix")

        class TestSettings(InternalBaseSettings):
            test_value: str = "default"

        monkeypatch.setenv("LEVIFTAS_TEST_VALUE", "from_env")
        settings = TestSettings()

        logger.debug("Loaded test_value: %s", settings.test_value)
        assert settings.test_value == "from_env"
        logger.info("Successfully loaded value from env with prefix")

    def test_env_ignore_empty(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Empty environment variables should be ignored."""
        logger.info("Testing empty env variable handling")

        class TestSettings(InternalBaseSettings):
            test_value: str = "default"

        monkeypatch.setenv("LEVIFTAS_TEST_VALUE", "")
        settings = TestSettings()

        logger.debug("Loaded test_value: %s", settings.test_value)
        assert settings.test_value == "default"
        logger.info("Empty env variable correctly ignored")

    def test_env_parse_none_str(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """String 'null' should be parsed as None."""
        logger.info("Testing null string parsing")

        class TestSettings(InternalBaseSettings):
            test_value: str | None = "default"

        monkeypatch.setenv("LEVIFTAS_TEST_VALUE", "null")
        settings = TestSettings()

        logger.debug("Loaded test_value: %s", settings.test_value)
        assert settings.test_value is None
        logger.info("'null' string correctly parsed as None")


class TestNestedEnvDelimiter:
    """Tests for nested environment variable delimiter."""

    def test_nested_model_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Nested models should load from env using __ delimiter."""
        logger.info("Testing nested model env loading")

        class DatabaseSettings(InternalBaseSettings):
            model_config = InternalBaseSettings.model_config.copy()
            host: str = "localhost"
            port: int = 5432

        class AppSettings(InternalBaseSettings):
            database: DatabaseSettings = DatabaseSettings()

        monkeypatch.setenv("LEVIFTAS_DATABASE__HOST", "prod-db.example.com")
        monkeypatch.setenv("LEVIFTAS_DATABASE__PORT", "5433")

        settings = AppSettings()

        logger.debug("Loaded database.host: %s", settings.database.host)
        logger.debug("Loaded database.port: %d", settings.database.port)

        assert settings.database.host == "prod-db.example.com"
        assert settings.database.port == 5433
        logger.info("Nested model correctly loaded from env")


class TestSubclassOverride:
    """Tests for subclass configuration override."""

    def test_subclass_can_override_env_prefix(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Subclass should be able to override env_prefix."""
        logger.info("Testing subclass env_prefix override")

        from pydantic_settings import SettingsConfigDict
        from typing_extensions import ClassVar

        class CustomSettings(InternalBaseSettings):
            model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
                **{**InternalBaseSettings.model_config, "env_prefix": "CUSTOM_"},
            )
            custom_value: str = "default"

        monkeypatch.setenv("CUSTOM_CUSTOM_VALUE", "overridden")
        settings = CustomSettings()

        logger.debug("Loaded custom_value: %s", settings.custom_value)
        assert settings.custom_value == "overridden"
        logger.info("Subclass env_prefix override works correctly")

    def test_subclass_can_enable_cli(self) -> None:
        """Subclass should be able to enable CLI parsing."""
        logger.info("Testing subclass CLI enable")

        from pydantic_settings import SettingsConfigDict
        from typing_extensions import ClassVar

        class CliSettings(InternalBaseSettings):
            model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
                **{
                    **InternalBaseSettings.model_config,
                    "cli_parse_args": True,
                    "cli_prog_name": "test-cli",
                },
            )

        assert CliSettings.model_config.get("cli_parse_args") is True
        assert CliSettings.model_config.get("cli_prog_name") == "test-cli"
        logger.info("Subclass CLI enable works correctly")

