# PCI DSS GRC Subtag Handbook

This document includes all subtag insights and playbook references.

## 1.1.1 — All security policies and operational procedures that are identified in Requirement 1 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 1.1.2 — Roles and responsibilities for performing activities in Requirement 1 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 1.2.7 — Configurations of NSCs are reviewed at least once every six months to confirm they are relevant and effective.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 1.5.1 — Security controls are implemented on any computing devices, including company- and employee-owned devices, that connect to both untrusted networks (including the Internet) and the CDE as follows:

-  Specific configuration settings are defined to prevent threats being introduced into the entity’s network. • Security controls are actively running. • Security controls are not alterable by users of the computing devices unless specifically documented and authorized by management on a case-by-case basis for a limited period.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 2.1.1 — All security policies and operational procedures that are identified in Requirement 2 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 2.1.2 — Roles and responsibilities for performing activities in Requirement 2 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 2.2.5 — If any insecure services, protocols, or daemons are present:

-  Business justification is documented. • Additional security features are documented and implemented that reduce the risk of using insecure services, protocols, or daemons.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 2.3.2 — For wireless environments connected to the CDE or transmitting account data, wireless encryption keys are changed as follows:

-  Whenever personnel with knowledge of the key leave the company or the role for which the knowledge was necessary. • Whenever a key is suspected of or known to be compromised.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.1.1 — All security policies and operational procedures that are identified in Requirement 3 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.1.2 — Roles and responsibilities for performing activities in Requirement 3 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.2.1 — Account data storage is kept to a minimum through implementation of data retention and disposal policies, procedures, and processes that include at least the following:

-  Coverage for all locations of stored account data. • Coverage for any sensitive authentication data (SAD) stored prior to completion of authorization. This bullet is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.2.1 and must be fully considered during a PCI DSS assessment. • Limiting data storage amount and retention time to that which is required for legal or regulatory, and/or business requirements. • Specific retention requirements for stored account data that defines length of retention period and includes a documented business justification. • Processes for secure deletion or rendering account data unrecoverable when no longer needed per the retention policy. • A process for verifying, at least once every three months, that stored account data exceeding the defined retention period has been securely deleted or rendered unrecoverable.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.4.2 — When using remote-access technologies, technical controls prevent copy and/or relocation of PAN for all personnel, except for those with documented, explicit authorization and a legitimate, defined business need. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.5.1 — PAN is rendered unreadable anywhere it is stored by using any of the following approaches:

-  One-way hashes based on strong cryptography of the entire PAN. • Truncation (hashing cannot be used to replace the truncated segment of PAN). - If hashed and truncated versions of the same PAN, or different truncation formats of the same PAN, are present in an environment, additional controls are in place such that the different versions cannot be correlated to reconstruct the original PAN. • Index tokens. • Strong cryptography with associated key-management processes and procedures.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.5.1.1 — Hashes used to render PAN unreadable (per the first bullet of Requirement 3.5.1) are keyed cryptographic hashes of the entire PAN, with associated key-management processes and procedures in accordance with Requirements 3.6 and 3.7. Note: This requirement is considered a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.5.1.3 — If disk-level or partition-level encryption is used (rather than file-, column-, or field--level database encryption) to render PAN unreadable, it is managed as follows:

-  Logical access is managed separately and independently of native operating system authentication and access control mechanisms. • Decryption keys are not associated with user accounts. • Authentication factors (passwords, passphrases, or cryptographic keys) that allow access to unencrypted data are stored securely.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.6.1 — Procedures are defined and implemented to protect cryptographic keys used to protect stored account data against disclosure and misuse that include:

-  Access to keys is restricted to the fewest number of custodians necessary. • Key-encrypting keys are at least as strong as the data-encrypting keys they protect. • Key-encrypting keys are stored separately from data-encrypting keys. • Keys are stored securely in the fewest possible locations and forms.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.6.1.1 — Additional requirement for service providers only: A documented description of the cryptographic architecture is maintained that includes:

-  Details of all algorithms, protocols, and keys used for the protection of stored account data, including key strength and expiry date. • Preventing the use of the same cryptographic keys in production and test environments. This bullet is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.6.1 and must be fully considered during a PCI DSS assessment. • Description of the key usage for each key. • Inventory of any hardware security modules (HSMs), key management systems (KMS), and other secure cryptographic devices (SCDs) used for key management, including type and location of devices, to support meeting Requirement 12.3.4.
**Subtags:** annotated-policy, audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.1 — Key-management policies and procedures are implemented to include generation of strong cryptographic keys used to protect stored account data.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.2 — Key-management policies and procedures are implemented to include secure distribution of cryptographic keys used to protect stored account data.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.3 — Key-management policies and procedures are implemented to include secure storage of cryptographic keys used to protect stored account data.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.4 — Key management policies and procedures are implemented for cryptographic key changes for keys that have reached the end of their cryptoperiod, as defined by the associated application vendor or key owner, and based on industry best practices and guidelines, including the following:

