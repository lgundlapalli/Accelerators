
Software Detailed Design Description (SDDD)
By approving this document, you attest that you have completed training on BTSQC09.05 and agree with the Software Detailed Design Description (SDDD) for this system.



When revising the document, add an additional row below the v1.0 line and complete the revision history information per document revision in a sequential manner.


# OVERVIEW
## Table of Contents
1.0	OVERVIEW	5
1.1	Table of Contents	5
1.2	Purpose	6
1.3	Acronyms and Definitions	6
1.4	References	6
1.5	Roles and Responsibilities	7
2.0	MODULES / COMPONENTS	7
3.0	FUNCTIONS	7
3.1	Function 1	8
3.1.1	Input	8
3.1.2	Output	9
3.1.3	Messages / Diagnostics / Alarms	10
3.1.4	Help	11
3.1.5	Error Handling	11
3.1.6	Maintenance	11
4.0	FUNCTIONAL SECURITY	11
4.1	Access, Identification, Authentication and Authorization	12
4.2	Audit and Accountability	12
4.3	System and Communication Protocol and Data Controls	13
4.4	Configuration and Architecture	13
4.5	Event Logging and Incident Response	13
4.6	Security Assessment	13
4.7	Physical Security	13
4.8	Malware Protection	14
4.9	System Hardening	14
4.10	Notification for Cybersecurity Breach	14
5.0	OPERATING MODES	14
5.1	Manual	14
5.2	Automatic	15
6.0	CUSTOM CODE AND CONFIGURATION FILE NAMES	15
7.0	RESILIENCY	15
7.1	Availability	15
7.2	Backups	16
7.3	Restore Testing	16
7.4	Disaster Recovery	16
8.0	PERFORMANCE CONSIDERATIONS	16
9.0	APPENDICES	17
10.0	ATTACHMENTS	17
## Purpose
This document describes the detailed   parameters intended to satisfy the systems functional behaviors, which support the business needs for the <Computer System Name>, to support Abbott < division > deployment.
The specifications contained in this document are written from a developer’s perspective and it is used to support the system through its lifecycle.
This document is created in compliance with and under the guidance of procedure BTSQC09.05, Computer Systems Lifecycle and Validation.
## Acronyms and Definitions
List and explain any terms or acronyms that might be unfamiliar, useful, or have specific meaning in the document’s context to the reader of the document. State whether terms are in the Glossary or in this document only. When no terms are applicable, delete Acronyms and Definitions section.
Click this link to access the Abbott Glossary.
Note:  The following terms are document specific and are included for reference in this document only.
## References
List the document number and title of all documents referenced throughout the document.
## Roles and Responsibilities
Describe who is responsible for performing the activities or actions described within this document. Add multiple rows, as necessary.
# MODULES / COMPONENTS
For each module or component that comprises the system (database, application server, main software, web server), address:
Module operation – a flow chart may be used
Interfaces to other modules – a system diagram may be used
Any timing considerations – timeouts, retries
Error handling and data checking
What system data the module / component uses
Any third-party libraries used, and if not using the latest stable version, document justification and risk acceptance
# FUNCTIONS
Each function in the system that had to be configured or developed is included here. Repeat this section as many times as needed. COTS functions do NOT need to be specified here.

## Function 1
Repeat this for as many functions as needed.
### Input
Input Source
Function 1 Control Parameter Input
Function 1 Input Screens Format
Provide details on how the data is processed. If none, use “Not applicable.”
Function 1 Processing
Describe any processes for data conversion. If none, use “Not applicable.”
Function 1 Data Conversion
Describe any processes for data calculations. If none, use “Not applicable.”
Function 1 Data Calculations
Describe any processes for data validity checks. If none, use “Not applicable.”
Function 1 Data Validity Checks
### Output
Describe any data output types. If none, use “Not applicable.”
Function 1 Data Outputs
Describe how data outputs are controlled. If none, use “Not applicable.”
Function 1 Data Output Controls
Describe output reports / display formats / Inquiry results. If none, use “Not applicable.”
Function 1 Information Outputs
### Messages / Diagnostics / Alarms
Describe any data output types. If none, use “Not applicable.”
Function 1 Messages / Diagnostics / Alarms
### Help
Describe any help functions. If none, use “Not applicable.”
Function 1 Help
Repeat this for as many functions as needed,
### Error Handling
Error Handling
Describe any alerts or notifications if the function fails or if it requires a manual verification, if it is proceduralized, etc.
### Maintenance
Maintenance
Describe how the function is maintained, who does it, and if it is proceduralized, etc.
# FUNCTIONAL SECURITY
Describe the physical and functional components of the system that meet the system’s technical security and cybersecurity requirements. Include all tools and processes needed to perform these services. Vendor security, third party security, database security, network security, applications, and operating system security are examples.  User profiles and roles may be described here. Describe the design in this section that addresses security for 21 CFR Part 11 / Annex 11 requirements (for quality-related systems).  Only information required by the application should be included.
Address the details of cybersecurity design considerations, which include the following technical security considerations for systems with data classified as Restricted or Highly Restricted (see 4-CS.01.STD.04 Technical Security Controls) and secure by design elements (see AQ1902.A Non-Product Software Cybersecurity for more details):
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

