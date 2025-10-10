# Contributing to Leviftas

Thank you for your interest in contributing to Leviftas! We welcome contributions of all kinds.

## How to Contribute

### Reporting Issues
- Use our [Issue Templates](https://github.com/Frost-Leo/Leviftas/issues/new/choose) to report bugs or request features
- Search existing issues before creating new ones
- Provide detailed information including environment details and reproduction steps

### Submitting Code
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a Pull Request

### Development Environment Setup

#### Prerequisites
- Python 3.13+
- setuptools>=78.1.1
- wheel>=0.45.1

#### Installation
```bash
# Clone the repository
git clone https://github.com/Frost-Leo/Leviftas.git
cd Leviftas

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode with test dependencies
pip install -e ".[test]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=src/leviftas --cov-report=html --cov-report=term
```

#### Project Structure
This project follows the standard `src` layout:
```
leviftas/
├── src/
│   └── leviftas/           # Main package source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── pyproject.toml          # Project configuration
└── README.md
```

#### Key Technologies
Contributors should be familiar with:

- **Django & Django REST Framework**: Core web framework and API development
- **Pydantic**: Data validation and serialization
- **Dynaconf**: Configuration management
- **Loguru**: Advanced logging capabilities
- **RBAC (Role-Based Access Control)**: Permission and authorization system
- **FastAPI**: Alternative API framework integration
- **OpenTelemetry**: Observability and monitoring

### Code Standards

#### Python Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting: `black .`
- Use isort for import sorting: `isort .`
- Use flake8 for linting: `flake8 .`
- Type hints are required for new code

#### Documentation
- Add docstrings to all public functions and classes
- Update README.md for significant changes
- Include inline comments for complex logic
- Document configuration options in Dynaconf settings

#### Testing
- Write unit tests for new features in the `tests/` directory
- Maintain test coverage above 80%
- Use pytest as the testing framework
- Follow pytest naming conventions: `test_*.py` or `*_test.py`
- Test files should mirror the `src/leviftas/` structure
- Use pytest fixtures and markers appropriately
- Test RBAC permissions thoroughly
- Include integration tests for API endpoints

#### Running Tests
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/leviftas --cov-report=html

# Run specific test file
pytest tests/test_example.py

# Run tests with specific marker
pytest -m internal

# Run tests in verbose mode
pytest -v
```

### Commit Message Guidelines
Use the format: `[scope] Brief description (#PR_number)`

#### Scope Categories:
- `[core]` - Core functionality changes
- `[api]` - API endpoint modifications
- `[auth]` - Authentication and RBAC changes
- `[config]` - Configuration and Dynaconf changes
- `[logging]` - Loguru logging improvements
- `[validation]` - Pydantic model and validation changes
- `[monitoring]` - OpenTelemetry and monitoring features
- `[docs]` - Documentation updates
- `[test]` - Test additions or modifications
- `[deps]` - Dependency updates
- `[ci]` - CI/CD and GitHub Actions changes
- `[fix]` - Bug fixes
- `[perf]` - Performance improvements
- `[refactor]` - Code refactoring without functional changes

#### Examples:
- `[auth] Add role-based permission middleware (#123)`
- `[api] Implement user profile endpoints (#456)`
- `[validation] Update Pydantic models for user schema (#789)`
- `[config] Add Dynaconf environment-specific settings (#234)`
- `[logging] Enhance Loguru structured logging format (#567)`
- `[monitoring] Integrate OpenTelemetry tracing (#890)`
- `[fix] Resolve RBAC permission inheritance issue (#345)`
- `[docs] Update API documentation for authentication (#678)`
- `[test] Add comprehensive tests for user management (#901)`
- `[deps] Bump Django to 5.2.4 (#112)`

#### Multi-scope Changes:
For changes affecting multiple areas:
- `[core][auth] Refactor user authentication system (#123)`
- `[api][validation] Update user endpoints with new Pydantic models (#456)`

### Pull Request Guidelines
- Ensure all tests pass
- Update documentation as needed
- Keep PRs focused and atomic
- Provide clear PR descriptions
- Link related issues
- Include screenshots for UI changes
- Test RBAC scenarios if permissions are affected

### Project Configuration
This project uses `pyproject.toml` for configuration:
- All project metadata is defined in `pyproject.toml`
- Dependencies are managed through `pyproject.toml`
- Test configuration is in `[tool.pytest.ini_options]`
- Use `pip install -e ".[test]"` for development installation

When working with Dynaconf:
- Follow the existing configuration structure
- Document new settings appropriately
- Use environment-specific overrides appropriately
- Test configuration changes across environments

### Logging Standards
When using Loguru:
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Include contextual information in log messages
- Follow structured logging practices
- Avoid logging sensitive information

### API Development
For Django REST Framework endpoints:
- Follow RESTful conventions
- Use appropriate HTTP status codes
- Implement proper serialization with Pydantic when applicable
- Include comprehensive API documentation
- Implement proper RBAC checks

### Security Considerations
- Never commit sensitive information
- Follow OWASP security guidelines
- Implement proper input validation
- Use RBAC for all protected endpoints
- Test for common security vulnerabilities

### License
By contributing, you agree that your contributions will be licensed under the GPL-3.0 License.

## Getting Help
- Check existing [Issues](https://github.com/Frost-Leo/Leviftas/issues)
- Join [Discussions](https://github.com/Frost-Leo/Leviftas/discussions)
- Read the project documentation

Thank you for contributing to Leviftas!