-  A defined cryptoperiod for each key type in use. • A process for key changes at the end of the defined cryptoperiod.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.5 — Key management policies procedures are implemented to include the retirement, replacement, or destruction of keys used to protect stored account data, as deemed necessary when:

-  The key has reached the end of its defined cryptoperiod. • The integrity of the key has been weakened, including when personnel with knowledge of a cleartext key component leaves the company, or the role for which the key component was known. • The key is suspected of or known to be compromised. • Retired or replaced keys are not used for encryption operations.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.6 — Where manual cleartext cryptographic key-management operations are performed by personnel, key-management policies and procedures are implemented, including managing these operations using split knowledge and dual control.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.7 — Key management policies and procedures are implemented to include the prevention of unauthorized substitution of cryptographic keys.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.8 — Key management policies and procedures are implemented to include that cryptographic key custodians formally acknowledge (in writing or electronically) that they understand and accept their key-custodian responsibilities.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 3.7.9 — Additional requirement for service providers only: Where a service provider shares cryptographic keys with its customers for transmission or storage of account data, guidance on secure transmission, storage and updating of such keys is documented and distributed to the service provider’s customers.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 4.1.1 — All security policies and operational procedures that are identified in Requirement 4 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 4.1.2 — Roles and responsibilities for performing activities in Requirement 4 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 4.2.1 — Strong cryptography and security protocols are implemented as follows to safeguard PAN during transmission over open, public networks:

-  Only trusted keys and certificates are accepted. • Certificates used to safeguard PAN during transmission over open, public networks are confirmed as valid and are not expired or revoked. This bullet is a best practice until 31 March 2025, after which it will be required as part of Requirement 4.2.1 and must be fully considered during a PCI DSS assessment. • The protocol in use supports only secure versions or configurations and does not support fallback to, or use of insecure versions, algorithms, key sizes, or implementations. • The encryption strength is appropriate for the encryption methodology in use.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 4.2.2 — PAN is secured with strong cryptography whenever it is sent via end-user messaging technologies.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.1.1 — All security policies and operational procedures that are identified in Requirement 5 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.1.2 — Roles and responsibilities for performing activities in Requirement 5 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.2.3 — Any system components that are not at risk for malware are evaluated periodically to include the following:

-  A documented list of all system components not at risk for malware. • Identification and evaluation of evolving malware threats for those system components. • Confirmation whether such system components continue to not require anti-malware protection.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.3.3 — For removable electronic media, the anti-malware solution(s):

-  Performs automatic scans of when the media is inserted, connected, or logically mounted, OR • Performs continuous behavioral analysis of systems or processes when the media is inserted, connected, or logically mounted. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.3.4 — Audit logs for the anti-malware solution(s) are enabled and retained in accordance with Requirement 10.5.1.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 5.3.5 — Anti-malware mechanisms cannot be disabled or altered by users, unless specifically documented, and authorized by management on a case-by-case basis for a limited time period.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.1.1 — All security policies and operational procedures that are identified in Requirement 6 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.1.2 — Roles and responsibilities for performing activities in Requirement 6 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.2.1 — Bespoke and custom software are developed securely, as follows:

-  Based on industry standards and/or best practices for secure development. • In accordance with PCI DSS (for example, secure authentication and logging). • Incorporating consideration of information security issues during each stage of the software development lifecycle.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.2.2 — Software development personnel working on bespoke and custom software are trained at least once every 12 months as follows:

-  On software security relevant to their job function and development languages. • Including secure software design and secure coding techniques. • Including, if security testing tools are used, how to use the tools for detecting vulnerabilities in software.
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.2.3 — Bespoke and custom software is reviewed prior to being released into production or to customers, to identify and correct potential coding vulnerabilities, as follows:

-  Code reviews ensure code is developed according to secure coding guidelines. • Code reviews look for both existing and emerging software vulnerabilities. • Appropriate corrections are implemented prior to release.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.2.3.1 — If manual code reviews are performed for bespoke and custom software prior to release to production, code changes are:

-  Reviewed by individuals other than the originating code author, and who are knowledgeable about code-review techniques and secure coding practices. • Reviewed and approved by management prior to release.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.2.4 — Software engineering techniques or other methods are defined and in use by software development personnel to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software, including but not limited to the following:

