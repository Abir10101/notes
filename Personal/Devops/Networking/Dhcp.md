# What is  DHCP (Dynamic Host Configuration Protocol) ?

## Introduction

Whenever a system connects to a network, it requires a unique public IP address to communicate with other machines. While manually configuring IP addresses is possible, it becomes impractical in large networks with hundreds of devices. To automate the allocation of unique IP addresses, even in vast networks like the Internet, DHCP was introduced.

## What is DHCP?

DHCP (Dynamic Host Configuration Protocol) is a network protocol that enables devices to automatically obtain network configuration parameters, primarily IP addresses, from a DHCP server.

## DHCP Architecture

The DHCP architecture comprises two main components:

- **DHCP Server:** A centralized entity responsible for managing a pool of available IP addresses and associated configuration parameters.
- **DHCP Client:** Software installed on network devices, such as computers, smartphones, and printers, that enables them to request and receive network configurations from a DHCP server.

## DHCP Operation

The DHCP process typically involves the following four steps:

1. **DHCP Discover:** When a DHCP client connects to a network, it broadcasts a DHCP Discover message to locate available DHCP servers.
2. **DHCP Offer:** DHCP servers on the network respond to the client's request with DHCP Offer messages, each containing an available IP address and other configuration parameters.
3. **DHCP Request:** The client selects an offer and sends a DHCP Request message to the corresponding server, requesting the offered IP address.
4. **DHCP Acknowledgment:** Upon receiving the client's request, the server reserves the requested IP address and sends a DHCP Acknowledgment message, confirming the lease to the client.

## IP Address Leasing and Renewal

To prevent IP address wastage when a device goes offline, DHCP servers assign IP addresses with a limited lease period. Clients are required to renew their leases before expiration. The renewal process typically occurs automatically in the background. If a client fails to renew its lease, the IP address is returned to the server's pool for reallocation.
