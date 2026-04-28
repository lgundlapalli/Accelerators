
System Architectural Design and Configuration Item Inventory (CII)
By approving this document, you attest that you have completed training on BTSQC09.05 and agree with the System Architectural Design and, if applicable, the Configuration Item Inventory (CII) for this system.



When revising the document, add an additional row below the v1.0 line and complete the revision history information per document revision in a sequential manner.


# OVERVIEW
## Table of Contents
1.0	OVERVIEW	5
1.1	Table of Contents	5
1.2	Purpose	5
1.3	Acronyms and Definitions	6
1.4	References	6
1.5	Roles and Responsibilities	6
2.0	SYSTEM CONTEXT	7
3.0	PROCESS MODEL	7
4.0	SYSTEM ARCHITECTURE	7
4.1	System Architecture	7
4.2	Software Architecture	8
4.3	Application Architecture	9
4.4	Data Architecture	10
4.5	Interface Architecture	11
5.0	SECURITY	11
6.0	CONFIGURATION ITEM INVENTORY (CII)	13
6.1	Configuration Management	13
7.0	PERFORMANCE	13
8.0	RESILIENCY	14
8.1	Availability	14
8.2	Backups	14
8.3	Restore Testing	15
8.4	Disaster Recovery	15
9.0	APPENDICES	15
9.1	Appendix A CII Item Details	15
10.0	ATTACHMENTS	15
10.1	Attachment 1 CII Item Details	15
## Purpose
This document describes the system architecture and high-level  parameters intended to satisfy the system’s functional behaviors, which support the business needs for the <Computer System Name>, to support Abbott < division > deployment.
The primary purpose of this document is to:
Decompose the application into components / subsystems
Identify each component via the configuration item, as applicable
Describe how these components interact with each other
The specifications contained in this document are written from a developer’s perspective and it is used to support the system through its lifecycle.
This document is created in compliance with and under the guidance of procedure BTSQC09.05, Computer Systems Lifecycle and Validation.
## Acronyms and Definitions
List and explain any terms or acronyms that might be unfamiliar, useful, or have specific meaning in the document’s context to the reader of the document. State whether terms are in the Glossary or in this document only. When no terms are applicable, delete Acronyms and Definitions section.
Click this link to access the Abbott Glossary.
## References
List the document number and title of all documents referenced throughout the document.
## Roles and Responsibilities
Describe who is responsible for performing the activities or actions described within this document. Add multiple rows, as necessary
# SYSTEM CONTEXT
Define the interactions of the system with its environment. The system context is a model of the system and the environment in which the system resides.  The model should show the system and the inputs and outputs to and from external systems.  Systems in a context diagram may be electronic systems, manual systems or individual actors.
The system context is shown below.
# PROCESS MODEL
Provide a process model. A process model provides modeling of business processes and
Defines the key processes used by a business
Models any or all of these processes in detail
Determines when a record is declared and when it should be disposed or archived
Identifies processes that need improvement and
Models new processes before they are implemented.
The process model is shown below.
# SYSTEM ARCHITECTURE
## System Architecture
Show the
Configuration of run-time physical elements (multiple instances of web, application and database servers),
Software components and data that live on the components
Network connections and firewalls between the components
Include resource estimates for communications network capacity (Local Area Network (LAN) and Wide Area Network (WAN)) needed to install and execute each application on each platform
Indicate if the processing system is distributed or centralized
Include resource estimates for processor capacity, memory, online storage and auxiliary storage
The system architecture is based on standard hardware as described below and located in a server environment. Qualified in <data center> located in <location>. An overview is shown below.

System Architecture
## Software Architecture
Document the required operating system (including specific version and release numbers) and required drivers for networks and peripheral devices.  Also address any additional runtimes or drivers required for the new application.  These most often include database packages, runtime libraries and middleware libraries.  Finally, other required software packages should be addressed such as COTS, third-party, or records and information archiving software.  These include applications such as communication programs, backup systems, etc., that may be required to run the application.
For third-party libraries used, if not using the latest stable version, document justification and risk acceptance either here or in the supporting Software Detailed Design Description template (BTSQC09.05-O).
Document the required software configurations for servers running the application.  If the application will support more than one server software configuration, several server software architecture definitions should be created.  Only information required by the application should be included.
The Software Architecture attributes of the computer system are described below
## Application Architecture
Describe all the components of the application architecture.
Display the layered architecture showing the presentation layer, application layer and data layer
If needed describe how each component can be further divided into subcomponents and describe the relation and interaction between those components
Include data flow diagrams
Show protocols used by the components to interact with each other
If the system has parts which are already existing before this development effort, then only describe the relation between new parts and existing parts
The Application Architecture attributes of the computer system are described below

