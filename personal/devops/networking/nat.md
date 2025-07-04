# NAT Gateway: A Comprehensive Guide for Network Engineers

## 1. Basic Concept

Network Address Translation (NAT) is a method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device. A NAT gateway is a network device that performs this translation.

The primary purposes of NAT are:
- To conserve public IPv4 addresses
- To improve security by hiding the internal network structure
- To enable communication between private networks and the public internet

## 2. Types of NAT

### 2.1 Static NAT
- One-to-one mapping between a private and a public IP address
- Useful for servers that need a consistent public IP address

### 2.2 Dynamic NAT
- Maps private IP addresses to a pool of public IP addresses
- Useful when you have more private IPs than public IPs, but not all devices need simultaneous internet access
- Example: 100 private IPs might share a pool of 10 public IPs

### 2.3 Port Address Translation (PAT) / Network Address Port Translation (NAPT)
- Many-to-one mapping, also known as IP masquerading
- Multiple private IP addresses share a single public IP address
- Distinguishes between different internal hosts by using port numbers
- Example: Most common type used in home routers and small businesses

## 3. NAT Gateway Components

A typical NAT gateway consists of:
1. At least two network interfaces (internal and external)
2. NAT translation table
3. Packet inspection and modification engine
4. Routing capabilities

## 4. NAT Process

1. An internal host sends a packet to an external destination
2. The NAT gateway receives the packet
3. It modifies the source IP address & port in the packet header
4. It creates an entry in its NAT table
5. The modified packet is sent to the destination
6. When a response is received, the NAT gateway uses its table to determine the original sender and forwards the packet accordingly

## 5. NAT Table

The NAT table typically includes:
- Original source IP and port
- Translated source IP and port
- Destination IP and port
- Protocol (TCP/UDP)
- Timestamp for entry expiration

## 6. NAT archietecture of Routers

```
Internet 
    ↕
ISP's DHCP Server (assigns public IP: 203.0.113.1)
    ↕
Router/NAT Gateway
    ↕
Local DHCP Server (inside router, assigns private IPs)
    ↕
Devices (get private IPs: 192.168.x.x)
```

1. Router's external network interface gets public IP Address from ISP's DHCP server and goes online in internet.
2. Router's internal network interface used its local DHCP server & assigns private IPs to local devices.
3. Router does the NAT Process for mapping local devices with internet.
4. So, the router will act as a NAT gateway in this scenaio.

## 7. NAT in IPv6

While IPv6 reduces the need for NAT due to its large address space, NAT is still used in IPv6 networks for:
- IPv4 to IPv6 translation (NAT64)
- Network renumbering
- Multihoming scenarios
