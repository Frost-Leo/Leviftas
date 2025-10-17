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
- Modified : 2025/10/17
-->

<div align="center">
  <img src="https://frost-leo.github.io/Leviftas/assets/images/github/changelog/header.svg" alt="Changelog Header">
</div>

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] (2025-10-16)


### Features

* **templates:** add enhancement/improvement issue template ([#11](https://github.com/Frost-Leo/Leviftas/issues/11)) ([bc1cff5](https://github.com/Frost-Leo/Leviftas/commit/bc1cff5)), closes [#10](https://github.com/Frost-Leo/Leviftas/issues/10)
  - includes current behavior, expected behavior, and priority fields
  - tracks implementation interest to encourage self-contribution
* **templates:** add documentation issue template ([#11](https://github.com/Frost-Leo/Leviftas/issues/11)) ([7db67e5](https://github.com/Frost-Leo/Leviftas/commit/7db67e5)), closes [#10](https://github.com/Frost-Leo/Leviftas/issues/10)
  - uses simplified unified description approach
  - covers documentation errors, missing docs, and improvements
* **templates:** add maintenance/chore issue template ([#11](https://github.com/Frost-Leo/Leviftas/issues/11)) ([324a186](https://github.com/Frost-Leo/Leviftas/commit/324a186)), closes [#10](https://github.com/Frost-Leo/Leviftas/issues/10)
  - covers dependency updates, configuration changes, CI/CD improvements
  - includes maintenance type categorization
* **ci:** add automated testing workflow ([#9](https://github.com/Frost-Leo/Leviftas/issues/9)) ([e2edee3](https://github.com/Frost-Leo/Leviftas/commit/e2edee3)), closes [#8](https://github.com/Frost-Leo/Leviftas/issues/8)
  - runs pytest with coverage reporting on push and PR
  - integrated with Codecov for coverage tracking


### Bug Fixes

* **workflows:** fix discussion content truncation ([#6](https://github.com/Frost-Leo/Leviftas/issues/6)) ([21b9694](https://github.com/Frost-Leo/Leviftas/commit/21b9694)), closes [#5](https://github.com/Frost-Leo/Leviftas/issues/5)
  - updated regex pattern in `issues-feature-discussion.yml`
  - prevented proposal content from being cut off at internal headings



## [0.1.0] (2025-10-13)

Initial release establishing foundation for Leviftas SDK project.


### Features

* **sdk:** initialize Leviftas SDK package structure ([#7](https://github.com/Frost-Leo/Leviftas/issues/7)) ([9b58ed1](https://github.com/Frost-Leo/Leviftas/commit/9b58ed1)), closes [#3](https://github.com/Frost-Leo/Leviftas/issues/3)
  - created `src/leviftas/` package directory
  - configured `pyproject.toml` following PEP 621 standards
  - set up setuptools build backend
* **testing:** add pytest configuration and test infrastructure ([#7](https://github.com/Frost-Leo/Leviftas/issues/7)) ([cf4d9d8](https://github.com/Frost-Leo/Leviftas/commit/cf4d9d8)), closes [#3](https://github.com/Frost-Leo/Leviftas/issues/3)
  - initialized `tests/` directory structure
  - configured pytest with coverage reporting
  - implemented package metadata validation tests
* **community:** establish GitHub community infrastructure ([#2](https://github.com/Frost-Leo/Leviftas/issues/2)) ([d64c71d](https://github.com/Frost-Leo/Leviftas/commit/d64c71d)), closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - created bug report and feature request templates
  - added PR template with standardized format
* **community:** add community health files ([#2](https://github.com/Frost-Leo/Leviftas/issues/2)) ([b9944d7](https://github.com/Frost-Leo/Leviftas/commit/b9944d7)), closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - `CONTRIBUTING.md` - contribution guidelines
  - `CODE_OF_CONDUCT.md` - community standards (Contributor Covenant v2.1)
  - `SECURITY.md` - security policy and vulnerability reporting
  - `CODEOWNERS` - file ownership and review assignments
* **workflows:** add issue and PR automation ([#2](https://github.com/Frost-Leo/Leviftas/issues/2)) ([2ecb567](https://github.com/Frost-Leo/Leviftas/commit/2ecb567)), closes [#1](https://github.com/Frost-Leo/Leviftas/issues/1)
  - automatic issue title date formatting
  - dynamic header insertion based on labels
  - automatic discussion creation for feature requests
  - PR title formatting and validation
