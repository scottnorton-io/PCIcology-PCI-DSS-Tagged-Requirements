# GRC Playbook: `roc-swipefile`

**Category**: Compliance

## Requirements tagged with this subtag:

| req_id | title |
|--------|-------|
| 5.3.4 | Audit logs for the anti-malware solution(s) are enabled and retained in accordance with Requirement 10.5.1. |
| 6.4.1 | For public-facing web applications, new threats and vulnerabilities are addressed on an ongoing basis and these applications are protected against known attacks as follows:

-  Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods as follows:

-  At least once every 12 months and after significant changes. - By an entity that specializes in application security. - Including, at a minimum, all common software attacks in Requirement 6.2.4. - All vulnerabilities are ranked in accordance with requirement 6.3.1. - All vulnerabilities are corrected. - The application is re-evaluated after the corrections OR • Installing an automated technical solution(s) that continually detects and prevents web-based attacks as follows:

-  Installed in front of public-facing web applications to detect and prevent web-based attacks. - Actively running and up to date as applicable. - Generating audit logs. - Configured to either block web-based attacks or generate an alert that is immediately investigated. Note: This requirement will be superseded by Requirement 6.4.2 after 31 March 2025 when Requirement 6.4.2 becomes effective. |
| 6.4.2 | For public-facing web applications, an automated technical solution is deployed that continually detects and prevents web-based attacks, with at least the following:

-  Is installed in front of public-facing web applications and is configured to detect and prevent web-based attacks. • Actively running and up to date as applicable. • Generating audit logs. • Configured to either block web-based attacks or generate an alert that is immediately investigated. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. This new requirement will replace Requirement 6.4.1 once its effective date is reached. |
| 10.2.1 | Audit logs are enabled and active for all system components and cardholder data. |
| 10.2.1.1 | Audit logs capture all individual user access to cardholder data. |
| 10.2.1.2 | Audit logs capture all actions taken by any individual with administrative access, including any interactive use of application or system accounts. |
| 10.2.1.3 | Audit logs capture all access to audit logs. |
| 10.2.1.4 | Audit logs capture all invalid logical access attempts. |
| 10.2.1.5 | Audit logs capture all changes to identification and authentication credentials including, but not limited to:

-  Creation of new accounts. • Elevation of privileges. • All changes, additions, or deletions to accounts with administrative access. |
| 10.2.1.6 | Audit logs capture the following:

-  All initialization of new audit logs, and • All starting, stopping, or pausing of the existing audit logs. |
| 10.2.1.7 | Audit logs capture all creation and deletion of system-level objects. |
| 10.2.2 | Audit logs record the following details for each auditable event:

-  User identification. • Type of event. • Date and time. • Success and failure indication. • Origination of event. • Identity or name of affected data, system component, resource, or service (for example, name and protocol). |
| 10.3.1 | Read access to audit logs files is limited to those with a job-related need. |
| 10.3.2 | Audit log files are protected to prevent modifications by individuals. |
| 10.3.3 | Audit log files, including those for external-facing technologies, are promptly backed up to a secure, central, internal log server(s) or other media that is difficult to modify. |
| 10.3.4 | File integrity monitoring or change-detection mechanisms is used on audit logs to ensure that existing log data cannot be changed without generating alerts. |
| 10.4.1 | The following audit logs are reviewed at least once daily:

-  All security events. • Logs of all system components that store, process, or transmit CHD and/or SAD. • Logs of all critical system components. • Logs of all servers and system components that perform security functions (for example, network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), authentication servers). |
| 10.4.1.1 | Automated mechanisms are used to perform audit log reviews. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 10.5.1 | Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis. |
| 10.7.1 | Additional requirement for service providers only: Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:

-  Network security controls. • IDS/IPS. • FIM. • Anti-malware solutions. • Physical access controls. • Logical access controls. • Audit logging mechanisms. • Segmentation controls (if used). Note: This requirement will be superseded by Requirement 10.7.2 as of 31 March 2025. |
| 10.7.2 | Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:

-  Network security controls. • IDS/IPS. • Change-detection mechanisms. • Anti-malware solutions. • Physical access controls. • Logical access controls. • Audit logging mechanisms. • Segmentation controls (if used). • Audit log review mechanisms. • Automated security testing tools (if used). Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment and will supersede Requirement 10.7.1. |
| A1.2.1 | Audit log capability is enabled for each customer's environment that is consistent with PCI DSS Requirement 10, including:

-  Logs are enabled for common third-party applications. • Logs are active by default. • Logs are available for review only by the owning customer. • Log locations are clearly communicated to the owning customer. • Log data and availability is consistent with PCI DSS Requirement 10. |
| 10.1 | Implement audit logs to track user activities and system events |
| 10.2 | Automate audit trails for all system components |
| 10.3 | Secure and protect audit logs to prevent unauthorized access |