-  Injection attacks, including SQL, LDAP, XPath, or other command, parameter, object, fault, or injection-type flaws. • Attacks on data and data structures, including attempts to manipulate buffers, pointers, input data, or shared data. • Attacks on cryptography usage, including attempts to exploit weak, insecure, or inappropriate cryptographic implementations, algorithms, cipher suites, or modes of operation. • Attacks on business logic, including attempts to abuse or bypass application features and functionalities through the manipulation of APIs, communication protocols and channels, client-side functionality, or other system/application functions and resources. This includes cross-site scripting (XSS) and cross-site request forgery (CSRF). • Attacks on access control mechanisms, including attempts to bypass or abuse identification, authentication, or authorization mechanisms, or attempts to exploit weaknesses in the implementation of such mechanisms. • Attacks via any "high-risk" vulnerabilities identified in the vulnerability identification process, as defined in Requirement 6.3.1.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.3.1 — Security vulnerabilities are identified and managed as follows:

-  New security vulnerabilities are identified using industry-recognized sources for security vulnerability information, including alerts from international and national computer emergency response teams (CERTs). • Vulnerabilities are assigned a risk ranking based on industry best practices and consideration of potential impact. • Risk rankings identify, at a minimum, all vulnerabilities considered to be a high-risk or critical to the environment. • Vulnerabilities for bespoke and custom, and third-party software (for example operating systems and databases) are covered.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.4.1 — For public-facing web applications, new threats and vulnerabilities are addressed on an ongoing basis and these applications are protected against known attacks as follows:

-  Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods as follows:

-  At least once every 12 months and after significant changes. - By an entity that specializes in application security. - Including, at a minimum, all common software attacks in Requirement 6.2.4. - All vulnerabilities are ranked in accordance with requirement 6.3.1. - All vulnerabilities are corrected. - The application is re-evaluated after the corrections OR • Installing an automated technical solution(s) that continually detects and prevents web-based attacks as follows:

-  Installed in front of public-facing web applications to detect and prevent web-based attacks. - Actively running and up to date as applicable. - Generating audit logs. - Configured to either block web-based attacks or generate an alert that is immediately investigated. Note: This requirement will be superseded by Requirement 6.4.2 after 31 March 2025 when Requirement 6.4.2 becomes effective.
**Subtags:** artifact-portal, audit-friction-alert, click-to-breach-visual, milestone-map, roc-swipefile, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.4.2 — For public-facing web applications, an automated technical solution is deployed that continually detects and prevents web-based attacks, with at least the following:

-  Is installed in front of public-facing web applications and is configured to detect and prevent web-based attacks. • Actively running and up to date as applicable. • Generating audit logs. • Configured to either block web-based attacks or generate an alert that is immediately investigated. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. This new requirement will replace Requirement 6.4.1 once its effective date is reached.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.5.1 — Changes to all system components in the production environment are made according to established procedures that include:

-  Reason for, and description of, the change. • Documentation of security impact. • Documented change approval by authorized parties. • Testing to verify that the change does not adversely impact system security. • For bespoke and custom software changes, all updates are tested for compliance with Requirement 6.2.4 before being deployed into production. • Procedures to address failures and return to a secure state.
**Subtags:** annotated-policy, audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.5.2 — Upon completion of a significant change, all applicable PCI DSS requirements are confirmed to be in place on all new or changed systems and networks, and documentation is updated as applicable.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.5.4 — Roles and functions are separated between production and pre-production environments to provide accountability such that only reviewed and approved changes are deployed.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 6.5.6 — Test data and test accounts are removed from system components before the system goes into production.
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 1.5 — Ensure security policies and operational procedures for managing firewalls are documented, in use, and known
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 7.1.1 — All security policies and operational procedures that are identified in Requirement 7 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 7.1.2 — Roles and responsibilities for performing activities in Requirement 7 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 7.2.4 — All user accounts and related access privileges, including third-party/vendor accounts, are reviewed as follows:

-  At least once every six months. • To ensure user accounts and access remain appropriate based on job function. • Any inappropriate access is addressed. • Management acknowledges that access remains appropriate. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 7.2.5.1 — All access by application and system accounts and related access privileges are reviewed as follows:

-  Periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1). • The application/system access remains appropriate for the function being performed. • Any inappropriate access is addressed. • Management acknowledges that access remains appropriate. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 7.2.6 — All user access to query repositories of stored cardholder data is restricted as follows:

-  Via applications or other programmatic methods, with access and allowed actions based on user roles and least privileges. • Only the responsible administrator(s) can directly access or query repositories of stored CHD.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.1.1 — All security policies and operational procedures that are identified in Requirement 8 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.1.2 — Roles and responsibilities for performing activities in Requirement 8 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.2.2 — Group, shared, or generic IDs, or other shared authentication credentials are only used when necessary on an exception basis, and are managed as follows:

-  ID use is prevented unless needed for an exceptional circumstance. • Use is limited to the time needed for the exceptional circumstance. • Business justification for use is documented. • Use is explicitly approved by management. • Individual user identity is confirmed before access to an account is granted. • Every action taken is attributable to an individual user.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.2.4 — Addition, deletion, and modification of user IDs, authentication factors, and other identifier objects are managed as follows:

