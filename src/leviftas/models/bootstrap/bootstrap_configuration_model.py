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

bootstrap_configuration_model.py

Bootstrap configuration model for Leviftas system initialization. This module
provides the minimal configuration required to start the system and connect
to the configuration center. It supports loading from environment variables,
CLI arguments, and .env files.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/19 
- Modified : 2025/12/19
"""

import platform
import socket
import uuid
from typing import Literal, Optional

from platformdirs import user_config_dir
from pydantic import Field, model_validator
from pydantic_settings import SettingsConfigDict
from typing_extensions import ClassVar, Self

from leviftas.models.base.internal_base_settings import InternalBaseSettings
from leviftas.models.bootstrap.config_center import ConfigCenterBaseModel

# Import to trigger registration
from leviftas.models.bootstrap.config_center import NacosConnConfigModel as _  # noqa: F401


class BootstrapConfigurationModel(InternalBaseSettings):
    """
    Bootstrap configuration for Leviftas system startup.

    This class provides the minimal configuration required to initialize the
    system and establish connection to the configuration center. All other
    runtime configurations (MQ, database, etc.) should be fetched from the
    configuration center after bootstrap.

    Attributes:
        model_config (SettingsConfigDict): Pydantic settings configuration
            for environment variables and CLI argument parsing.

    Note:
        Configuration priority (low to high):
        1. Model default values
        2. .env file
        3. Environment variables
        4. CLI arguments
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        # Case insensitive by default.
        case_sensitive=False,
        # Use LEVIFTAS_ as environment variable prefix.
        env_prefix="LEVIFTAS_",
        # Load configuration from .env file in the current working directory.
        env_file=".env",
        # Use UTF-8 encoding for .env file to avoid cross-platform issues.
        env_file_encoding="utf-8",
        # Ignore empty environment variables, use default values instead.
        env_ignore_empty=True,
        # Parse "null" string as None value.
        env_parse_none_str="null",
        # Program name displayed in CLI help message.
        cli_prog_name="leviftas",
        # Enable CLI argument parsing from sys.argv.
        cli_parse_args=True,
        # Parse "null" string as None value in CLI arguments.
        cli_parse_none_str="null",
        # Enable implicit flags: --debug equals --debug=true, --no-debug equals --debug=false.
        cli_implicit_flags=True,
        # Use kebab-case for CLI arguments: --node-id instead of --node_id.
        cli_kebab_case=True,
        # Load secrets from Docker/Kubernetes secrets directory.
        secrets_dir="/run/secrets",
    )

    hostname: str = Field(
        default_factory=socket.gethostname,
        description="Host name of the machine.",
    )
    """Host name of the machine, auto-detected from system."""

    os_type: str = Field(
        default_factory=platform.system,
        description="Operating system type (Windows, Linux, Darwin).",
    )
    """Operating system type, auto-detected from system."""

    os_version: str = Field(
        default_factory=platform.version,
        description="Operating system version.",
    )
    """Operating system version, auto-detected from system."""

    platform_arch: str = Field(
        default_factory=platform.machine,
        description="Platform architecture (x86_64, arm64, etc.).",
    )
    """Platform architecture, auto-detected from system."""

    node_id: str = Field(
        default_factory=socket.gethostname,
        description="Node identifier, shared by all instances on the same machine.",
    )
    """Node identifier from environment variable, defaults to hostname."""

    instance_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique instance identifier, generated on each startup.",
    )
    """Unique instance identifier, auto-generated UUID for each process."""

    service_name: str = Field(
        description="Service name for registration and discovery.",
    )
    """Service name, required field from environment variable or CLI."""

    env: str = Field(
        default="dev",
        description="Runtime environment (dev, staging, prod).",
    )
    """Runtime environment, defaults to dev."""

    config_source: Literal["remote", "local"] = Field(
        default="remote",
        description="Configuration source: 'remote' for config center, 'local' for file.",
    )
    """Configuration source, defaults to remote (config center)."""

    config_center_type: Optional[str] = Field(
        default=None,
        description="Configuration center type (e.g., 'nacos', 'apollo').",
    )
    """Configuration center type, required when config_source is 'remote'."""

    config_center: Optional[ConfigCenterBaseModel] = Field(
        default=None,
        description="Configuration center connection settings, auto-loaded by type.",
    )
    """Configuration center settings, auto-instantiated from registry."""

    config_dir: str = Field(
        default_factory=lambda: user_config_dir("leviftas"),
        description="Local configuration directory path.",
    )
    """Local config directory, defaults to platform-specific user config dir."""

    @model_validator(mode="after")
    def validate_and_load_config(self) -> Self:
        """Validate config_source and auto-load config_center from registry."""
        if self.config_source == "remote":
            if self.config_center_type is None:
                raise ValueError(
                    "config_center_type is required when config_source is 'remote'"
                )
            if self.config_center is None:
                self.config_center = ConfigCenterBaseModel.get_by_type(
                    self.config_center_type
                )
        return self
