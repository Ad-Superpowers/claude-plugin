# Security Policy

## Supported Versions

Security fixes land on the current minor release. Older lines are not backported,
so please update before reporting an issue you found on an earlier version.

| Version | Supported |
|---------|-----------|
| 2.2.x   | Yes       |
| 2.1.x   | Security fixes only |
| 2.0.x and earlier | No |

## Reporting a Vulnerability

We take security seriously. If you discover a vulnerability in Ad Superpowers, please report it responsibly.

### How to Report

**Email:** [contact@adsuperpowers.ai](mailto:contact@adsuperpowers.ai)

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

**Do not** open a public GitHub issue for security vulnerabilities.

### What to Expect

- **Acknowledgment:** Within 48 hours of your report
- **Status update:** Within 5 business days
- **Resolution target:** Critical issues within 14 days, others within 30 days

### Scope

The following are in scope:
- The MCP server at `mcp.adsuperpowers.ai`
- OAuth flows and token handling
- API key authentication
- Data access controls between tenants
- Plugin code in this repository

The following are **out of scope**:
- Third-party ad platform APIs (Meta, Google, LinkedIn, TikTok)
- Denial of service attacks
- Social engineering

### Credentials and data handling

The plugin itself ships no credentials. It contains skills, commands, agents and a
pointer to the remote MCP server at `https://mcp.adsuperpowers.ai/v1` over HTTPS.
Ad platform access is granted per user through OAuth in the Ad Superpowers dashboard,
or through an API key the user issues themselves. Tokens stay server side, encrypted
at rest, and are never written into plugin files or into the repository.

If you believe a credential has leaked into a published release, treat it as a
vulnerability and report it by email rather than opening an issue.

### Safe Harbor

We will not pursue legal action against researchers who:
- Act in good faith and follow this policy
- Avoid accessing or modifying other users' data
- Do not disclose vulnerabilities publicly before we've had reasonable time to address them
- Do not degrade the service for other users

We appreciate your help keeping Ad Superpowers and its users safe.
