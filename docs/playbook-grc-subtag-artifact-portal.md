# GRC Playbook: `artifact-portal`

**Category**: Governance

## Requirements tagged with this subtag:

| req_id | title |
|--------|-------|
| 1.1.2 | Roles and responsibilities for performing activities in Requirement 1 are documented, assigned, and understood. |
| 1.2.7 | Configurations of NSCs are reviewed at least once every six months to confirm they are relevant and effective. |
| 2.1.2 | Roles and responsibilities for performing activities in Requirement 2 are documented, assigned, and understood. |
| 2.3.2 | For wireless environments connected to the CDE or transmitting account data, wireless encryption keys are changed as follows:

-  Whenever personnel with knowledge of the key leave the company or the role for which the knowledge was necessary. • Whenever a key is suspected of or known to be compromised. |
| 3.1.2 | Roles and responsibilities for performing activities in Requirement 3 are documented, assigned, and understood. |
| 3.7.5 | Key management policies procedures are implemented to include the retirement, replacement, or destruction of keys used to protect stored account data, as deemed necessary when:

-  The key has reached the end of its defined cryptoperiod. • The integrity of the key has been weakened, including when personnel with knowledge of a cleartext key component leaves the company, or the role for which the key component was known. • The key is suspected of or known to be compromised. • Retired or replaced keys are not used for encryption operations. |
| 4.1.2 | Roles and responsibilities for performing activities in Requirement 4 are documented, assigned, and understood. |
| 5.1.2 | Roles and responsibilities for performing activities in Requirement 5 are documented, assigned, and understood. |
| 6.1.2 | Roles and responsibilities for performing activities in Requirement 6 are documented, assigned, and understood. |
| 6.2.3 | Bespoke and custom software is reviewed prior to being released into production or to customers, to identify and correct potential coding vulnerabilities, as follows:

-  Code reviews ensure code is developed according to secure coding guidelines. • Code reviews look for both existing and emerging software vulnerabilities. • Appropriate corrections are implemented prior to release. |
| 6.2.3.1 | If manual code reviews are performed for bespoke and custom software prior to release to production, code changes are:

-  Reviewed by individuals other than the originating code author, and who are knowledgeable about code-review techniques and secure coding practices. • Reviewed and approved by management prior to release. |
| 6.4.1 | For public-facing web applications, new threats and vulnerabilities are addressed on an ongoing basis and these applications are protected against known attacks as follows:

-  Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods as follows:

-  At least once every 12 months and after significant changes. - By an entity that specializes in application security. - Including, at a minimum, all common software attacks in Requirement 6.2.4. - All vulnerabilities are ranked in accordance with requirement 6.3.1. - All vulnerabilities are corrected. - The application is re-evaluated after the corrections OR • Installing an automated technical solution(s) that continually detects and prevents web-based attacks as follows:

-  Installed in front of public-facing web applications to detect and prevent web-based attacks. - Actively running and up to date as applicable. - Generating audit logs. - Configured to either block web-based attacks or generate an alert that is immediately investigated. Note: This requirement will be superseded by Requirement 6.4.2 after 31 March 2025 when Requirement 6.4.2 becomes effective. |
| 6.5.4 | Roles and functions are separated between production and pre-production environments to provide accountability such that only reviewed and approved changes are deployed. |
| 7.1.2 | Roles and responsibilities for performing activities in Requirement 7 are documented, assigned, and understood. |
| 7.2.4 | All user accounts and related access privileges, including third-party/vendor accounts, are reviewed as follows:

-  At least once every six months. • To ensure user accounts and access remain appropriate based on job function. • Any inappropriate access is addressed. • Management acknowledges that access remains appropriate. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 7.2.5.1 | All access by application and system accounts and related access privileges are reviewed as follows:

-  Periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1). • The application/system access remains appropriate for the function being performed. • Any inappropriate access is addressed. • Management acknowledges that access remains appropriate. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 7.2.6 | All user access to query repositories of stored cardholder data is restricted as follows:

-  Via applications or other programmatic methods, with access and allowed actions based on user roles and least privileges. • Only the responsible administrator(s) can directly access or query repositories of stored CHD. |
| 8.1.2 | Roles and responsibilities for performing activities in Requirement 8 are documented, assigned, and understood. |
| 9.1.2 | Roles and responsibilities for performing activities in Requirement 9 are documented, assigned, and understood. |
| 9.2.1.1 | Individual physical access to sensitive areas within the CDE is monitored with either video cameras or physical access control mechanisms (or both) as follows:

