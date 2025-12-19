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

nacos_conn_config_model.py

Minimal Nacos configuration center connection model for bootstrap phase.
Full Nacos client configuration should be defined in the Nacos module.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/19
- Modified : 2025/12/19
"""

from typing import Optional

from pydantic import Field
from pydantic_settings import SettingsConfigDict
from typing_extensions import ClassVar

from leviftas.models.bootstrap.config_center.base import ConfigCenterBaseModel


class NacosConnConfigModel(ConfigCenterBaseModel):
    """
    Minimal Nacos configuration center connection settings for bootstrap.

    This model contains only the essential fields required to establish
    initial connection to Nacos. Full Nacos client configuration should
    be defined in the Nacos module.
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="NACOS_",
        cli_prog_name="nacos",
    )

    class Meta:
        """Nacos configuration center metadata."""

        abstract = False
        type_name = "nacos"

    server_address: str = Field(
        description="Nacos server address (e.g., 'localhost:8848').",
    )
    """Nacos server address, required field."""

    namespace_id: str = Field(
        default="",
        description="Nacos namespace ID, empty string for public namespace.",
    )
    """Nacos namespace ID, defaults to public namespace."""

    username: Optional[str] = Field(
        default=None,
        description="Nacos authentication username.",
    )
    """Nacos username for authentication."""

    password: Optional[str] = Field(
        default=None,
        description="Nacos authentication password.",
    )
    """Nacos password for authentication."""

    access_key: Optional[str] = Field(
        default=None,
        description="Alibaba Cloud access key ID for ACM mode.",
    )
    """Alibaba Cloud access key for ACM authentication."""

    secret_key: Optional[str] = Field(
        default=None,
        description="Alibaba Cloud secret key for ACM mode.",
    )
    """Alibaba Cloud secret key for ACM authentication."""
