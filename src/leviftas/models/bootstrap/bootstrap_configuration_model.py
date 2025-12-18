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

__init__.py

Bootstrap Configuration Model

- Author   : shadowmoss <ltx1577634892@outlook.com>
- Created  : 2025/12/18 
- Modified : 2025/12/18 
"""
from pydantic_settings import BaseSettings,SettingsConfigDict
from typing_extensions import ClassVar

class BootStrapConfigurationModel(BaseSettings):
    """
        BootStrapConfigurationModel read LEVIFTAS application basic infomation when application startup.
        such as HOST_NAME、OS_VERSION、Process Port、Domain、WorkSpace
    """
    model_config:ClassVar[SettingsConfigDict] = SettingsConfigDict(
        # Specific Environment Variable Prefix
        env_prefix='LEVIFTAS_',
        # Enviroment Variable Case Sentsitive
        case_sensitive=True
    )
    # current host runs LEVIFTAS Application
    APP_HOSTNAME:str
    
    # current os runs LEVIFTAS Application
    OS_VERSION:str

    # current LEVIFTAS Application port
    PORT:int
    
    # current LEVIFTAS Application ip or domain address
    DOMAIN:str

    # current LEVIFTAS Application work Directory address
    WORK_SPACE:str