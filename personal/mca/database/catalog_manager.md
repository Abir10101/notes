## Catalog Manager in DDBMS

The **Catalog Manager** (also called **Data Dictionary Manager** or **Metadata Manager**) stores information about the data and provides essential information for query processing and optimization.

### Information It Stores

**1. Schema Information**
- Table definitions, structures, constraints
- Relationships between tables (foreign keys, primary keys)

**2. Data Distribution Information**
- **Fragmentation details** - how data is partitioned (horizontal/vertical/hybrid)
- **Replication information** - which data is replicated and where

**3. Access Control Information**
- User privileges and permissions
- Authorization rules for different sites
- Security policies

**4. Network Information**
- Site locations and addresses
- Communication costs between sites
- Network topology

### Example Usage

```
Query: SELECT * FROM Employee WHERE dept = 'Sales'

Catalog Manager provides:
- Employee table structure
- Fragmentation: horizontally fragmented by department
- Location: Sales dept data at Site B
- Statistics: ~500 sales employees
- Access rights: User has SELECT permission
```