-  Entry and exit points to/from sensitive areas within the CDE are monitored. • Monitoring devices or mechanisms are protected from tampering or disabling. • Collected data is reviewed and correlated with other entries. • Collected data is stored for at least three months, unless otherwise restricted by law. |
| 9.4.1.2 | The security of the offline media backup location(s) with cardholder data is reviewed at least once every 12 months. |
| 9.5.1 | POI devices that capture payment card data via direct physical interaction with the payment card form factor are protected from tampering and unauthorized substitution, including the following:

-  Maintaining a list of POI devices. • Periodically inspecting POI devices to look for tampering or unauthorized substitution. • Training personnel to be aware of suspicious behavior and to report tampering or unauthorized substitution of devices. |
| 9.5.1.3 | Training is provided for personnel in POI environments to be aware of attempted tampering or replacement of POI devices, and includes:

-  Verifying the identity of any third-party persons claiming to be repair or maintenance personnel, before granting them access to modify or troubleshoot devices. • Procedures to ensure devices are not installed, replaced, or returned without verification. • Being aware of suspicious behavior around devices. • Reporting suspicious behavior and indications of device tampering or substitution to appropriate personnel. |
| 10.1.2 | Roles and responsibilities for performing activities in Requirement 10 are documented, assigned, and understood. |
| 10.4.1 | The following audit logs are reviewed at least once daily:

-  All security events. • Logs of all system components that store, process, or transmit CHD and/or SAD. • Logs of all critical system components. • Logs of all servers and system components that perform security functions (for example, network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), authentication servers). |
| 10.4.1.1 | Automated mechanisms are used to perform audit log reviews. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 10.4.2 | Logs of all other system components (those not specified in Requirement 10.4.1) are reviewed periodically. |
| 10.4.2.1 | The frequency of periodic log reviews for all other system components (not defined in Requirement 10.4.1) is defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1 Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 10.4.3 | Exceptions and anomalies identified during the review process are addressed. |
| 10.6.3 | Time synchronization settings and data are protected as follows:

-  Access to time data is restricted to only personnel with a business need. • Any changes to time settings on critical systems are logged, monitored, and reviewed. |
| 10.7.2 | Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:

-  Network security controls. • IDS/IPS. • Change-detection mechanisms. • Anti-malware solutions. • Physical access controls. • Logical access controls. • Audit logging mechanisms. • Segmentation controls (if used). • Audit log review mechanisms. • Automated security testing tools (if used). Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment and will supersede Requirement 10.7.1. |
| 11.1.2 | Roles and responsibilities for performing activities in Requirement 11 are documented, assigned, and understood. |
| 11.4.1 | A penetration testing methodology is defined, documented, and implemented by the entity and includes:

-  Industry-accepted penetration testing approaches. • Coverage for the entire CDE perimeter and critical systems. • Testing from both inside and outside the network. • Testing to validate any segmentation and scope-reduction controls. • Application-layer penetration testing to identify, at a minimum, the vulnerabilities listed in Requirement 6.2.4. • Network-layer penetration tests that encompass all components that support network functions as well as operating systems. • Review and consideration of threats and vulnerabilities experienced in the last 12 months. • Documented approach to assessing and addressing the risk posed by exploitable vulnerabilities and security weaknesses found during penetration testing. • Retention of penetration testing results and remediation activities results for at least 12 months. |
| 12.1.2 | The information security policy is:

-  Reviewed at least once every 12 months. • Updated as needed to reflect changes to business objectives or risks to the environment. |
| 12.1.3 | The security policy clearly defines information security roles and responsibilities for all personnel, and all personnel are aware of and acknowledge their information security responsibilities. |
| 12.3.1 | For each PCI DSS requirement that specifies completion of a targeted risk analysis, the analysis is documented and includes:

