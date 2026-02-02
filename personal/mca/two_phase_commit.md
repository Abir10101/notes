## Two-Phase Commit Protocol (2PC) in DDBMS

The **Two-Phase Commit Protocol** is a distributed algorithm that ensures all participating databases in a distributed transaction either commit or abort together, maintaining ACID properties across multiple sites.

### How It Works

**Phase 1: Prepare Phase (Voting Phase)**
1. **Coordinator** sends a "prepare to commit" message to all participating sites
2. Each **participant** (database node):
   - Executes the transaction locally
   - Writes transaction to its local log
   - Locks affected resources
   - Responds with "ready to commit" (YES vote) or "abort" (NO vote)
3. Coordinator collects all votes

**Phase 2: Commit Phase (Decision Phase)**
1. **If all votes are YES:**
   - Coordinator sends "commit" message to all participants
   - Each participant commits the transaction permanently
   - Participants release locks and send acknowledgment
   
2. **If any vote is NO:**
   - Coordinator sends "abort" message to all participants
   - Each participant rolls back the transaction
   - Participants release locks and send acknowledgment

### Example Scenario
```
Transaction: Transfer $100 from Bank A to Bank B

Phase 1:
- Coordinator → Bank A: "Can you deduct $100?"
- Coordinator → Bank B: "Can you add $100?"
- Bank A → Coordinator: "YES, ready"
- Bank B → Coordinator: "YES, ready"

Phase 2:
- Coordinator → All: "COMMIT"
- Both banks finalize the transaction
```

### Advantages
- **Guarantees atomicity** across distributed sites
- **Data consistency** maintained globally
- **Reliable** for critical transactions

### Disadvantages
- **Blocking protocol** - participants wait for coordinator's decision
- **Single point of failure** - coordinator crash can block entire system
- **High latency** - requires multiple round-trip communications
- **Resource locking** - locks held throughout both phases (performance impact)
- **Not partition-tolerant** - network failures can cause indefinite blocking

### States in 2PC
- **Initial state** - Transaction begins
- **Prepared state** - Participant ready to commit
- **Committed state** - Transaction finalized
- **Aborted state** - Transaction rolled back
