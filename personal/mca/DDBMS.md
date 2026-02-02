# Distributed DBMS

### **Definition**

A **Distributed DBMS** is a database software system that manages a database spread across multiple physical locations while making it appear as a single logical database to the end user. In this system, data is not stored on a single machine but is distributed over a network of computers.

---

## Types of DDBMS

### 1. Based on Autonomy

#### Unfederated
* Tightly integrated with single centralized control.
* Common schema followed by all databases.
* Homogeneous system design.
* *Example:* Enterprise system with branches using identical databases.


#### Federated
* Loosely integrated.
* Individual, fully functional distributed databases.
* Can follow heterogeneous system design.
* *Example:* Multi-institutional data sharing networks.

### 2. Based on Distribution

#### Homogeneous
* All sites use the same DBMS software.
* Simple integration.


#### Heterogeneous
* Different DBMS software used at different sites.
* Complex integration process.

### 3. Based on Data Organization

* **Fragmented / Partitioned**
* Database is divided into fragments (horizontal or vertical).
* Each fragment is stored at different sites.
* *Example:* Customer data partitioned by region.


* **Replicated**
* Data rows are replicated or duplicated across multiple sites.
* Requires a synchronization mechanism across sites.
* *Example:* Product catalog replicated across regional servers.


* **Hybrid**
* Combines data fragmentation and replication.
* Some data is fragmented while some is replicated.
* Most common in practice for balancing performance and consistency.