-  Authorized with the appropriate approval. • Implemented with only the privileges specified on the documented approval.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.3.8 — Authentication policies and procedures are documented and communicated to all users including:

-  Guidance on selecting strong authentication factors. • Guidance for how users should protect their authentication factors. • Instructions not to reuse previously used passwords/passphrases. • Instructions to change passwords/passphrases if there is any suspicion or knowledge that the password/passphrases have been compromised and how to report the incident.
**Subtags:** annotated-policy, breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.3.11 — Where authentication factors such as physical or logical security tokens, smart cards, or certificates are used:

-  Factors are assigned to an individual user and not shared among multiple users. • Physical and/or logical controls ensure only the intended user can use that factor to gain access.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.5.1 — MFA systems are implemented as follows:

-  The MFA system is not susceptible to replay attacks. • MFA systems cannot be bypassed by any users, including administrative users unless specifically documented, and authorized by management on an exception basis, for a limited time period. • At least two different types of authentication factors are used. • Success of all authentication factors is required before access is granted. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.6.1 — If accounts used by systems or applications can be used for interactive login, they are managed as follows:

-  Interactive use is prevented unless needed for an exceptional circumstance. • Interactive use is limited to the time needed for the exceptional circumstance. • Business justification for interactive use is documented. • Interactive use is explicitly approved by management. • Individual user identity is confirmed before access to account is granted. • Every action taken is attributable to an individual user. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.6.2 — Passwords/passphrases for any application and system accounts that can be used for interactive login are not hard coded in scripts, configuration/property files, or bespoke and custom source code. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.1.1 — All security policies and operational procedures that are identified in Requirement 9 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.1.2 — Roles and responsibilities for performing activities in Requirement 9 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.2.1.1 — Individual physical access to sensitive areas within the CDE is monitored with either video cameras or physical access control mechanisms (or both) as follows:

-  Entry and exit points to/from sensitive areas within the CDE are monitored. • Monitoring devices or mechanisms are protected from tampering or disabling. • Collected data is reviewed and correlated with other entries. • Collected data is stored for at least three months, unless otherwise restricted by law.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.2.2 — Physical and/or logical controls are implemented to restrict use of publicly accessible network jacks within the facility.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.3.1 — Procedures are implemented for authorizing and managing physical access of personnel to the CDE, including:

-  Identifying personnel. • Managing changes to an individual's physical access requirements. • Revoking or terminating personnel identification. • Limiting access to the identification process or system to authorized personnel.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.3.2 — Procedures are implemented for authorizing and managing visitor access to the CDE, including:

-  Visitors are authorized before entering. • Visitors are escorted at all times. • Visitors are clearly identified and given a badge or other identification that expires. • Visitor badges or other identification visibly distinguishes visitors from personnel.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.3.4 — Visitor logs are used to maintain a physical record of visitor activity both within the facility and within sensitive areas, including:

-  The visitor’s name and the organization represented. • The date and time of the visit. • The name of the personnel authorizing physical access. • Retaining the log for at least three months, unless otherwise restricted by law.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.4.1.2 — The security of the offline media backup location(s) with cardholder data is reviewed at least once every 12 months.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.4.3 — Media with cardholder data sent outside the facility is secured as follows:

-  Media sent outside the facility is logged. • Media is sent by secured courier or other delivery method that can be accurately tracked. • Offsite tracking logs include details about media location.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.4.5 — Inventory logs of all electronic media with cardholder data are maintained.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.5.1 — POI devices that capture payment card data via direct physical interaction with the payment card form factor are protected from tampering and unauthorized substitution, including the following:

-  Maintaining a list of POI devices. • Periodically inspecting POI devices to look for tampering or unauthorized substitution. • Training personnel to be aware of suspicious behavior and to report tampering or unauthorized substitution of devices.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.5.1.3 — Training is provided for personnel in POI environments to be aware of attempted tampering or replacement of POI devices, and includes:

-  Verifying the identity of any third-party persons claiming to be repair or maintenance personnel, before granting them access to modify or troubleshoot devices. • Procedures to ensure devices are not installed, replaced, or returned without verification. • Being aware of suspicious behavior around devices. • Reporting suspicious behavior and indications of device tampering or substitution to appropriate personnel.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.1.1 — All security policies and operational procedures that are identified in Requirement 10 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.1.2 — Roles and responsibilities for performing activities in Requirement 10 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1 — Audit logs are enabled and active for all system components and cardholder data.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.1 — Audit logs capture all individual user access to cardholder data.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.2 — Audit logs capture all actions taken by any individual with administrative access, including any interactive use of application or system accounts.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.3 — Audit logs capture all access to audit logs.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.4 — Audit logs capture all invalid logical access attempts.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.5 — Audit logs capture all changes to identification and authentication credentials including, but not limited to:

