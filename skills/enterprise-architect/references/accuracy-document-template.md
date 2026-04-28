

Source Code Review Template
By approving this document, you attest that you have completed training on BTSQC09.05 and agree with the Source Code Review for this system.
When revising the document, add an additional row below the v1.0 line and complete the revision history information per document revision in a sequential manner.

# OVERVIEW
## 1.1	Table of Contents

1.0	OVERVIEW	4
1.1	Table of Contents	4
1.2	Purpose	4
1.3	Acronyms and Definitions	4
1.4	References	5
1.5	Roles and Responsibilities	5
1.6	Source Code Review Information	6
1.6.1	General Information	6
1.6.2	Source Code Module/Details	6
1.7	Source Code Review Checklist	7
1.8	Source Code Review Observations and Responses	8
## 1.2	Purpose
This Software Source Code Review template describes the steps to perform and document a manual Software Source Code Review prior to unit testing, qualification, or validation activities.
This document is created in compliance with and under the guidance of procedure BTSQC09.05, Computer Systems Lifecycle and Validation.
## 1.3	Acronyms and Definitions
List and explain any terms or acronyms that might be unfamiliar, useful, or have specific meaning in the document’s context to the reader of the document. State whether terms are in the Glossary or in this document only.
Click this link to access the Abbott Glossary.
Note:  The following terms are document specific and are included for reference in this document only.
## 1.4	References
List the document number and title of all documents referenced throughout the document.
## 1.5	Roles and Responsibilities
Describe who is responsible for performing the activities or actions described within this document. Add multiple rows, as necessary
## 2.0	Source Code Review Information
### 2.1	General Information
### 2.2	Source Code Module/Details
## 3.0	Source Code Review Checklist


## 4.0	Source Code Review Observations and Responses
Below are the observations and responses from this Software Source Code Review.  The responses result from analysis by and discussion with the Developer/Code Author.
If response includes no rework or N/A is marked, provide an explanation. Indicate if a follow-up review is required to confirm correction.
If a defect in the software source code is noted, the Reviewer is expected to notify the Developer and not approve the review.

end of document


| These instructions are guidance information within the body of the template.
DO NOT MODIFY STYLES.
Blue text is sample and / or optional text. Select the appropriate value or remove. 
Red text is instructional. Red text will not appear in the PDF version. Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template.
Black text is required and must be addressed in the template. All text must be black in the final version. |
| --- |
| The Source Code Review template is used to perform manual peer reviews of Abbott custom code.  Source Code Reviews are intended to be performed before unit testing, qualification, or validation activities commence. 
This form is not applicable for Source Code Reviews of Abbott custom code performed using automated tools, and is not applicable to source code owned and maintained by third parties. 
Per BTSQC09.05, Source Code Reviews are required for Quality Critical Custom functions.
Header Instructions:
The following information should appear on each page of the document (i.e., be included in the header of the document).
Application Name and Acronym – Enter the application name and acronym as documented within the Document Management System and Application Inventory.
Application Inventory ID – Enter the ID from the Application Inventory
Document ID: Enter the document identifier for easy retrieval from the VMS tool.
M-Files: Document Collection ID
WindChill: Document ID
Document Version: Enter the version number of this document.
Document Name: Provide the name of the document.
Change Number: Provide the Change number |
| Template Instructions End |
| Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template. |


| Source Code Reviewed by: | Source Code Reviewed by: | Source Code Reviewed by: |
| --- | --- | --- |
| Name and Function Reviewer must be a different person than the code author. | Signature | Date (DD-MON-YYYY) |
| Technical Architect May be the sole Reviewer if not also the code author. | Captured electronically | Captured electronically |
| Reviewer Name Remove this row if not required. | Captured electronically | Captured electronically |


| Revision History: | Revision History: | Revision History: |
| --- | --- | --- |
| Document Version # | Revision Date
(DD-MON-YYYY) | Change Summary
(Reference section[s] changed) |
| 1.0 |  | Initial writing |