-  Identification of the assets being protected. • Identification of the threat(s) that the requirement is protecting against. • Identification of factors that contribute to the likelihood and/or impact of a threat being realized. • Resulting analysis that determines, and includes justification for, how the frequency or processes defined by the entity to meet the requirement minimize the likelihood and/or impact of the threat being realized. • Review of each targeted risk analysis at least once every 12 months to determine whether the results are still valid or if an updated risk analysis is needed. • Performance of updated risk analyses when needed, as determined by the annual review. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.3.3 | Cryptographic cipher suites and protocols in use are documented and reviewed at least once every 12 months, including at least the following:

-  An up-to-date inventory of all cryptographic cipher suites and protocols in use, including purpose and where used. • Active monitoring of industry trends regarding continued viability of all cryptographic cipher suites and protocols in use. • Documentation of a plan to respond to anticipated changes in cryptographic vulnerabilities. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.3.4 | Hardware and software technologies in use are reviewed at least once every 12 months, including at least the following:

-  Analysis that the technologies continue to receive security fixes from vendors promptly. • Analysis that the technologies continue to support (and do not preclude) the entity’s PCI DSS compliance. • Documentation of any industry announcements or trends related to a technology, such as when a vendor has announced “end of life” plans for a technology. • Documentation of a plan, approved by senior management, to remediate outdated technologies, including those for which vendors have announced “end of life” plans. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.4.2 | Additional requirement for service providers only: Reviews are performed at least once every three months to confirm that personnel are performing their tasks in accordance with all security policies and operational procedures. Reviews are performed by personnel other than those responsible for performing the given task and include, but are not limited to, the following tasks:

-  Daily log reviews. • Configuration reviews for network security controls. • Applying configuration standards to new systems. • Responding to security alerts. • Change-management processes. |
| 12.4.2.1 | Additional requirement for service providers only: Reviews conducted in accordance with Requirement 12.4.2 are documented to include:

-  Results of the reviews. • Documented remediation actions taken for any tasks that were found to not be performed at Requirement 12.4.2. • Review and sign-off of results by personnel assigned responsibility for the PCI DSS compliance program. |
| 12.5.3 | Additional requirement for service providers only: Significant changes to organizational structure result in a documented (internal) review of the impact to PCI DSS scope and applicability of controls, with results communicated to executive management. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.6.1 | A formal security awareness program is implemented to make all personnel aware of the entity’s information security policy and procedures, and their role in protecting the cardholder data. |
| 12.6.2 | The security awareness program is:

-  Reviewed at least once every 12 months, and • Updated as needed to address any new threats and vulnerabilities that may impact the security of the entity's cardholder data and/or sensitive authentication data, or the information provided to personnel about their role in protecting cardholder data. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.6.3 | Personnel receive security awareness training as follows:

-  Upon hire and at least once every 12 months. • Multiple methods of communication are used. • Personnel acknowledge at least once every 12 months that they have read and understood the information security policy and procedures. |
| 12.6.3.1 | Security awareness training includes awareness of threats and vulnerabilities that could impact the security of cardholder data and/or sensitive authentication data, including but not limited to:

-  Phishing and related attacks. • Social engineering. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.6.3.2 | Security awareness training includes awareness about the acceptable use of end-user technologies in accordance with Requirement 12.2.1. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| 12.10.1 | An incident response plan exists and is ready to be activated in the event of a suspected or confirmed security incident. The plan includes, but is not limited to:

-  Roles, responsibilities, and communication and contact strategies in the event of a suspected or confirmed security incident, including notification of payment brands and acquirers, at a minimum. • Incident response procedures with specific containment and mitigation activities for different types of incidents. • Business recovery and continuity procedures. • Data backup processes. • Analysis of legal requirements for reporting compromises. • Coverage and responses of all critical system components. • Reference or inclusion of incident response procedures from the payment brands. |
| 12.10.2 | At least once every 12 months, the security incident response plan is:

-  Reviewed and the content is updated as needed. • Tested, including all elements listed in Requirement 12.10.1. |
| 12.10.4.1 | The frequency of periodic training for incident response personnel is defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. |
| A1.2.1 | Audit log capability is enabled for each customer's environment that is consistent with PCI DSS Requirement 10, including:

-  Logs are enabled for common third-party applications. • Logs are active by default. • Logs are available for review only by the owning customer. • Log locations are clearly communicated to the owning customer. • Log data and availability is consistent with PCI DSS Requirement 10. |
| A3.4.1 | The organization reviews control failures and implements timely remediation |