-  Creation of new accounts. • Elevation of privileges. • All changes, additions, or deletions to accounts with administrative access.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.6 — Audit logs capture the following:

-  All initialization of new audit logs, and • All starting, stopping, or pausing of the existing audit logs.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.1.7 — Audit logs capture all creation and deletion of system-level objects.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2.2 — Audit logs record the following details for each auditable event:

-  User identification. • Type of event. • Date and time. • Success and failure indication. • Origination of event. • Identity or name of affected data, system component, resource, or service (for example, name and protocol).
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.3.1 — Read access to audit logs files is limited to those with a job-related need.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.3.2 — Audit log files are protected to prevent modifications by individuals.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.3.3 — Audit log files, including those for external-facing technologies, are promptly backed up to a secure, central, internal log server(s) or other media that is difficult to modify.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.3.4 — File integrity monitoring or change-detection mechanisms is used on audit logs to ensure that existing log data cannot be changed without generating alerts.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.4.1 — The following audit logs are reviewed at least once daily:

-  All security events. • Logs of all system components that store, process, or transmit CHD and/or SAD. • Logs of all critical system components. • Logs of all servers and system components that perform security functions (for example, network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), authentication servers).
**Subtags:** artifact-portal, audit-friction-alert, click-to-breach-visual, milestone-map, roc-swipefile, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.4.1.1 — Automated mechanisms are used to perform audit log reviews. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** artifact-portal, audit-friction-alert, click-to-breach-visual, milestone-map, roc-swipefile, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.4.2 — Logs of all other system components (those not specified in Requirement 10.4.1) are reviewed periodically.
**Subtags:** artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.4.2.1 — The frequency of periodic log reviews for all other system components (not defined in Requirement 10.4.1) is defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1 Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.4.3 — Exceptions and anomalies identified during the review process are addressed.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.5.1 — Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.6.1 — System clocks and time are synchronized using time-synchronization technology.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.6.3 — Time synchronization settings and data are protected as follows:

-  Access to time data is restricted to only personnel with a business need. • Any changes to time settings on critical systems are logged, monitored, and reviewed.
**Subtags:** artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.7.1 — Additional requirement for service providers only: Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:

-  Network security controls. • IDS/IPS. • FIM. • Anti-malware solutions. • Physical access controls. • Logical access controls. • Audit logging mechanisms. • Segmentation controls (if used). Note: This requirement will be superseded by Requirement 10.7.2 as of 31 March 2025.
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.7.2 — Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:

-  Network security controls. • IDS/IPS. • Change-detection mechanisms. • Anti-malware solutions. • Physical access controls. • Logical access controls. • Audit logging mechanisms. • Segmentation controls (if used). • Audit log review mechanisms. • Automated security testing tools (if used). Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment and will supersede Requirement 10.7.1.
**Subtags:** artifact-portal, audit-friction-alert, click-to-breach-visual, justification-library, milestone-map, roc-swipefile, scorecard, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.7.3 — Failures of any critical security control systems are responded to promptly, including but not limited to:

-  Restoring security functions. • Identifying and documenting the duration (date and time from start to end) of the security failure. • Identifying and documenting the cause(s) of failure and documenting required remediation. • Identifying and addressing any security issues that arose during the failure. • Determining whether further actions are required as a result of the security failure. • Implementing controls to prevent the cause of failure from reoccurring. • Resuming monitoring of security controls. Note: This is a current v3.2.1 requirement that applies to service providers only. However, this requirement is a best practice for all other entities until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.1.1 — All security policies and operational procedures that are identified in Requirement 11 are:

-  Documented. • Kept up to date. • In use. • Known to all affected parties.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.1.2 — Roles and responsibilities for performing activities in Requirement 11 are documented, assigned, and understood.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.2.1 — Authorized and unauthorized wireless access points are managed as follows:

-  The presence of wireless (Wi-Fi) access points is tested for, • All authorized and unauthorized wireless access points are detected and identified, • Testing, detection, and identification occurs at least once every three months. • If automated monitoring is used, personnel are notified via generated alerts.
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.2.2 — An inventory of authorized wireless access points is maintained, including a documented business justification.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.3.1 — Internal vulnerability scans are performed as follows:

