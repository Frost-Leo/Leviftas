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

conftest.py

Prerequisite configuration for testing.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/10 
- Modified : 2025/10/10

"""

import sys
from pathlib import Path
from logging import getLogger
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.reports import TestReport

from tests.fixtures.internal.models.base.internal_base_model.fixtures import *

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))


def pytest_exception_interact(
        node: Item,
        call: CallInfo,
        report: TestReport,
) -> None:
    """
    Catch all test exceptions and log them to file.

    This hook is called when an exception occurs during test execution,
    allowing us to capture and log detailed exception information.

    Args:
        node (Item): The pytest test item (test function/method) that failed
        call (CallInfo): Information about the test call, including exception details
        report (TestReport): The test report containing failure information

    Returns:
        None

    Note:
        This function is automatically called by pytest when a test fails.
        It logs the exception details to both console and file logs.
    """
    if report.failed and call.excinfo is not None:
        exception_logger = getLogger("pytest.exceptions")

        exception_logger.error(f"Test failed: {node.nodeid}")
        exception_logger.error(f"Exception type: {call.excinfo.typename}")
        exception_logger.error(f"Exception value: {call.excinfo.value}")

        if call.excinfo.traceback is not None:
            exception_logger.error(f"Traceback: {call.excinfo.traceback}")

        exception_logger.error(f"Full exception repr:\n{call.excinfo.getrepr()}")

        exception_logger.error(f"Test phase: {report.when}")

        if hasattr(report, 'longrepr') and report.longrepr:
            exception_logger.error(f"Detailed failure info:\n{report.longrepr}")