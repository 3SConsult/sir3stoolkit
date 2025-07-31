# Security Policy

## Supported Versions

The SIR 3S Toolkit (`sir3stoolkit`) currently supports only the latest stable release published on [PyPI](https://pypi.org/project/sir3stoolkit/).

## Security Scope

This Python package is a client-side wrapper for the proprietary simulation software **SIR 3S** by 3S Consult.  
It does **not contain any server-side components, network services, or execution environments**.  
There are no known remote entry points or executable interfaces that would expose users to network-based attacks.

As such, the attack surface of this package is limited to:
- Python code execution within the local environment of the user
- File system interactions initiated by the user

Nevertheless, we encourage responsible disclosure of any potential issues.

## Reporting a Vulnerability

If you discover a potential vulnerability, even if minor or theoretical, please report it privately.

📧 Contact: [sir3stoolkit@3sconsult.de](mailto:sir3stoolkit@3sconsult.de)

Please include:
- A clear description of the issue
- Steps to reproduce (if applicable)
- Affected version
- Any relevant logs or traceback
- Your suggested fix or mitigation (optional)

We strive to review reported security issues within a reasonable timeframe, but response times may vary depending on project availability.

## Responsible Disclosure

Please **do not** create public GitHub issues for vulnerabilities.  
This helps protect users while we assess and address the issue.

We appreciate your contribution to keeping the SIR 3S Toolkit safe and reliable.