QWP Computer System Software Application Architecture
## Data Architecture
Describe at a high level the data architecture and types of data that will be required by the system.  The low-level details should be specified in the Software Database Design template (BTSQC09.05-N).
Describe the data model or include a diagram. When applicable, indicate the systems that own the data. Items to consider include internal and external data sources, physical structure of databases, database sizing, the type of relational database management system, online analytical processing design, or extract, transform, load (ETL) design.
Consider the following with regard to data integrity and architecture:
Can the system maintain data integrity while multiple users are processing the same record?
Can the system maintain data integrity while a single user is processing multiple records?
Consider the following with regards to Data Lifecycle Management (DLM):
Can records be created, managed, and disposed according to the retention periods defined in the DLM Assessment?
What data attributes comprise the record for each record type defined in the DLM Assessment?
Can records be locked such that editing, or disposal cannot occur when one or more Legal Hold Orders are in effect?
How much records and information should remain in the production environment?  When should records and information be archived?
Can the records and information be archived to lower cost storage and to optimize volume kept in production environments? The system data architecture is based on data as described below and stored, transferred in the application, etc.
The Data Architecture attributes of the computer system are described below
## Interface Architecture
This section is intended to provide a high-level interface architecture description and/or diagram.  The low-level details should be specified in the Software Interface Design template (BTSQC09.05-P). See the Data Architecture section above for description or diagram of the data model.
If there are no interfaces of any type, include a statement that there are no interfaces included in the system design.
An interface is defined as two applications or systems that send/receive information to/from each other. Describe the interface(s) between the system being developed and other systems (e.g., batch transfers, queries, etc.).
Consider both internal (inside the system) and external (outside the system) interfaces, and those where the application is acting as a service provider (push) or as a consumer of a service (pull).
The Interface Architecture attributes of the computer system are described below

# SECURITY
Describe the physical and functional components of the system that meet the system’s technical security and cybersecurity requirements. Include all tools and processes needed to perform these services. Vendor security, third party security, database security, network security, applications, and operating system security are examples.  User profiles and roles may be described here.  Describe the design in this section that addresses security for 21 CFR Part 11 requirements (for quality-related systems).  Only information required by the application should be included.
In addition, cybersecurity considerations include the following technical security considerations for systems with data classified as Restricted or Highly Restricted (see 4-CS.01.STD.04 Technical Security Controls) and secure by design elements (see AQ1902.A Non-Product Software Cybersecurity for more details):
Access, Identification, Authentication and Authorization
Access control
Remote connection -
Audit and Accountability
System and Communication Protection and Data Controls
Data encryption
Secure interfaces
Configuration and Architecture, e.g., geography considerations
Event Logging and Incident Response
Security Assessment
Physical Security
Malware protection
System hardening
Notification for identifying and notifying users upon detection of a potential cybersecurity breach
The technical security and cybersecurity architecture aspects are described below at a high-level.
# CONFIGURATION ITEM INVENTORY (CII)
This Configuration Item Inventory (CII) is NOT required except for Quality Critical or Quality Non-Critical systems of type Configurable or Custom.
Include impacted configuration items here. In the case of cloud-based applications, specify the application as the configurable item. There is no need to specify instance names as they are dynamic.
## Configuration Management
## Provide justification for CMD difference between Test and Production in the table below. This justification can also be provided in the SLC Plan, Validation Plan, or Installation & Deployment Plan.  If justification is provided in another document, make a reference in the table below.
# PERFORMANCE
Provide a graphical representation with detailed information for each of the individual performance and reliability hardware components to include the below items:
Capacity and volume requirements / estimates
Performance expectations
Performance design to meet capacity requirements
Reliability design to meet availability requirements
The table below identifies performance specifications.
# RESILIENCY
## Describe at a high-level the availability, backup, restore, and Disaster Recovery design specifications relevant in the event of a failure, including a failure due to a cybersecurity event
## Availability
Describe the design considerations for ensuring that the system will meet availability requirements.  Included should be tools, functions, and processes used to ensure system availability.  Any single points of failure in the architecture should be described in detail here.  Troubleshooting methods to be practiced if the failover does not occur should be documented.
## Backups
## Restore Testing
## Disaster Recovery
Describe the tools, functions, and processes required to support the disaster recovery plan.  Reference the disaster recovery plan as appropriate.
Describe backup requirements such as business requirements for business continuity.  This includes backup feature / function and data.  Describe the types and frequencies of the backups.  Refer to any backup and recovery procedures in this section.
# APPENDICES
If appendices are used, itemize here. If none, use “Not applicable.”
## Appendix A	CII Item Details
# ATTACHMENTS
If attachments are used, itemize here. If none, use “Not applicable.”
## Attachment 1	CII Item Details

END OF DOCUMENT

