# Security Policy

## Supported Versions

We currently provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Development | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Leviftas seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them using one of the following methods:

1. **Recommended**: Use GitHub's private security reporting feature
   - Go to [Security Advisories](https://github.com/Frost-Leo/Leviftas/security/advisories)
   - Click "Report a vulnerability"

2. **Email**: Send details to the project maintainers
   - Include "[SECURITY]" in the subject line

### What to Include

Please include the following information in your report:

- Detailed description of the vulnerability
- Steps to reproduce (if possible)
- Affected versions
- Potential impact and severity assessment
- Any possible mitigations
- Your contact information (optional)

### Security Considerations for Leviftas Components

#### Django & Django REST Framework
- Authentication and authorization vulnerabilities
- SQL injection through ORM misuse
- Cross-site scripting (XSS) in API responses
- Cross-site request forgery (CSRF) protection bypasses

#### RBAC (Role-Based Access Control)
- Permission escalation vulnerabilities
- Role assignment bypasses
- Access control logic flaws
- Privilege boundary violations

#### Pydantic Data Validation
- Input validation bypasses
- Serialization/deserialization vulnerabilities
- Type confusion attacks
- Schema validation circumvention

#### Dynaconf Configuration
- Configuration injection attacks
- Sensitive data exposure in config files
- Environment variable manipulation
- Configuration override vulnerabilities

#### Loguru Logging
- Log injection attacks
- Sensitive data leakage in logs
- Log tampering vulnerabilities
- Information disclosure through logs

#### FastAPI Integration
- API endpoint security issues
- Request/response manipulation
- Authentication bypass in FastAPI routes
- OpenAPI specification information leakage

#### OpenTelemetry Monitoring
- Telemetry data injection
- Monitoring bypass techniques
- Sensitive data exposure in traces
- Performance monitoring abuse

### Response Timeline

1. **Acknowledgment**: We will acknowledge receipt within 48 hours
2. **Initial Assessment**: Initial security assessment within 7 days
3. **Detailed Investigation**: Detailed investigation may take 1-4 weeks depending on complexity
4. **Fix Development**: Development and testing of security fixes
5. **Coordinated Disclosure**: Coordinate public disclosure timing with reporter

### Security Updates

- Security fixes will be prioritized
- We will publish security advisories detailing vulnerabilities and fixes
- Users will be notified through GitHub Releases and project documentation

### Security Best Practices

When using Leviftas, please follow these security best practices:

#### General Security
- Always use the latest version
- Regularly update dependencies
- Disable debug mode in production
- Use strong authentication mechanisms
- Regularly review access permissions
- Monitor for unusual activity

#### Django/DRF Specific
- Configure proper CORS settings
- Use HTTPS in production
- Implement proper session management
- Validate all input data
- Use Django's built-in security features

#### RBAC Implementation
- Follow principle of least privilege
- Regularly audit role assignments
- Implement proper permission checks
- Use secure role inheritance patterns
- Monitor permission changes

#### Configuration Security
- Secure Dynaconf configuration files
- Use environment variables for secrets
- Implement proper secret rotation
- Avoid hardcoded credentials
- Secure configuration file permissions

#### Logging Security
- Configure Loguru to avoid sensitive data logging
- Implement log rotation and retention policies
- Secure log file access
- Monitor logs for security events
- Use structured logging for better analysis

### Acknowledgments

We appreciate security researchers and users who help keep Leviftas secure. Contributors who responsibly report vulnerabilities will be acknowledged in security advisories (unless they prefer to remain anonymous).

## Contact

For any security-related questions, please contact us through the channels mentioned above.