-  At least once every three months. • Vulnerabilities that are either high-risk or critical (according to the entity's vulnerability risk rankings defined at Requirement 6.3.1) are resolved. • Rescans are performed that confirm all high-risk and critical vulnerabilities (as noted above) have been resolved. • Scan tool is kept up to date with latest vulnerability information. • Scans are performed by qualified personnel and organizational independence of the tester exists.
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.3.1.2 — Internal vulnerability scans are performed via authenticated scanning as follows:

-  Systems that are unable to accept credentials for authenticated scanning are documented. • Sufficient privileges are used for those systems that accept credentials for scanning. • If accounts used for authenticated scanning can be used for interactive login, they are managed in accordance with Requirement 8.2.2. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.3.1.3 — Internal vulnerability scans are performed after any significant change as follows:

-  Vulnerabilities that are either high-risk or critical (according to the entity's vulnerability risk rankings defined at Requirement 6.3.1) are resolved. • Rescans are conducted as needed. • Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV).
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.3.2.1 — External vulnerability scans are performed after any significant change as follows:

-  Vulnerabilities that are scored 4.0 or higher by the CVSS are resolved. • Rescans are conducted as needed. • Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV).
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.1 — A penetration testing methodology is defined, documented, and implemented by the entity and includes:

-  Industry-accepted penetration testing approaches. • Coverage for the entire CDE perimeter and critical systems. • Testing from both inside and outside the network. • Testing to validate any segmentation and scope-reduction controls. • Application-layer penetration testing to identify, at a minimum, the vulnerabilities listed in Requirement 6.2.4. • Network-layer penetration tests that encompass all components that support network functions as well as operating systems. • Review and consideration of threats and vulnerabilities experienced in the last 12 months. • Documented approach to assessing and addressing the risk posed by exploitable vulnerabilities and security weaknesses found during penetration testing. • Retention of penetration testing results and remediation activities results for at least 12 months.
**Subtags:** annotated-policy, artifact-portal, audit-friction-alert, click-to-breach-visual, justification-library, milestone-map, scorecard, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.2 — Internal penetration testing is performed:

-  Per the entity's defined methodology • At least once every 12 months • After any significant infrastructure or application upgrade or change • By a qualified internal resource or qualified external third-party • Organizational independence of the tester exists (not required to be a QSA or ASV)
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.3 — External penetration testing is performed:

-  Per the entity's defined methodology • At least once every 12 months • After any significant infrastructure or application upgrade or change • By a qualified internal resource or qualified external third party • Organizational independence of the tester exists (not required to be a QSA or ASV)
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.4 — Exploitable vulnerabilities and security weaknesses found during penetration testing are corrected as follows:

-  In accordance with the entity's assessment of the risk posed by the security issue as defined in Requirement 6.3.1. • Penetration testing is repeated to verify the corrections.
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.5 — If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:

-  At least once every 12 months and after any changes to segmentation controls/methods • Covering all segmentation controls/methods in use • According to the entity's defined penetration testing methodology • Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems • Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3) • Performed by a qualified internal resource or qualified external third party • Organizational independence of the tester exists (not required to be a QSA or ASV)
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.6 — Additional requirement for service providers only: If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:

-  At least once every six months and after any changes to segmentation controls/methods. • Covering all segmentation controls/methods in use. • According to the entity's defined penetration testing methodology. • Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems. • Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3). • Performed by a qualified internal resource or qualified external third party. • Organizational independence of the tester exists (not required to be a QSA or ASV).
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.4.7 — Additional requirement for multi-tenant service providers only: Multi-tenant service providers support their customers for external penetration testing per Requirement 11.4.3 and 11.4.4. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.5.1 — Intrusion-detection and/or intrusion-prevention techniques are used to detect and/or prevent intrusions into the network as follows:

-  All traffic is monitored at the perimeter of the CDE. • All traffic is monitored at critical points in the CDE. • Personnel are alerted to suspected compromises. • All intrusion-detection and prevention engines, baselines, and signatures are kept up to date.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.5.1.1 — Additional requirement for service providers only: Intrusion-detection and/or intrusion-prevention techniques detect, alert on/prevent, and address covert malware communication channels. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.5.2 — A change-detection mechanism (for example, file integrity monitoring tools) is deployed as follows:

-  To alert personnel to unauthorized modification (including changes, additions, and deletions) of critical files. • To perform critical file comparisons at least once weekly.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.6.1 — A change- and tamper-detection mechanism is deployed as follows:

-  To alert personnel to unauthorized modification (including indicators of compromise, changes, additions, and deletions) to the security-impacting HTTP headers and the script contents of payment pages as received by the consumer browser. • The mechanism is configured to evaluate the received HTTP headers and payment pages. • The mechanism functions are performed as follows:

-  At least once weekly OR - Periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1). Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.1.2 — The information security policy is:

-  Reviewed at least once every 12 months. • Updated as needed to reflect changes to business objectives or risks to the environment.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.1.3 — The security policy clearly defines information security roles and responsibilities for all personnel, and all personnel are aware of and acknowledge their information security responsibilities.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.2.1 — Acceptable use policies for end-user technologies are documented and implemented, including:

