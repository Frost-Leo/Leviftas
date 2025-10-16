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

test_pkg_metadata.py

Package metadata validation tests.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/16 
- Modified : 2025/10/16
"""

import re


class TestPackageMetadata:
    """
    Package metadata test suite.
    
    Attributes:
        None
    """

    def test_version(self):
        """
        Test that __version__ exists and follows semantic versioning format.
        
        Args:
            None
            
        Returns:
            None
        """
        from leviftas import __version__
        
        assert __version__ is not None
        assert isinstance(__version__, str)
        assert re.match(r"^\d+\.\d+\.\d+$", __version__), \
            f"Version '{__version__}' does not match semantic versioning"

    def test_author(self):
        """
        Test that __author__ exists and matches expected value.
        
        Args:
            None
            
        Returns:
            None
        """
        from leviftas import __author__
        
        assert __author__ == "Frost Leo"

    def test_email(self):
        """
        Test that __email__ exists and matches expected value.
        
        Args:
            None
            
        Returns:
            None
        """
        from leviftas import __email__
        
        assert __email__ == "frostleo.dev@gmail.com"

    def test_license(self):
        """
        Test that __license__ exists and matches expected value.
        
        Args:
            None
            
        Returns:
            None
        """
        from leviftas import __license__
        
        assert __license__ == "GPL-3.0-or-later"

    def test_all_exports(self):
        """
        Test that __all__ contains expected exports.
        
        Args:
            None
            
        Returns:
            None
        """
        from leviftas import __all__
        
        assert "__version__" in __all__
