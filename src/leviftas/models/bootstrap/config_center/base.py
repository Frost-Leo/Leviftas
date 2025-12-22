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

base.py

Base model for configuration center connection models. Implements the Registry
pattern for auto-discovery and instantiation of configuration center models.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/12/19
- Modified : 2025/12/19
"""

from pydantic_settings import SettingsConfigDict
from typing_extensions import Any, ClassVar

from leviftas.models.base.internal_base_settings import InternalBaseSettings


class ConfigCenterBaseModel(InternalBaseSettings):
    """
    Base class for all configuration center connection models.

    Implements an auto-registration mechanism via the `registry` class attribute.
    Subclasses are automatically registered by their `type_name` defined in Meta.

    Attributes:
        registry (ClassVar[dict[str, type[ConfigCenterBaseModel]]]):
            Central registry for all configuration center models.
            Maps type names to their corresponding model classes.
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        # Inherit all settings from parent class.
        **InternalBaseSettings.model_config,
        # Clear env_prefix to let subclasses define their own.
        env_prefix="",
    )

    registry: ClassVar[dict[str, type["ConfigCenterBaseModel"]]] = {}

    class Meta:
        """
        Metadata configuration for configuration center models.

        Attributes:
            abstract (bool): If True, this class won't be registered.
            type_name (str): Unique identifier for the config center type.
        """

        abstract: bool = True
        type_name: str = ""

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        """
        Hook called when a class is subclassed.

        Registers the subclass to the global registry unless it is marked as abstract.
        """
        super().__pydantic_init_subclass__(**kwargs)

        if getattr(cls.Meta, "abstract", False):
            return

        type_name = getattr(cls.Meta, "type_name", "")
        if type_name:
            if type_name in ConfigCenterBaseModel.registry:
                existing_cls = ConfigCenterBaseModel.registry[type_name]
                raise ValueError(
                    f"Duplicate config center type_name '{type_name}': "
                    f"{cls.__name__} conflicts with {existing_cls.__name__}"
                )
            ConfigCenterBaseModel.registry[type_name] = cls

    @classmethod
    def get_by_type(cls, type_name: str) -> "ConfigCenterBaseModel":
        """
        Get and instantiate a configuration center model by type name.

        The model will automatically load values from environment variables
        based on its configured env_prefix.

        Args:
            type_name: The type identifier (e.g., "nacos", "apollo").

        Returns:
            An instantiated configuration center model.

        Raises:
            ValueError: If the type name is not found in the registry.
        """
        model_cls = cls.registry.get(type_name)
        if not model_cls:
            available = ", ".join(cls.registry.keys()) or "none"
            raise ValueError(
                f"Unknown config center type: '{type_name}'. Available types: {available}"
            )
        return model_cls()

    @classmethod
    def get_available_types(cls) -> list[str]:
        """
        Get a list of all registered configuration center types.

        Returns:
            List of available type names.
        """
        return list(cls.registry.keys())