-  Explicit approval by authorized parties. • Acceptable uses of the technology. • List of products approved by the company for employee use, including hardware and software.
**Subtags:** annotated-policy, click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.3.1 — For each PCI DSS requirement that specifies completion of a targeted risk analysis, the analysis is documented and includes:

-  Identification of the assets being protected. • Identification of the threat(s) that the requirement is protecting against. • Identification of factors that contribute to the likelihood and/or impact of a threat being realized. • Resulting analysis that determines, and includes justification for, how the frequency or processes defined by the entity to meet the requirement minimize the likelihood and/or impact of the threat being realized. • Review of each targeted risk analysis at least once every 12 months to determine whether the results are still valid or if an updated risk analysis is needed. • Performance of updated risk analyses when needed, as determined by the annual review. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.3.2 — A targeted risk analysis is performed for each PCI DSS requirement that the entity meets with the customized approach, to include:

-  Documented evidence detailing each element specified in Appendix D: Customized Approach (including, at a minimum, a controls matrix and risk analysis). • Approval of documented evidence by senior management. • Performance of the targeted analysis of risk at least once every 12 months.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.3.3 — Cryptographic cipher suites and protocols in use are documented and reviewed at least once every 12 months, including at least the following:

-  An up-to-date inventory of all cryptographic cipher suites and protocols in use, including purpose and where used. • Active monitoring of industry trends regarding continued viability of all cryptographic cipher suites and protocols in use. • Documentation of a plan to respond to anticipated changes in cryptographic vulnerabilities. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.3.4 — Hardware and software technologies in use are reviewed at least once every 12 months, including at least the following:

-  Analysis that the technologies continue to receive security fixes from vendors promptly. • Analysis that the technologies continue to support (and do not preclude) the entity’s PCI DSS compliance. • Documentation of any industry announcements or trends related to a technology, such as when a vendor has announced “end of life” plans for a technology. • Documentation of a plan, approved by senior management, to remediate outdated technologies, including those for which vendors have announced “end of life” plans. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.4.2 — Additional requirement for service providers only: Reviews are performed at least once every three months to confirm that personnel are performing their tasks in accordance with all security policies and operational procedures. Reviews are performed by personnel other than those responsible for performing the given task and include, but are not limited to, the following tasks:

-  Daily log reviews. • Configuration reviews for network security controls. • Applying configuration standards to new systems. • Responding to security alerts. • Change-management processes.
**Subtags:** annotated-policy, artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.4.2.1 — Additional requirement for service providers only: Reviews conducted in accordance with Requirement 12.4.2 are documented to include:

-  Results of the reviews. • Documented remediation actions taken for any tasks that were found to not be performed at Requirement 12.4.2. • Review and sign-off of results by personnel assigned responsibility for the PCI DSS compliance program.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.5.2 — PCI DSS scope is documented and confirmed by the entity at least once every 12 months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes:

-  Identifying all data flows for the various payment stages (for example, authorization, capture settlement, chargebacks, and refunds) and acceptance channels (for example, card-present, card-not-present, and e-commerce). • Updating all data-flow diagrams per Requirement 1.2.4. • Identifying all locations where account data is stored, processed, and transmitted, including but not limited to:

1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups. • Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE. • Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope. • Identifying all connections from third-party entities with access to the CDE. • Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.5.2.1 — Additional requirement for service providers only: PCI DSS scope is documented and confirmed by the entity at least once every six months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes all the elements specified in Requirement 12.5.2. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.5.3 — Additional requirement for service providers only: Significant changes to organizational structure result in a documented (internal) review of the impact to PCI DSS scope and applicability of controls, with results communicated to executive management. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.6.1 — A formal security awareness program is implemented to make all personnel aware of the entity’s information security policy and procedures, and their role in protecting the cardholder data.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.6.2 — The security awareness program is:

-  Reviewed at least once every 12 months, and • Updated as needed to address any new threats and vulnerabilities that may impact the security of the entity's cardholder data and/or sensitive authentication data, or the information provided to personnel about their role in protecting cardholder data. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.6.3 — Personnel receive security awareness training as follows:

-  Upon hire and at least once every 12 months. • Multiple methods of communication are used. • Personnel acknowledge at least once every 12 months that they have read and understood the information security policy and procedures.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.6.3.1 — Security awareness training includes awareness of threats and vulnerabilities that could impact the security of cardholder data and/or sensitive authentication data, including but not limited to:

-  Phishing and related attacks. • Social engineering. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.6.3.2 — Security awareness training includes awareness about the acceptable use of end-user technologies in accordance with Requirement 12.2.1. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, click-to-breach-visual, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.1 — An incident response plan exists and is ready to be activated in the event of a suspected or confirmed security incident. The plan includes, but is not limited to:

