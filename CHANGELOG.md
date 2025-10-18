<!--
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

CHANGELOG.md

Version history and change log for Leviftas project following Keep a Changelog format.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/17
- Modified : 2025/10/19
-->

<div align="center">
  <img src="https://frost-leo.github.io/Leviftas/assets/images/github/changelog/header.svg" alt="Changelog Header">
</div>

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [0.2.0-dev] - In Development

Development version preparing for v0.2.0 release with version management improvements.

### Added
- **Issue Templates** ([#16](https://github.com/Frost-Leo/Leviftas/issues/16))
  - Version 0.2 label to all issue templates for better milestone tracking and categorization
  - Improved template organization for v0.2.0 development cycle

### Changed
- **Version Management** ([#16](https://github.com/Frost-Leo/Leviftas/issues/16))
  - Version number updated from `0.1.1` to `0.2.0-dev` in `src/leviftas/__init__.py`
  - Established clear version boundary between stable v0.1 and development v0.2
- **Documentation** ([#16](https://github.com/Frost-Leo/Leviftas/issues/16))
  - Restructured CHANGELOG.md following Keep a Changelog format more strictly
  - Reorganized v0.1 release entries with better categorization and functional grouping
  - Added comprehensive descriptions for historical releases
  - Aligned version management strategy with simplified tagging approach

---

## [0.1.1] - 2025-10-17

Second development iteration expanding GitHub community infrastructure and establishing changelog documentation.

### Added
- **Issue Templates** ([#11](https://github.com/Frost-Leo/Leviftas/pull/11)) - Closes [#10](https://github.com/Frost-Leo/Leviftas/issues/10)
  - Enhancement/Improvement template with priority tracking and implementation interest fields
  - Documentation template covering errors, missing docs, and improvements with unified description
  - Maintenance/Chore template for dependency updates, configuration changes, and CI/CD improvements
- **CI/CD** ([#9](https://github.com/Frost-Leo/Leviftas/pull/9)) - Closes [#8](https://github.com/Frost-Leo/Leviftas/issues/8)
  - GitHub Actions workflow for automated testing on push and pull requests
  - Pytest execution with coverage reporting for Python 3.13
  - Codecov integration for coverage tracking and reporting
- **Documentation** ([#13](https://github.com/Frost-Leo/Leviftas/pull/13)) - Closes [#12](https://github.com/Frost-Leo/Leviftas/issues/12)
  - `CHANGELOG.md` following Keep a Changelog v1.0.0 specification
  - Changelog header SVG visual asset
  - Comprehensive documentation of v0.1.0 release

### Fixed
- **GitHub Workflows** ([#6](https://github.com/Frost-Leo/Leviftas/pull/6)) - Closes [#5](https://github.com/Frost-Leo/Leviftas/issues/5)
  - Discussion proposal content truncation in `issues-feature-discussion.yml`
  - Updated regex pattern to preserve complete proposal content including internal headings
  - Improved content extraction for feature request discussions

---

## [0.1.0] - 2025-10-16

**First pre-release** establishing the foundation and core infrastructure for the Leviftas SDK project.

### Added
- **SDK Package Structure** ([#7](https://github.com/Frost-Leo/Leviftas/pull/7)) - Closes [#3](https://github.com/Frost-Leo/Leviftas/issues/3)
  - `src/leviftas/` package directory with proper initialization
  - Package metadata: `__version__`, `__author__`, `__email__`, `__license__`
  - GPL-3.0 license headers and comprehensive documentation
- **Build System** ([#7](https://github.com/Frost-Leo/Leviftas/pull/7)) - Closes [#3](https://github.com/Frost-Leo/Leviftas/issues/3)
  - `pyproject.toml` configuration following modern Python packaging standards (PEP 621)
  - Setuptools build backend with dynamic version reading
  - Project metadata, dependencies, and classifiers
  - Optional test dependencies group
- **Testing Infrastructure** ([#7](https://github.com/Frost-Leo/Leviftas/pull/7)) - Closes [#3](https://github.com/Frost-Leo/Leviftas/issues/3)
  - `tests/` directory structure with `conftest.py`
  - Pytest configuration with HTML and terminal coverage reporting
  - Test markers and branch coverage analysis
  - Package metadata validation tests (5 tests passing)
- **GitHub Community Infrastructure** ([#2](https://github.com/Frost-Leo/Leviftas/pull/2)) - Closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - Issue templates: Bug Report (`bug_report.yml`) and Feature Request (`feature_request.yml`)
  - Pull Request template (`PULL_REQUEST_TEMPLATE.md`) with testing checklist
  - Issue template configuration disabling blank issues
- **Community Health Files** ([#2](https://github.com/Frost-Leo/Leviftas/pull/2)) - Closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - `CONTRIBUTING.md` - Contribution guidelines and development workflow
  - `CODE_OF_CONDUCT.md` - Community behavior standards (Contributor Covenant v2.1)
  - `SECURITY.md` - Security policy and vulnerability reporting procedures
  - `CODEOWNERS` - File ownership definitions and automatic review assignments
- **Automation Workflows** ([#2](https://github.com/Frost-Leo/Leviftas/pull/2)) - Closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - Issue automation: automatic date formatting, dynamic header insertion, discussion creation
  - PR automation: title formatting and validation, metadata insertion, label assignment
- **Visual Assets** ([#2](https://github.com/Frost-Leo/Leviftas/pull/2)) - Closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - Professional SVG graphics for templates and workflows
  - Consistent visual style using project theme colors
  - Organized asset structure in `docs/assets/images/github/`

---

## Release Links

- [0.1](https://github.com/Frost-Leo/Leviftas/releases/tag/0.1) - First pre-release (2025-10-16)

---

**Note**: This project uses simplified version tagging (e.g., `0.1`, `0.2`) similar to Python's release branch strategy. CHANGELOG maintains detailed revision history (e.g., `0.1.0`, `0.1.1`) for development tracking, but only major/minor versions receive git tags.
