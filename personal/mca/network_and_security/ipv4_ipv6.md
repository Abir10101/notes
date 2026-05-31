# IPv4 and IPv6

## IPv4 (Internet Protocol version 4)

### Address Format

32-bit address divided into 4 octets. Each octet = 8 bits (0-255 decimal).

**Format**: `192.168.1.1`

**Range**: 0.0.0.0 to 255.255.255.255

**Total addresses**: 2^32 = 4,294,967,296 addresses (~4.3 billion)

### Address Classes

| Class | Range | Purpose | Hosts per Network |
|-------|-------|---------|-------------------|
| A | 1.0.0.0 - 126.255.255.255 | Large networks | 16.7 million |
| B | 128.0.0.0 - 191.255.255.255 | Medium networks | 65,534 |
| C | 192.0.0.0 - 223.255.255.255 | Small networks | 254 |
| D | 224.0.0.0 - 239.255.255.255 | Multicast | N/A |
| E | 240.0.0.0 - 255.255.255.255 | Reserved | N/A |

### IPv4 Limitations

1. **Address exhaustion**: 4.3 billion addresses insufficient for modern devices (IoT, mobile, cloud)
2. **No built-in security**: Authentication/encryption bolted on later (IPsec optional)
3. **No quality of service**: Cannot prioritize traffic types natively
4. **No built-in mobility**: Difficult for roaming devices to maintain connections
5. **Fragmentation issues**: Inefficient packet handling when sizes don't match
6. **No auto-configuration**: Manual setup required or DHCP needed
7. **Header complexity**: 20-60 byte header with variable options

---

## IPv6 (Internet Protocol version 6)

### Address Format

128-bit address divided into 8 groups of 16-bit hexadecimal numbers.

**Format**: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

**Compressed format**: `2001:db8:85a3::8a2e:370:7334` (consecutive zeros = ::)

**Range**: 0:0:0:0:0:0:0:0 to ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff

**Total addresses**: 2^128 = 340,282,366,920,938,463,463,374,607,431,768,211,456 addresses (~340 undecillion)

### Address Structure

```
2001 : 0db8 : 85a3 : 0000 : 0000 : 8a2e : 0370 : 7334
├─┬──┘ ├─┬──┘ ├─┬──┘ ├─┬──┘ ├─┬──┘ ├─┬──┘ ├─┬──┘ ├─┬──┘
  │      │      │      │      │      │      │      │
Global  Site   Subnet Host identifier bits
Prefix  Routing  ID
```

### IPv6 Address Types

- **Unicast**: One sender to one recipient (most common)
- **Multicast**: One sender to multiple recipients (224::/4)
- **Anycast**: One sender to nearest recipient in group

---

## IPv6 Advantages Over IPv4

### 1. Address Space

| Aspect | IPv4 | IPv6 |
|--------|------|------|
| Address size | 32-bit | 128-bit |
| Total addresses | 4.3 billion | 340 undecillion |
| Addresses per person | ~0.5 | ~42 billion |

**Impact**: Every device gets unique public IP. No shortage. No NAT needed.

### 2. Built-in Security (IPsec)

IPsec mandatory in IPv6, optional in IPv4.

- Authentication Header (AH) verifies sender identity
- Encapsulating Security Payload (ESP) encrypts data
- Prevents tampering, eavesdropping natively

### 3. Auto-Configuration

IPv6 devices self-configure address without DHCP.

- Link-local address auto-generated from MAC address
- Global address from network prefix + auto-generated suffix
- Plug-and-play networking

### 4. Quality of Service (QoS)

- Traffic class field (8 bits) prioritizes traffic types
- Flow label field marks packets belonging same stream
- Routers handle priority natively (video > email)

### 5. Simplified Header

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Header size | 20-60 bytes | Fixed 40 bytes |
| Header complexity | Variable options | Fixed fields |
| Fragmentation | Router can fragment | Only source fragments |
| TTL/Hop limit | 8 bits | 8 bits (same logic) |

**Impact**: Faster processing. Simpler routers.

### 6. Better Routing

- Hierarchical address structure built-in
- Smaller routing tables (aggregation by design)
- More efficient packet forwarding

### 7. Improved Multicast

- Multicast replacing broadcast (reduces network noise)
- Cleaner address allocation
- Better for streaming, group communication

### 8. Mobility Support

- MIPv6 (Mobile IP for IPv6) seamless handoff
- Devices maintain connection while roaming between networks
- No lost sessions when switching WiFi

### 9. No NAT Required

- Sufficient addresses = every device gets public IP
- Direct communication between devices
- End-to-end connectivity restored
- Simplifies P2P applications, gaming, IoT

### 10. Flow Labeling

- 20-bit flow label field groups packets
- Router recognizes packet streams
- Enables Quality of Service without deep packet inspection

---

## Comparison Table

| Feature | IPv4 | IPv6 | Winner |
|---------|------|------|--------|
| Address space | 4.3 billion | 340 undecillion | IPv6 |
| Security | Optional (IPsec) | Mandatory (IPsec) | IPv6 |
| QoS | No native support | Traffic Class + Flow Label | IPv6 |
| Auto-config | Requires DHCP | Stateless (SLAAC) | IPv6 |
| Header size | 20-60 bytes | Fixed 40 bytes | IPv6 |
| Fragmentation | Router can fragment | Source only | IPv6 |
| Routing efficiency | Good | Excellent | IPv6 |
| Multicast | Limited | Standard | IPv6 |
| Mobility | Difficult | Native (MIPv6) | IPv6 |
| NAT required | Yes | No | IPv6 |
| Deployment | 100% | ~50% (as of 2024) | IPv4 (legacy) |