| Acronyms/ Terms | Definition |
| --- | --- |
| Source Code | Computer instructions and data definitions expressed in a form suitable for input to an assembler, compiler or other translator. The human readable version of the list of instructions (program) that cause a computer to perform a task. |
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
| Technical Architect | Reviewing and approving the Software Source Code Review
May act as sole IT Peer Reviewer if not also the code author |
| IT Peer Reviewer | Must be different than the IT Developer / Code Author
Any resource that understands the software source code and underlying business process sufficient to provide a meaningful review
Identifying and describing risks, incidents and issues in the documents or custom source code under review
Ensuring good coding practices are followed and the source code is accurately documented |
| IT Developer / Code Author | Ensuring that the document or software element is ready for code review
Participating in code review as a subject expert
Reworking source code to address risks, incidents or issues identified during the code review |


| Application/System Name |  |
| --- | --- |
| Application/System Version |  |
| Code Author / Developer Name(s) |  |


| Module | Functional / Design Reference 
If applicable, reference the Functional Requirement or Design Specification section related to the code file. | Version Indicate the source code file version. |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
| Add or delete rows as needed. |  |  |


| # | Source Code Review Checklist Question | Acceptance Criteria Met? | Acceptance Criteria Met? | Acceptance Criteria Met? |
| --- | --- | --- | --- | --- |
| 1 | Is the source code modular and reusable? Check whether the code utilizes modules and reusable services, functions, and components. Check that the Source Code does not contain any redundant code resulting in unnecessary executions. | Yes | No | N/A |
| 2 | Is the source code readable with sufficient annotations/ comments? Check that the code is self-explanatory, and that complex aspects are sufficiently annotated and/or commented to facilitate understanding by other developers. | Yes | No | N/A |
| 3 | Does the source code follow accepted naming practices for the system under review? Check whether the defined procedures are followed for naming. | Yes | No | N/A |
| 4 | Are modifications to the source code documented? Check whether the changes to the code have been documented and verified before transferring to production. | Yes | No | N/A |
| 5 | Is the source code configured for the Production environment for which it will be deployed? Check whether required configurations are available in production environment before movement of Source Code to production | Yes | No | N/A |
| 6 | Is the source code free of dead code? Check whether the Source Code contains obsolete or “dead” code whose execution is not the part of final computation, especially that which could present a potential security vulnerability? | Yes | No | N/A |
| 7 | Does the source code use appropriate error handling and alert / notification messages, both internally and for interfaces? Check that practices for error handling have been followed in the code. Check that interface error handling considers interface timing, external responses, and error conditions. | Yes | No | N/A |
| 8 | Does the source code use authorization checks as appropriate? Check whether authorization checks are followed during execution of process through source code. | Yes | No | N/A |
| 9 | Does the source code secure credentials and handle them appropriately? Check that database, interface, and other credentials are appropriate for the system. Check that the code does not have any default, cleartext, or hardcoded passwords. | Yes | No | N/A |
| 10 | Does the source code secure sensitive data? Check for encryption of sensitive data (e.g. credit card data, patient information). Check that sensitive algorithms are obfuscated or otherwise protected. | Yes | No | N/A |
| 11 | Does the source code include security elements? Check for secure code practices, e.g., authentication, authorization, input data validation, security of external interfaces, no developer back doors. | Yes | No | N/A |
| 12 | Is the source code maintainable? Check that code does not have references to hardcoded values/constants, allows for future growth and changes, and does not use hard to understand coding conventions. | Yes | No | N/A |
| 13 | Does the source code meet Abbott or system-specific coding standards? Check that required applicable software coding standards have been followed | Yes | No | N/A |
| 14 | Does the source code meet the Design? Check that the source code addresses the Architectural Design Description (i.e., - System, Software, Application, Database, Interface, and Security architecture, as well as performance and resiliency design considerations). | Yes | No | N/A |
| 15 | Does the source code include the software functionality to meet its intended use (i.e., meet FRS requirements)? Check that the source code is written to support the functionality needed to meet FRS requirements, including electronic records and audit trail functionality if applicable. | Yes | No | N/A |
| 16 | Does the version of the source code to be qualified show only expected code changes compared to the previous version? Mark as N/A if the source code under review is the initial version. | Yes | No | N/A |


| # | Observation Reference 
(e.g., Section #, Code Module) | Observation | Response |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 | Add or delete rows as needed. |  |  |