| These instructions are guidance information within the body of the template.
DO NOT MODIFY STYLES.
Blue text is sample and / or optional text. Select the appropriate value or remove. 
Red text is instructional. Delete or replace all red text in final version. Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template.
Black text is required and must be addressed in the template. All text must be black in the final version. |
| --- |
| This System Architectural Design and Configuration Item Inventory (CII) template is intended to be utilized to document the architecture, and if applicable, the configuration item inventory, of a new system or major release. The template content may be tailored, (i.e., expanded or deleted) to address the needs of the project.  This document is unique to a computer system and therefore, none will look alike or even have all the same sections. It is the responsibility of the technical team to define relevant content to support the system.
This template may be supported by the Software Detailed Design Description template (BTSQC09.05-O), and/or the Software Database Design Description template (BTSQC09.05-N), and/or the Software Interface Design Description template (BTSQC09.05-P), as applicable.
Per BTSQC09.05,this Architectural Design and Configuration Item Inventory template applies as follows:
As a reminder, this template also applies for all Regulated (Quality or Non-Quality) systems that utilize Software-as-a-Service (SaaS) hosting, following the table above based on the System Type. 
Header Instructions:
The following information should appear on each page of the document (i.e., be included in the header of the document by replacing the template’s header.
Application Name and Acronym – Enter the application name and acronym as documented within the Document Management System and Application Inventory.
Application Inventory ID – Enter the ID from the Application Inventory
Document ID: Enter the document identifier for easy retrieval from the VMS tool.
M-Files: Document Collection ID
WindChill: Document ID
Document Version: Enter the version number of this document.
Document Name: Provide the name of the document. |
| Template Instructions End |
| Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template. |


| Document Prepared by: | Document Prepared by: | Document Prepared by: |
| --- | --- | --- |
| Name and Function | Signature | Date (DD-MON-YYYY) |
| Author | Captured electronically | Captured electronically |


| Document Approvals: | Document Approvals: | Document Approvals: |
| --- | --- | --- |
| Name and Function | Signature | Date (DD-MON-YYYY) |
| Technical Architect | Captured electronically | Captured electronically |
| SME Title / SME
Remove this row if not required. | Captured electronically | Captured electronically |


| Revision History: | Revision History: | Revision History: | Revision History: |
| --- | --- | --- | --- |
| Document Version # | Revision Date
(DD-MON-YYYY) | Author | Change Summary
(Reference section[s] changed) |
| 1.0 |  |  | Initial writing – describes the system architectural design and, if applicable, the configuration item inventory |
|  |  |  |  |


| Term / Acronym | Definition |
| --- | --- |
|  |  |
|  |  |


| Document Number | Document Title |
| --- | --- |
|  |  |
|  |  |


| Function | Responsibility |
| --- | --- |
| Technical Architect | Review and approval of the document |
| IT – Technical Team | Document business process models, system architecture aspects including cybersecurity, data flows, configuration items if applicable, failover/disaster recovery mechanisms, and performance considerations, and update as needed as part of each release / upgrade |


| Software | Release / Version | Library |
| --- | --- | --- |
| Windows OS | 10.2.4.11 |  |


| Design Elements | Design Considerations |
| --- | --- |
|  |  |
| Audit and Accountability |  |
| system and Communication Protection and Data Controls |  |
| Configuration and Architecture |  |
| Event Loggins and Incident Response |  |
| Security Assessment |  |
| Physical Security |  |
| System Hardening |  |
| Notifications |  |


| Item | Description | Type | Version | System Identifier |
| --- | --- | --- | --- | --- |
| The name of the software / hardware application configuration item. | A brief description of the storage configuration item (e.g., SAN Storage Capacity). | Type of the system – software, application, security .etc | The version number of each software configuration item. | The location of the software application via system identifier. |
|  |  |  |  |  |


| Justification of CMD Difference Between Test / QA and Production |
| --- |
|  |


| Performance Parameter | Details |
| --- | --- |
| Capacity / Volume |  |
| Performance |  |
| Capacity |  |
| Reliability |  |


| Availability Consideration | Details / Comments |
| --- | --- |
|  |  |
|  |  |
|  |  |


| Name | Backed-up Item | Backup Type | Frequency | Method |
| --- | --- | --- | --- | --- |
| CSXXX | Database Server | Incremental | Real-time | Rubrik |
| CSXXX | Database Server | Full | Daily | Rubrik |
| CSXXX |  |  |  |  |


| Restore Testing Strategy | Environment | Frequency |
| --- | --- | --- |
| Restore Hidden table “XYZ.” | Production | Annual |
|  |  |  |


| Disaster Recovery Steps | Responsible | Actions |
| --- | --- | --- |
| DR Plan # | 1234567 | 1234567 |
| Perform regular system backups. | IT Infrastructure | RPO set to 4 hours
RTO set to 2 hours |
| Declare a disaster | System Owner | Send email to all users. |
|  |  |  |
