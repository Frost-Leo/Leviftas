#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
conftest

This module provides 

Copyright © 2025 Leviftas authors. All rights reserved.

SPDX-License-Identifier: GPL-3.0-or-later

For the full license text, see <https://www.gnu.org/licenses/gpl-3.0.html>

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/9/29
- Modified : 2025/9/29
"""

import sys
from logging import getLogger
from pathlib import Path
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.reports import TestReport

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

# Export the fixtures required for the test
from tests.fixtures.internal.models.base.internal_base_model.fixtures import *

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