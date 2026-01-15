# Object-Oriented Database Management Systems (OODBMS)

## Key Characteristics

### 1. Direct Object Persistence
OODBMS allows storing class objects directly without transformation. Complex objects with nested relationships can be persisted in their natural form.

**Example:**
```java
class Person {
  int id;
  String name;
}

class Student {
  int id;
  Person person;
}
```

In OODBMS, the `person` attribute within the `Student` object is stored as-is, maintaining the object reference and structure.

**Contrast with RDBMS:**
In relational databases, you would need to:
- Create separate tables for `Student` and `Person`
- Define a foreign key in the `Student` table referencing the `Person` table
- Manually manage the relationship through join operations

### 2. Object-Oriented Programming Support
OODBMS natively supports OOP concepts, including:

- **Encapsulation:** Objects maintain their data and methods together
- **Inheritance:** Class hierarchies are preserved in the database
- **Polymorphism:** Objects can be stored and retrieved with their behavioral characteristics intact
- **Abstraction:** Complex data types and relationships are handled naturally

This eliminates the **object-relational impedance mismatch** that occurs when mapping object-oriented code to relational database schemas.

## Multiversion Concurrency Control (MVCC) - Summary

### Core Concept

**MVCC allows multiple transactions to access the same data simultaneously by maintaining multiple versions of each data item.** Instead of locking data, each transaction gets its own consistent snapshot of the database.

### How It Works

```
# Database state over time
Time T0: Account balance = $1000 (Version 1)

# T1: Transaction A starts - gets snapshot
Transaction A: sees balance = $1000

# T2: Transaction B updates balance
Transaction B: balance = $1000 + $500 = $1500
              Creates Version 2

# T3: Transaction A still reading
Transaction A: still sees $1000 (its snapshot - Version 1)

# T4: Transaction C starts
Transaction C: sees $1500 (latest - Version 2)

# All three transactions work simultaneously!
```

**Key Principle**: Readers read old versions, writers create new versions - no one blocks anyone.

### Traditional Locking vs MVCC

#### Traditional Locking

```python
# Transaction 1: Generate monthly report
db.lock(accounts)          # 🔒 Lock all accounts
for account in accounts:
    calculate_interest()   # Takes 30 seconds
db.unlock(accounts)        # 🔓 Release lock

# Transaction 2: User checks balance
db.lock(account)           # ⏳ BLOCKED! Waits 30 seconds
balance = account.balance  
db.unlock(account)

# Transaction 3: Deposit money
db.lock(account)           # ⏳ BLOCKED! Waits...
account.balance += 100
db.unlock(account)
```

**Problem**: Long-running reads block all other operations.

#### MVCC

```python
# Transaction 1: Generate monthly report
snapshot = db.snapshot(T1)    # ✅ Get snapshot instantly
for account in snapshot:
    calculate_interest()      # Takes 30 seconds, no locks!

# Transaction 2: User checks balance (runs simultaneously)
snapshot = db.snapshot(T2)    # ✅ Get latest snapshot
balance = account.balance     # ✅ No waiting!

# Transaction 3: Deposit money (runs simultaneously)
account.balance += 100        # ✅ Creates new version
db.commit()                   # ✅ No waiting!
```

**Solution**: All operations proceed without blocking.

### Key Advantages

- Readers Don't Block Writers & Writers Don't Block Readers
- Consistent Snapshots
- Higher Concurrency
