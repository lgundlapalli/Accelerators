
Software Interface Design Description
By approving this document, you attest that you have completed training on BTSQC09.05 and agree with the Software Interface Design Description for this system.



When revising the document, add an additional row below the v1.0 line and complete the revision history information per document revision in a sequential manner.


# OVERVIEW
## Table of Contents
1.0	OVERVIEW	5
1.1	Table of Contents	5
1.2	Purpose	5
1.3	Acronyms and Definitions	5
1.4	References	6
1.5	Roles and Responsibilities	6
2.0	SYSTEM INTERFACE DEFINITION	6
2.1	Hardware Interfaces	6
2.2	Service Interfaces	6
2.3	Filtering Criteria and Routing Rules	6
2.4	Error Handling, Notification, Reconciliation, and Reprocessing	7
2.5	Security and Logging	7
2.6	User Interfaces	7
2.6.1	Functions	7
2.6.2	Screens / Graphical User Interface	8
2.6.3	Forms	8
2.6.4	Reports	8
3.0	APPENDICES	8
4.0	ATTACHMENTS	8
## Purpose
This document describes the interface  parameters intended to satisfy the system’s functional behaviors, which support the business needs for the <Computer System Name>, to support Abbott < division > deployment.
The specifications contained in this document are written from a developer’s perspective and it is used to support the system through its lifecycle
This document is created in compliance with and under the guidance of procedure BTSQC09.05, Computer Systems Lifecycle and Validation.
## Acronyms and Definitions
List and explain any terms or acronyms that might be unfamiliar, useful, or have specific meaning in the document’s context to the reader of the document. State whether terms are in the Glossary or in this document only. When no terms are applicable, delete Acronyms and Definitions section.
Click this link to access the Abbott Glossary.
Note:  The following terms are document specific and are included for reference in this document only.
## References
List the document number and title of all documents referenced throughout the document.
## Roles and Responsibilities
Describe who is responsible for performing the activities or actions described within this document. Add multiple rows, as necessary
# SYSTEM INTERFACE DEFINITION
An interface is defined as two applications or systems that send/receive information to/from each other. Describe the interface(s) between the system being developed and other systems (e.g., batch transfers, queries, etc.). Consider both internal (inside the system) and external (outside the system) interfaces, and those where the application is acting as a service provider (push) or as a consumer of a service (pull).
If needed for context, add a reference here to the data model which may be in the System Architectural Design template (BTSQC09.05-AS) or the Software Database Design template (BTSQC09.05-N).
This section defines the interface design for the system.
## Hardware Interfaces
Define hardware interfaces that application depends on.
## Service Interfaces
If the application is acting as a service provider reference the document which provides the high-level description of the message schemas with the following information along with the schema documents
Field Name
Data Type
Cardinality
Optionality
Encryption
Description
Comments
If applicable, state expectations for ongoing maintenance of consumer services. Specifically, if system access is requested and granted to another system (not an individual), constituting a new consumer service, the individual approving the access to this system is responsible to notify the technical team so they are aware and so that this interface documentation can be updated with the next document revision.
If the application is a consumer of an internal/external service, reference the mapping document which will provide the high-level mapping of the source and target elements for each of the services. The document should contain the following information
Source Fields
Target Fields
Comments
Custom logic
Cardinality/Optionality

## Filtering Criteria and Routing Rules
List the filtering business rules that apply to this interface, e.g. “All purchase orders when have been changed should have their status set to “Released”or “Only address changes to purchase orders, as creation of purchase orders is handled via a separate interface”.
For routing, provide key fields and parameters that determine the data split. If the source files/data need to be routed to different targets, describe the fields that would determine where to route the file/data and how the file/data would be parsed, e.g. if company code and cost center determines the partner.
## Error Handling, Notification, Reconciliation, and Reprocessing
Describe how errors are detected, communicated, and resolved. Specify the error handling technique that will be used, and the action:
All or nothing: If there is an error, roll back any processed data and stop processing.
Only Good Data: If there is an error, skip the erroneous record and continue processing.
Stop Processing: Run until there is an error, then stop, but don’t roll anything back.
Other: Error log to be populated in the output screen with relevant messages.
Errors from downstream services have to be translated, logged and mapped to client facing error codes. User friendly error codes and messages need to be mapped and internal error code should not be exposed. List these error code mappings in the following table format
## Security and Logging
Describe the authentication and authorization mechanism between the interfaces (Internal/External) of both systems as well as services. Security-related logging should also be described here.
## User Interfaces
In this section, address all hardware, software, screens, menus, functions and features, that affect two-way communications between the user and the system.
### Functions
For every function
Input Source
Input Controls
Output Controls
Output information
Messages /Alerts
Error Handling
### Screens / Graphical User Interface
Include any UI screen, navigation items, wireframes.
Screens / GUIs include…
### Forms
Include form and list the individual fields along with any constraints.
Forms include…
### Reports
Include the report format, data constraints.
Reports include…
# APPENDICES
If appendices are used, itemize here. If none, use “Not applicable.”
Appendix A
# ATTACHMENTS
If attachments are used, itemize here. If none, use “Not applicable.”
Attachment 1	Service Schemas Documents
Attachment 2	Service Mapping Documents
END OF DOCUMENT

| These instructions are guidance information within the body of the template.
DO NOT MODIFY STYLES.
Blue text is sample and / or optional text. Select the appropriate value or remove. 
Red text is instructional. Delete or replace all red text in final version. Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template. 
Black text is required and must be addressed in the template. All text must be black in the final version. |
| --- |
| This Software Interface Design Description template is intended to translate a computer system’s functional requirements related to interface design to detailed construction and build documentation. This document is a “conversation” between developers and IT support staff to facilitate an understanding of how functions are built. The template content may be tailored, (i.e., expanded or deleted) to address the needs of the project. This document is unique to a computer system and therefore, none will look alike or even have all the same sections. This topic may be addressed in one document, or for large systems with modules or workflows, may be broken into separate documents. This is a very flexible template and should be adapted to the system’s needs. It is the responsibility of the technical team to define relevant contents to support the system.
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
| 1.0 |  |  | Initial writing – describes the software interface design for the system |
|  |  |  |  |


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
| IT – Technical Team | Document interfaces, including authorization and authentication mechanisms, error mapping and handling, and input and outputs along with constraints. 
As part of each release / upgrade, update documentation as needed for interfaces, including authorization and authentication mechanisms, error mapping and handling, and input and outputs along with constraints. |


| Name | Internal/External | Version | Constrains |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |


| Error Message Number | Error Message Text | Error Conditions | Notification | Reprocessing Requirements |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


| Source Code | Description | Consumer Code | Message |
| --- | --- | --- | --- |
|  |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |


| ID | Function | Description | Constrains |
| --- | --- | --- | --- |
| CSXXX |  |  |  |
