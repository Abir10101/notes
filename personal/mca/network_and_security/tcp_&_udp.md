# TCP & UDP

---

## Socket

**Definition:** IP Address + Port + Protocol (TCP/UDP)

A socket is a concrete endpoint for communication with state.

**Server:** Binds to port → Listens for connections  
**Client:** Connects to IP:Port → Gets ephemeral port

```
(192.168.1.10, 54321, TCP) ←→ (10.0.0.1, 8080, TCP)
   Client Socket                    Server Socket
```

---

## UDP

- **Connectionless:** No handshake before sending datagrams
- **No state:** No connection tracking, supports more clients
- **Low overhead:** 8 bytes per segment
- **Use case:** DNS, VoIP, streaming

---

## TCP

### Background
- Designed by Vinton Cerf & Robert Kahn (1974)
- Goal: interconnect different networks with a common protocol
- Split from single TCP/IP into TCP and IP as separate layers
- Received ACM Turing Award (2004) for this work

### Key Features
- **Connection-oriented:** Handshake before data transfer
- **Full-duplex:** Bidirectional data flow simultaneously
- **Point-to-point:** Exactly two endpoints (no multicasting)
- **Reliable:** Ordered, error-checked delivery

### Three-Way Handshake

```
Client                              Server
 │                                    │
 │─────────── SYN (seq=x) ──────────►│  Step 1: Client initiates
 │                                    │
 │◄──────── SYN-ACK (seq=y, ack=x+1) │  Step 2: Server responds
 │                                    │
 │─────────── ACK (ack=y+1) ────────►│  Step 3: Connection established
 │                                    │
 ═══════════ DATA FLOW ═══════════════
```

**States:**
- Client: `SYN_SENT` → `ESTABLISHED`
- Server: `SYN_RECEIVED` → `ESTABLISHED`

**Sequence:**
1. Client sends SYN with initial sequence number `x`
2. Server replies SYN+ACK with sequence `y`, acknowledges `x+1`
3. Client sends ACK acknowledging `y+1`