-  Roles, responsibilities, and communication and contact strategies in the event of a suspected or confirmed security incident, including notification of payment brands and acquirers, at a minimum. • Incident response procedures with specific containment and mitigation activities for different types of incidents. • Business recovery and continuity procedures. • Data backup processes. • Analysis of legal requirements for reporting compromises. • Coverage and responses of all critical system components. • Reference or inclusion of incident response procedures from the payment brands.
**Subtags:** annotated-policy, artifact-portal, breach-simulation, milestone-map, scorecard, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.2 — At least once every 12 months, the security incident response plan is:

-  Reviewed and the content is updated as needed. • Tested, including all elements listed in Requirement 12.10.1.
**Subtags:** artifact-portal, audit-friction-alert, breach-simulation, justification-library, milestone-map, scorecard, self-healing-control, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.3 — Specific personnel are designated to be available on a 24/7 basis to respond to suspected or confirmed security incidents.
**Subtags:** breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.4 — Personnel responsible for responding to suspected and confirmed security incidents are appropriately and periodically trained on their incident response responsibilities.
**Subtags:** breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.4.1 — The frequency of periodic training for incident response personnel is defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, artifact-portal, breach-simulation, milestone-map, scorecard, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.5 — The security incident response plan includes monitoring and responding to alerts from security monitoring systems, including but not limited to:

-  Intrusion-detection and intrusion-prevention systems. • Network security controls. • Change-detection mechanisms for critical files. • The change-and tamper-detection mechanism for payment pages. This bullet is a best practice until 31 March 2025, after which it will be required as part of Requirement 12.10.5 and must be fully considered during a PCI DSS assessment. • Detection of unauthorized wireless access points.
**Subtags:** breach-simulation, click-to-breach-visual, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.6 — The security incident response plan is modified and evolved according to lessons learned and to incorporate industry developments.
**Subtags:** breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.10.7 — Incident response procedures are in place, to be initiated upon the detection of stored PAN anywhere it is not expected, and include:

-  Determining what to do if PAN is discovered outside the CDE, including its retrieval, secure deletion, and/or migration into the currently defined CDE, as applicable. • Identifying whether sensitive authentication data is stored with PAN. • Determining where the account data came from and how it ended up where it was not expected. • Remediating data leaks or process gaps that resulted in the account data being where it was not expected. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** annotated-policy, breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A1.1.1 — Logical separation is implemented as follows:

-  The provider cannot access its customers' environments without authorization. • Customers cannot access the provider's environment without authorization. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A1.1.4 — The effectiveness of logical separation controls used to separate customer environments is confirmed at least once every six months via penetration testing. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** audit-friction-alert, click-to-breach-visual, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A1.2.1 — Audit log capability is enabled for each customer's environment that is consistent with PCI DSS Requirement 10, including:

-  Logs are enabled for common third-party applications. • Logs are active by default. • Logs are available for review only by the owning customer. • Log locations are clearly communicated to the owning customer. • Log data and availability is consistent with PCI DSS Requirement 10.
**Subtags:** artifact-portal, audit-friction-alert, click-to-breach-visual, milestone-map, roc-swipefile, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A1.2.2 — Processes or mechanisms are implemented to support and/or facilitate prompt forensic investigations in the event of a suspected or confirmed security incident for any customer.
**Subtags:** breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A1.2.3 — Processes or mechanisms are implemented for reporting and addressing suspected or confirmed security incidents and vulnerabilities, including:

-  Customers can securely report security incidents and vulnerabilities to the provider. • The provider addresses and remediates suspected or confirmed security incidents and vulnerabilities according to Requirement 6.3.1. Note: This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Subtags:** breach-simulation, threat-feed-link

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 8.1 — Define and manage user identification and authentication policies and procedures
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 9.2 — Develop procedures to authorize and revoke access to physical areas with CDE systems
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.1 — Implement audit logs to track user activities and system events
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.2 — Automate audit trails for all system components
**Subtags:** audit-friction-alert, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 10.3 — Secure and protect audit logs to prevent unauthorized access
**Subtags:** audit-friction-alert, click-to-breach-visual, roc-swipefile

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.1 — Test for the presence of wireless access points and detect unauthorized wireless access points
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 11.3 — Perform internal and external penetration testing
**Subtags:** audit-friction-alert, justification-library, self-healing-control

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## 12.3 — Develop usage policies for critical technologies
**Subtags:** click-to-breach-visual

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A3.3.1 — Annual scope validation is performed and documented
**Subtags:** annotated-policy

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

## A3.4.1 — The organization reviews control failures and implements timely remediation
**Subtags:** artifact-portal, milestone-map, scorecard

- [ ] Review control intent
- [ ] Link to policy or artifact
- [ ] Owner: _(fill in)_

