
# OSI MODEL

- Lets say we have an an simple web application that returns a 'hello world' if we call a certain api from postman.
- Now the server might returns within a few miliseconds but there are many network processes that happened between the request and response. The request and response data both have to undergo same steps to reach the either servers.
- Lets say a person P1 is inside a room R1, and that person has to visit another room R2. Now it is not that simple to get out of that room R1 and visit the other room R2, there are some layers inside room R1 which he have to pass and each layer has many open doors from which he have to choose one door. Now, after crossing from one door he has to lock the door and take the key of that door with him. After getting out of all layers and collecting the keys he have to get inside the other room R2 which also has layers and and many doors similarly like room R1. Now using the collected keys he have to unlock the exact door in exact layer he choose from the previous room R1.
- In terms of networking, this doors & keys are basically protocols, person P1 is the data, layers are OSI layers & the rooms R1 & R2 is the servers, sender & receiver respectively. All the networking concepts are not covered in the hypothetical example but the purpose is to clear the basic idea.
- > **Defination of OSI model:**  
OSI model is a framework that standerizes the functions & protocols and the ordering of those functions of a networking system.
- The OSI model divides the network communication amoung 7 layers:
	- **Application (Layer 7):**  
	This is where end user's interaction happens. It provides functionalities like email, web browsing, file transfer.  
	**Protocols**: SMTP, HTTP, FTP, POP3, SNMP.
	- **Presentation (Layer 6):**  
	This is where data is encrypted, compressed and formatted.  
	**Protocols**: SSL, TLS, JPEG, MPEG
	- **Session (Layer 5):**  
	This layer establish, maintains & terminates connections. This layer is also handles the authentication and authorization of the connection. For example: When a user logs into a remote system using SSH (Secure Shell), the authentication happens at this layer. The SSH protocol verifies the user's identity (e.g., username and password) and establishes a secure session.  
	**Protocols**: SIP, PPTP, L2TP, H.245, SMB, NFS, PAP
	- **Transport (Layer 4):**  
	This layer divides larger data into smaller segments for transmission. It ensures that data is transmitted without errors. This is achieved through error detection mechanisms (like checksums) and retransmission of corrupted or lost segments. This layer is implemented by the OS and this layer also determines the delivery ports. This layer is also known as **heart of the OSI model**.  
	**Protocols**: TCP, UDP, SCTP, DCCP
	- **Network (Layer 3):**  
	This layer defines the IP address of both receiver & sender, and decides the best route for the data to be transmitted. It is implemented by the newtwork devices like routers and switches. Segments from transport layer is converted into Packets in this layer.  
	**Protocols**: IP, ICMP, ARP, IPsec, MPLS.
	- **Data Link (Layer 2):**  
	This layer is responsible for connection to local network devices. It performs various functions like:
		- The Data Link Layer encapsulates packets received from the Network Layer into frames. Each frame includes a header (containing source and destination addresses) and a trailer (often containing error-checking information).
		- Adds physical addresses (MAC addresses) to the frame headers ensuring that frames are delivered to the correct devices on a local network.
		- Flow control mechanisms are implemented to prevent a fast sender from overwhelming a slow receiver. Techniques such as stop-and-wait or sliding window protocols are commonly used for flow control.
		- It also manages how multiple devices share the same communication medium (e.g., wired or wireless networks). It implements protocols to avoid collisions when two devices attempt to transmit simultaneously.  
	**Protocols**: HDLC, LLDP, PPP, Ethernet, IEEE 802.11 (Wi-Fi)
	- **Physical (Layer 1):**  
	This is the actual layer which is responsible for devices to be physically connected. It is responsible for transmitting individual bits from one node to another. It defines how the data flows between the connected devices, possible modes of transmission are Simplex, half-duplex and full-duplex. This layer implements devices like Hub, Repeater, Modem, and Cables.  
	**Protocols**: Ethernet, IEEE 802.11 (Wi-Fi), Bluetooth, USB

