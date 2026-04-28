
Software Database Design Description
By approving this document, you attest that you have completed training on BTSQC09.05 and agree with the Software Database Design Description for this system.



When revising the document, add an additional row below the v1.0 line and complete the revision history information per document revision in a sequential manner.


# OVERVIEW
## Table of Contents
1.0	OVERVIEW	5
1.1	Table of Contents	5
1.2	Purpose	6
1.3	Acronyms and Definitions	6
1.4	References	6
1.5	Roles and Responsibilities	6
2.0	SOFTWARE DATABASE DESIGN DEFINITION	7
2.1	Database Interface Diagram	7
2.2	Entity Definitions	7
2.3	Attribute Definitions	7
2.4	Relationship Definitions	8
2.5	Table Definitions	8
2.6	Column Definitions	8
2.7	Record Definitions	8
2.8	Data Archive and Purge	9
2.9	Critical Components	9
2.10	Database Views	9
2.11	Triggers	9
2.12	Indexes	10
2.13	Sequences	10
2.14	Data Model / Definition / System Data	10
2.15	Databases and File Collections	11
2.16	Files	11
2.17	Records	11
2.18	Data Types	11
2.19	Database Software	12
3.0	DATABASE SECURITY	12
4.0	DATABASE SIZING	13
5.0	APPENDICES	13
6.0	ATTACHMENTS	13

## Purpose
This document describes the database   parameters intended to satisfy the system’s functional behaviors, which support the business needs for the <Computer System Name>, to support Abbott < division > deployment.
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
# SOFTWARE DATABASE DESIGN DEFINITION
This section defines the software database design for the system.
Describe the database design definition using subsections below. Add additional subsections as needed for other types of database objects that are part of the design, for example:
Packages and Procedures
Synonyms (both Private and Public)
Functions
Database Links
Database Directories
Other, e.g., usage of any other uncommon features and/or placeholder for new features in future database software versions.
A logical model or an Entity-Relationship Diagram (ERD) may be used for subsections 2.2-2.4.
## Database Interface Diagram
Include an architectural diagram of application interfaces into/out of the database.
## Entity Definitions
List and describe relevant entities. An entity is a thing of significance, whether real or conceptual, about which the business or system being modeled needs to hold information (e.g., customer or employee).
## Attribute Definitions
List and describe attributes. An attribute is any detail that serves to qualify, identify, classify, quantify, or express the state of an entity (e.g., an employee would have a name, social security number, or address).
## Relationship Definitions
List and describe all relationships between entities.
## Table Definitions
List all tables with name and description.
## Column Definitions
List all tables, columns, data types, column sizes, and constraints.
Note: For systems with a large number of tables and columns, this can be added as appendix or attachment at the end of this document
## Record Definitions
If applicable, list all record series codes, record descriptions, table names and column names.
Note: For Records Series Codes, refer to the Data Lifecycle Management (DLM) Assessment.
The following design criteria should be documented for each Record Series Code (expand below table or add table if needed):
How would records and information eligible for disposal be identified and acted upon?
If a Legal Hold Order (LHO) was issued, how would the records be locked (i.e., disposal of records prevented until the LHO was released)?
## Data Archive and Purge
List specifications for data archival and purge design, including online data retention and archival data retention requirements.
## Critical Components
Remove this section if the system is not classified as Critical.
For only the features identified as Critical in the Functional Requirements Specification, describe the audit trail, electronic copies, and record retention specifications for critical components of the database or electronic records relevant to 21 CFR Part 11.
## Database Views
A view is any relation that is not part of the data model but is made visible to a user as a “virtual relation”. Provide a list of the key, affected views, their descriptions, and column names.
Include Materialized Views if applicable.
## Triggers
A trigger is a statement that is executed automatically by the system as a side effect of a modification to the database such as insert, update and delete.
Provide a list of key, affected tables, triggers, and types of triggers. Triggers may be used to enforce 21 CFR Part 11 audit trail requirements. It can be implemented by having a history table for each table. Triggers used to implement 21 CFR Part 11 should be described, when applicable.
## Indexes
Describe the types of indexes used. An index, or keyed sequence access path, provides access to a table that is arranged according to the contents of key columns. The keyed sequence is the order in which rows are retrieved. The access path is automatically maintained whenever rows are added to or deleted from the table, or whenever the contents of the index columns are changed.
Columns that are good candidates for creating indexes are as follows
Columns that are frequently referenced in row selection predicates
Columns that are frequently referenced in grouping or ordering and
Columns that are used to join tables.
## Sequences
A sequence is a surrogate primary key; it also provides values for the key column. Such sequences are never modified after their initial creation. It is a means of uniquely identifying entities within an entity set.
Provide a list of key, affected sequences.
## Data Model / Definition / System Data
Define system data and major data objects. Data should be defined in a hierarchical manner, building smaller components into more complex. This may include table relationships, primary keys or any data schema / structure attribute.
## Databases and File Collections
Each file collection and data structure should be considered and identified.
## Files
Each file and data structure should be considered and identified
## Records
## Data Types
Formal data description methods should be used.
## Database Software
Detail any required software products or dependencies in addition to the standard DBMS software.

