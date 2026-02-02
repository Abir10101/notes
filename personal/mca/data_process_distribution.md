# Levels of Data & Process Distribution

## Overview
Data and process distribution determines how information and computational tasks are spread across computer systems, affecting system performance, reliability, and efficiency.

---

## Data Distribution Levels

### 1. Centralized Data
- All data stored in one central location
- Single point of access for all information
- Example: All files on one main computer

### 2. Distributed Data
- Data spread across multiple computers or servers
- Each location maintains its own portion of data
- Enables parallel access and processing

---

## Process Distribution Levels

### 1. Centralized Processing
- Single powerful computer/server handles all tasks
- All processing occurs at one location
- Simple management but potential bottleneck

### 2. Distributed Processing
- Multiple computers work together on tasks
- Processing workload shared across systems
- Improved speed and fault tolerance

---

## Distribution Architectures

### SPSD (Single-Site Processing, Single-Site Data)
**Characteristics:**
- All processing and data storage on one main computer
- Common in mainframe and midrange systems
- Users access via dumb terminals (no local processing)
- DBMS operates under time-sharing, multitasking OS

**Limitations:**
- Single point of failure
- Limited scalability
- All users depend on central system performance

---

### MPSD (Multiple-Site Processing, Single-Site Data)
**Characteristics:**
- Multiple computers process data
- Single centralized data repository (file server)
- Common in PC network environments
- File server acts as shared storage

**How it works:**
- Workstations send data requests to file server
- File server handles only data I/O operations
- Processing happens at individual workstations

**Drawbacks:**
- Entire files transferred over network for processing
- High network traffic and communication costs
- Slower response times
- File/record locking managed at workstation level

---

### SPMD (Single-Site Processing, Multiple-Site Data)
**Characteristics:**
- Single centralized processor handles all data operations from multiple locations
- Data distributed across multiple physical sites/nodes
- Data partitioned geographically or logically
- Common in geographically distributed organizations

**How it works:**
- All processing requests routed to central processor
- Central processor retrieves data from multiple remote sites as needed
- Data remains stored at distributed locations
- Processing results sent back to requesting locations

**Drawbacks:**
- Central processor becomes a bottleneck
- Single point of failure for all operations
- Limited scalability as processing demands increase

---

### MPMD (Multiple-Site Processing, Multiple-Site Data)
**Characteristics:**
- Fully distributed DBMS architecture
- Multiple data processors at different locations
- Multiple transaction processors across sites
- True distributed processing and storage

**Types:**

**Homogeneous DDBMS:**
- Single type of DBMS across all nodes
- Same database system on different platforms
- Easier integration and management

**Heterogeneous DDBMS:**
- Different types of DBMS integrated together
- Supports various data models (relational, hierarchical, network)
- Runs on diverse platforms (mainframes, PCs, servers)

---

## Key Takeaways

| Architecture | Processing Sites | Data Sites | Best For |
|--------------|-----------------|------------|----------|
| **SPSD** | Single | Single | Simple systems, centralized control |
| **MPSD** | Multiple | Single | File sharing, workgroup applications |
| **SPMD** | Single | Single | Geographically distributed applications |
| **MPMD** | Multiple | Multiple | Enterprise systems, high availability |
