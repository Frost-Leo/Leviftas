# Getting Help

Thank you for using Leviftas! If you need help, please check the following resources.

## Documentation

- **Project Documentation**: Check the [docs/](../docs/) directory for detailed documentation
- **README**: [README.md](../README.md) contains quick start guide
- **API Documentation**: Access `/docs/` endpoint when running the project for interactive API docs

## Technology Stack Resources

### Core Frameworks
- **Django Documentation**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **FastAPI Documentation**: https://fastapi.tiangolo.com/

### Key Libraries
- **Pydantic**: https://docs.pydantic.dev/ - Data validation and serialization
- **Dynaconf**: https://dynaconf.readthedocs.io/ - Configuration management
- **Loguru**: https://loguru.readthedocs.io/ - Advanced logging
- **OpenTelemetry**: https://opentelemetry.io/docs/ - Observability and monitoring

### RBAC (Role-Based Access Control)
- Understanding permission systems in Django
- Custom RBAC implementation patterns
- Role hierarchy and inheritance
- Permission checking best practices

## Common Issues

### Installation and Setup
- Ensure you're using Python 3.13+
- Install in development mode: `pip install -e ".[test]"`
- Verify all dependencies are correctly installed
- Check project structure follows src layout
- Validate Pydantic model definitions
- Run tests to verify installation: `pytest`

### Configuration Issues (Dynaconf)
- Check `settings.toml` configuration syntax
- Verify environment-specific overrides
- Ensure proper secret management
- Validate configuration loading order

### Authentication and RBAC
- Verify role assignments are correct
- Check permission decorators on views
- Ensure proper user authentication flow
- Validate RBAC policy definitions

### API Development
- Check Django REST Framework serializers
- Verify Pydantic model validation
- Ensure proper HTTP status codes
- Validate API endpoint permissions

### Logging Issues (Loguru)
- Check log configuration settings
- Verify log file permissions
- Ensure proper log rotation setup
- Validate structured logging format

### Performance and Monitoring
- Check OpenTelemetry configuration
- Verify database query optimization
- Monitor API response times
- Validate caching implementation

## Getting Help

### 1. Search Existing Resources
Before asking questions, please:
- Search [existing Issues](https://github.com/Frost-Leo/Leviftas/issues)
- Check [Discussions](https://github.com/Frost-Leo/Leviftas/discussions)
- Read project documentation
- Review technology stack documentation

### 2. Create an Issue
If you encounter a bug or have a feature request:
- Use appropriate [Issue Templates](https://github.com/Frost-Leo/Leviftas/issues/new/choose)
- Provide detailed information and reproduction steps
- Include environment information (Python version, Django version, etc.)
- Specify which component is affected (Django, Pydantic, RBAC, etc.)

### 3. Join Discussions
For general questions and discussions:
- Use [GitHub Discussions](https://github.com/Frost-Leo/Leviftas/discussions)
- Choose appropriate discussion category
- Provide clear problem description
- Mention relevant technologies (Dynaconf, Loguru, etc.)

### 4. Contribute Code
If you want to contribute:
- Read [Contributing Guidelines](CONTRIBUTING.md)
- Fork the project and create Pull Requests
- Follow code standards and testing requirements
- Understand the RBAC system before making permission changes

## Reporting Bugs

Use the [Bug Report Template](https://github.com/Frost-Leo/Leviftas/issues/new?template=bug_report.yml) and include:

- **Environment Information**: OS, Python version, package version (`pip show leviftas`)
- **Component Affected**: Django, Pydantic, Dynaconf, Loguru, RBAC, FastAPI, etc.
- **Installation Method**: `pip install leviftas` or `pip install -e ".[test]"`
- **Reproduction Steps**: Detailed steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Error Messages**: Complete error stack traces
- **Test Results**: Output from `pytest` if relevant
- **Configuration**: Relevant settings (sanitized)
- **Code Samples**: Minimal reproduction code

## Feature Requests

Use the [Feature Request Template](https://github.com/Frost-Leo/Leviftas/issues/new?template=feature_request.yml):

- **Problem Description**: What problem are you trying to solve
- **Proposed Solution**: How you'd like it implemented
- **Technology Integration**: Which components it affects (RBAC, Pydantic, etc.)
- **Alternative Solutions**: Other approaches you've considered
- **Use Cases**: Specific usage scenarios

## Response Times

We strive to respond promptly, but please understand:

- **Bug Reports**: Usually responded to within 2-3 business days
- **Feature Requests**: May require longer evaluation time
- **Security Issues**: Please see [Security Policy](SECURITY.md)
- **General Questions**: Community members may respond faster

## Community Guidelines

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a friendly and respectful environment.

## Technology-Specific Help

### Django/DRF Issues
- Check Django and DRF documentation first
- Verify model relationships and serializers
- Ensure proper URL routing
- Check middleware configuration

### Pydantic Problems
- Validate model definitions
- Check type annotations
- Verify serialization/deserialization
- Ensure proper validation rules

### Dynaconf Configuration
- Check configuration file syntax
- Verify environment variable loading
- Ensure proper secret management
- Test configuration in different environments

### RBAC Implementation
- Understand role hierarchy
- Check permission assignments
- Verify access control decorators
- Test permission inheritance

### Loguru Logging
- Check log configuration
- Verify log formatting
- Ensure proper log levels
- Test log rotation settings

Thank you for your support and contribution to Leviftas!