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

CONTRIBUTING.md

Leviftas project Contributing Guidelines.

- Author   : FrostLeo <frostleo.dev@gmail.com>
- Created  : 2025/10/15
- Modified : 2025/10/15
-->

<div align="center">

![Contributing Guidelines Header](https://frost-leo.github.io/Leviftas/assets/images/github/contributing/header.svg)

</div>

Thank you for your interest in the Leviftas project! This guide covers the basic contribution process for our community.

![Issue Guidelines](https://frost-leo.github.io/Leviftas/assets/images/github/contributing/issue-guidelines.svg)

### Feature Requests

1. **Create a Feature Issue** - Use our [Feature Request template](https://github.com/Frost-Leo/Leviftas/issues/new?template=feature-request.yml)
2. **Automatic Discussion Creation** - Our CI will automatically create a discussion if you select that option
3. **Wait for community feedback** before starting implementation

### Bug Reports

1. **Search existing Issues** first
2. **Use our [Bug Report template](https://github.com/Frost-Leo/Leviftas/issues/new?template=bug_report.yml)**
3. **Include reproduction steps and environment details**

![Commit Message Guidelines](https://frost-leo.github.io/Leviftas/assets/images/github/contributing/commit-guidelines.svg)

### Commit Message Format

```
gh-<issue_number> [<type>]: <date> | <summary_description>

<detailed_description>

Refs #<issue_number>

Signed-off-by: <name> <email>
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `refactor` | Code refactoring |
| `test` | Tests |
| `style` | Code style |
| `perf` | Performance |
| `build` | Build system |
| `ci` | CI/CD |
| `chore` | Maintenance |

### Example

```
gh-1 [feat]: 2025-10-14 | Add automated issue title formatting workflow

- Add issues-add-date.yml for automatic date formatting
- Support various date formats and handle edge cases

Refs #1

Signed-off-by: FrostLeo <frostleo.dev@gmail.com>
```

---

More detailed guidelines will be added as the project grows.