## Access, Identification, Authentication and Authorization
## Audit and Accountability
## System and Communication Protocol and Data Controls
## Configuration and Architecture
## Event Logging and Incident Response
## Security Assessment
## Physical Security
## Malware Protection
## System Hardening
## Notification for Cybersecurity Breach

# OPERATING MODES
Describe the operating modes used within the system.
## Manual
Describe the manual modes. If none, use “Not applicable.”
## Automatic
Describe the automatic modes. If none, use “Not applicable.”
# CUSTOM CODE AND CONFIGURATION FILE NAMES
# RESILIENCY
## Availability
Describe the details of design considerations for ensuring that the system will meet availability requirements. Included should be tools, functions, and processes used to ensure system availability.  Any single points of failure in the architecture should be described in detail here. Troubleshooting methods to be practiced if the failover does not occur should be documented.
## Backups
Describe details of the backups. What gets backed up, when and how. Do not N/A this section.
## Restore Testing
## Disaster Recovery
Describe the tools, functions, and processes required to support the disaster recovery plan. Reference the disaster recovery plan as appropriate.
# PERFORMANCE CONSIDERATIONS
Describe details of performance considerations such as load balancing. Load balancing defines the required characteristics for maintaining the proper level of throughput through the system’s operating cycles.  Load balancing design elements include the tools, functions, and processes used to control the processing load.  This section should reference peak and minimal usage performance considerations.  Consideration for records and information archiving is important. Archiving reduces the volume of content in a production environment, thus eliminating the potential need for more CPUs, reducing the volume residing on expensive storage tiers and gaining or maintaining expected system performance.  Redundancy in the architecture should be documented here.
# APPENDICES
If appendices are used, itemize here. If none, use “Not applicable.”
Appendix A	System Configuration Report

# ATTACHMENTS
If attachments are used, itemize here. If none, use “Not applicable.”
Attachment 1	System Configuration Report
END OF DOCUMENT


| These instructions are guidance information within the body of the template.
DO NOT MODIFY STYLES.
Blue text is sample and / or optional text. Select the appropriate value or remove. 
Red text is instructional. Delete or replace all red text in final version. Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template.
Black text is required and must be addressed in the template. All text must be black in the final version. |
| --- |
| This Software Detailed Design Description (SDDD) template is intended to be utilized to translate a computer system’s functional requirements to detailed construction and build documentation. This document is a “conversation” between developers and IT support staff to facilitate an understanding of how functions are built. The template content may be tailored, (i.e., expanded or deleted) to address the needs of the project. This document is unique to a computer system and therefore, none will look alike or even have all the same sections. This topic may be addressed in one document, or for large systems with modules or workflows, may be broken into separate documents. This is a very flexible template and should be adapted to the system’s needs. It is the responsibility of the technical team to define relevant content to support the system.
This template provides supporting information for the System Architectural Design template (BTSQC09.05-AS), and may be supported by the Software Database Design Description template (BTSQC09.05-N) and/or the Software Interface Design Description template (BTSQC09.05-P), as applicable.
Per BTSQC09.05,this Software Detailed Design Description template applies as follows:
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
| 1.0 |  |  | Initial writing – describes the software detailed design for the system |
| 2.0 |  |  |  |


| Acronyms/ Terms | Definition |
| --- | --- |
|  |  |
|  |  |


| Document Number | Document Title |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |


| Function | Responsibility |
| --- | --- |
| Technical Architect | Review and approval of the document |
| IT – Technical Team | Document configurations, design, connections, functions and any relevant system information for development, maintenance
As part of each release / upgrade, update documentation as needed for configurations, design, connections, functions and any relevant system information for development, maintenance |


| Module | Interfaced Systems | Timing | Error Handling | Data Checking | Data Consumed |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


| Name | Attribute / Field | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Source | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Control | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Screen | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Function | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Spec # | Description |
| --- | --- |
| DSXXX |  |
| DSXXX |  |
| DSXXX |  |


| Name | Mode | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Mode | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| File Name | Description | Location |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |
| DSXX |  |  |
| DSXX |  |  |
| DSXX |  |  |


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


| Performance Consideration | Details / Comments |
| --- | --- |
|  |  |
|  |  |
|  |  |