# DATABASE SECURITY
This section defines the database security for the system.
Describe how database security will be implemented, based on applicable requirements for the Data Sensitivity Classification defined in the System Risk Classification.  Details to consider include, where applicable:
Authentication and authorization details
Owners and users of end-user profiles
Required system privileges for schemas
Required system roles for schemas
Specific audit policies, audit data retention period (if non-standard) or other audit requirements
Group roles of users accessing the system and what authorizations they require
Verify that vendor supplied default passwords for database systems and associated layered applications have been changed to comply with Abbott IT 4-020-001 Information Security and Access Password Controls Procedure.
# DATABASE SIZING
Below is the list of tables along with initial size estimates, which is determined based on the number of rows, number of columns, maximum variable size, indexes on the table. The growth rate provides information for future capacity needs.
Describe the database size and growth rate. Database size estimates should include on-line history requirements, expected data growth rates over a 5-year period, audit log sizes, and data copies, replications, or archives. These size estimates may be critical for allocating file resources, budgeting for storage and addressing performance issues. Details such as table names and initial sizes should be included.
# APPENDICES
If appendices are used, itemize here. If none, use “Not applicable.”
Appendix A	Database Detail Design
# ATTACHMENTS
If attachments are used, itemize here. If none, use “Not applicable.”
Attachment 1	Database Table Relationship
END OF DOCUMENT

| These instructions are guidance information within the body of the template.
DO NOT MODIFY STYLES.
Blue text is sample and / or optional text. Select the appropriate value or remove. 
Red text is instructional. Delete or replace all red text in final version. Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template.
Black text is required and must be addressed in the template. All text must be black in the final version. |
| --- |
| This Software Database Design Description template is intended to translate a computer system’s functional requirements related to database design into detailed construction and build documentation. This document is a “conversation” between developers and IT support staff to facilitate an understanding of how functions are built. The template content may be tailored, (i.e., expanded or deleted) to address the needs of the project. This document is unique to a computer system and therefore, none will look alike or even have all the same sections. This topic may be addressed in one document, or for large systems with modules or workflows, may be broken into separate documents. This is a very flexible template and should be adapted to the system’s needs. It is the responsibility of the technical team to define relevant contents to support the system.
This template provides supporting information for the System Architectural Design template (BTSQC09.05-AS) and the Software Detailed Design Description template (BTSQC09.05-O). 
Per BTSQC09.05, this Software Database Design Description template applies as follows:
 
Header Instructions:
The following information should appear on each page of the document (i.e., be included in the header of the document by replacing the template’s header.
Application Name and Acronym – Enter the Application name and acronym as documented within the Document Management System and Application Inventory.
Application Inventory ID – Enter the ID from the Application Inventory
Document ID: Enter the document identifier for easy retrieval from the VMS tool.
M-Files: Document Collection ID
WindChill: Document ID
Document Version: Enter the version number of this document.
Document Name: Provide the name of this document. |
| Template Instructions End |
| Use the Paragraph (¶) button in the Toolbar to toggle on/off the red instructional text in this template. |


| Document Prepared by: | Document Prepared by: | Document Prepared by: |
| --- | --- | --- |
| It is strongly recommended that this document be reviewed by a member of the Database Architect team prior to finalizing each revision. Name and Function | Signature | Date (DD-MON-YYYY) |
| Author | Captured electronically | Captured electronically |


| Document Approvals: | Document Approvals: | Document Approvals: |
| --- | --- | --- |
| Name and Function | Signature | Date (DD-MON-YYYY) |
| Technical Architect | Captured electronically | Captured electronically |
| SME Title / SME
Remove this row if not required. | Captured electronically | Captured electronically |


| Revision History | Revision History | Revision History | Revision History |
| --- | --- | --- | --- |
| Document Version # | Revision Date
(DD-MON-YYYY) | Author | Change Summary
(Reference section[s] changed) |
| 1.0 |  |  | Initial writing – describes the software database design for the system |


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
|  |  |


| Function | Responsibility |
| --- | --- |
| Technical Architect | Review and approval of the document |
| IT – Technical Team | Document database configurations, design, connections, functions, and any relevant system information for development and maintenance
As part of each release / upgrade, update documentation as needed for database configurations, design, connections, functions, and any relevant system information for development and maintenance |


| Entity | Entity Name | Description |
| --- | --- | --- |
|  |  |  |


| Entity Name | Attribute Name | Description |
| --- | --- | --- |
|  |  |  |


| Relationship Name | Description |
| --- | --- |
|  |  |


| Table Name | Description |
| --- | --- |
|  |  |


| Table Name | Column Name | Data Type | Column Size | Constraint
(Primary Key, Foreign Key, Domain) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |


| Record Series Code | Record Description | Table Name | Column Name |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |


| Specification | Description | Comments |
| --- | --- | --- |
|  |  |  |


| Component | Functionality | Comments |
| --- | --- | --- |
|  |  |  |


| View Name | Description | Column Name |
| --- | --- | --- |
|  |  |  |


| Trigger | Description | Action |
| --- | --- | --- |
|  |  |  |


| Index | Description | Columns |
| --- | --- | --- |
|  |  |  |


| Sequence | Description | Comments |
| --- | --- | --- |
|  |  |  |


| Name | Data | Description |
| --- | --- | --- |
| CSXXX |  | Database schema |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Database / File Collection | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | File | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Record | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Name | Data Type | Description |
| --- | --- | --- |
| CSXXX |  |  |
| CSXXX |  |  |
| CSXXX |  |  |


| Product | Description or Dependency | Comments |
| --- | --- | --- |
|  |  |  |


| Detail | Description |
| --- | --- |
| Role Based Access Control |  |
| Data Encryption |  |
| Realtime Monitoring |  |


| Table Name | Initial Size | Growth Rate | Type of Table Transactional,
Look-up, etc. |
| --- | --- | --- | --- |
|  |  |  |  |
