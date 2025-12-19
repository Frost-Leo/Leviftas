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

internal_base_settings.py

Internal base settings model for Leviftas system components. This module provides
a strictly configured Pydantic BaseSettings designed for internal use only,
with security-hardened settings and consistent validation behavior.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/19
- Modified : 2025/12/19
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import ClassVar


class InternalBaseSettings(BaseSettings):
    """
    Base settings model for all internal Leviftas system components.

    This class provides a security-hardened, strictly-typed foundation for
    internal settings models. It enforces consistent validation, serialization,
    and security policies across all internal system components.

    Subclasses should override model_config to set their own env_prefix while
    keeping other settings consistent.

    Attributes:
        model_config (SettingsConfigDict): Pydantic settings configuration with
            security-hardened settings for internal system use.

    Note:
        This model is intended for internal system use only. For public-facing
        APIs or user-defined models, use the appropriate public model classes.
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        # Case insensitive by default.
        case_sensitive=False,
        # Load configuration from .env file in the current working directory.
        env_file=".env",
        # Use UTF-8 encoding for .env file to avoid cross-platform issues.
        env_file_encoding="utf-8",
        # Ignore empty environment variables, use default values instead.
        env_ignore_empty=True,
        # Parse "null" string as None value.
        env_parse_none_str="null",
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
