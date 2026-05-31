# Deadlock in Distributed DBMS: Scenarios, Prevention & Recovery

## What is Deadlock?

A deadlock occurs when two or more transactions are circularly waiting for each other to release locks, and none can proceed. In a **Distributed DBMS (DDBMS)**, this becomes more complex because transactions span multiple sites/nodes, making detection and resolution significantly harder.

---

## The Classic Deadlock Scenario

Imagine a banking system distributed across two sites:

**Site A** holds account data for *Customer X*
**Site B** holds account data for *Customer Y*

Two transactions start simultaneously:

```
Transaction T1 (Transfer from X → Y):          Transaction T2 (Transfer from Y → X):
─────────────────────────────────────          ─────────────────────────────────────
1. Lock X at Site A          ✅ (granted)      1. Lock Y at Site B          ✅ (granted)
2. Lock Y at Site B          ⏳ (waiting...)   2. Lock X at Site A          ⏳ (waiting...)
```

**Result:** T1 holds the lock on X and waits for Y. T2 holds the lock on Y and waits for X. Neither can ever proceed — **deadlock**.

In a **centralized DBMS**, a single lock manager can easily detect circular waits. In a distributed system, each site manages its own locks, making it harder to detect deadlocks.

---

## Detection Approaches

### 1. Centralized Detection
One designated site (the **coordinator**) collects wait-for graph information from all sites and checks for cycles.

**Drawback:** The coordinator itself becomes a bottleneck or single point of failure.

### 2. Distributed Detection (Chang-Roberts style)
Each site sends local wait-for information along a logical ring. If a message travels the full ring and returns to the originator, a cycle (deadlock) exists.

### 3. Timeout-Based Detection
If a transaction waits longer than a threshold (e.g., 5 seconds), the system **assumes** a deadlock and aborts it.

**Drawback:** May abort transactions that are simply slow, not actually deadlocked (false positives).

---

## Prevention Strategies

Prevention eliminates deadlock *before* it can occur, so no detection is ever needed.

### 1. Wait-Die Scheme (Age-based)
Older transactions wait. Younger ones always die. The circular wait condition can never form.

```
T1 requests a lock held by T2.
- If T1 is older than T2 -> T1 WAITS
- If T1 is younger than T2 -> T1 DIES
```

### 2. Wound-Wait Scheme (also Age-based, reversed)
Younger transactions wait. Older ones always preempt.

```
T1 requests a lock held by T2.
- If T1 is older than T2 -> T1 WOUNDS T2 (forces T2 to roll back) so T1 can proceed
- If T1 is younger than T2 -> T1 WAITS
```

### 3. Lock Ordering (Resource Ordering)
Assign a global order to all resources (e.g., tables/rows get IDs). Every transaction must acquire locks **in ascending order** of resource IDs, regardless of which site holds them.

```
Resources:  Account_X (ID=1)   Account_Y (ID=2)

T1 and T2 must both lock ID=1 first, then ID=2.
→ One will get ID=1 first, the other waits. No cycle possible.
```

This is simple and effective but requires careful coordination in a distributed setting.

---

## Recovery After Deadlock (Victim Selection)

Once a deadlock is detected, the system must **choose a victim** to abort. Common criteria:

| Criterion | Description |
|---|---|
| **Minimum cost** | Abort the transaction that has done the least work so far |
| **Minimum rollback** | Abort the one with the fewest changes to undo |
| **Youngest transaction** | Abort the most recently started one (aligns with Wait-Die) |
| **Fewest locks held** | Abort the one holding the fewest resources |

The victim is **rolled back**, its locks are released, and it may be **restarted** later.

---

## Full Worked Example

A distributed e-commerce system with three sites:

```
Site A: Product inventory    Site B: Customer accounts    Site C: Order records

T1: "Place order for Customer 1 buying Product 10"
    → Lock Product_10 (Site A) ✅
    → Lock Customer_1 (Site B) ⏳ waiting...

T2: "Apply discount to Customer 1 on Product 10"
    → Lock Customer_1 (Site B) ✅
    → Lock Product_10 (Site A) ⏳ waiting...

          ┌──────── T1 waits for ────────┐
          ↓                              ↑
   [ Customer_1 ]              [ Product_10 ]
          ↑                              ↓
          └──────── T2 waits for ────────┘
                    DEADLOCK!
```

**Using Wait-Die to prevent this (if timestamps were enforced):**
- T1 (timestamp 100), T2 (timestamp 200)
- T2 is younger and wants a lock held by T1 → T2 **dies** (aborts)
- T1 proceeds, completes, releases locks
- T2 restarts with a new timestamp and completes without conflict

---

## Summary

| Technique | Type | Handles DDBMS? | Tradeoff |
|---|---|---|---|
| Timeout | Detection | Yes (simple) | False positives possible |
| Centralized wait-for graph | Detection | Limited | Single point of failure |
| Distributed wait-for graph | Detection | Yes | Communication overhead |
| Wait-Die | Prevention | Yes | Young transactions may restart often |
| Wound-Wait | Prevention | Yes | Young transactions may be aborted unfairly |
| Lock Ordering | Prevention | Yes | Requires global resource ordering |
