
# OSI MODEL

- Lets say we have an an simple web application that returns a 'hello world' if we call a certain api from postman.
- Now the server might returns within a few miliseconds but there are many network processes that happened between the request and response. The request and response data both have to undergo same steps to reach the either servers.
- Imagine a person (let’s call him P1) is inside a room (R1), and he need to visit another room (R2). However, getting from R1 to R2 isn't as straightforward as just walking through a door. Inside Room R1, there are several layers, each with multiple doors. P1 has to choose a door in each layer. Once P1 goes through a door, he lock it behind him and take the key with him. After passing through all the layers and collecting all the keys, P1 exits Room R1. Now, when P1 arrives at Room R2, he encounter similar layers and doors, just like in Room R1. P1 has to use the keys he collected earlier, to unlock the exact doors in Room R2, in the same order as he did in Room R1. After that he can enter Room R2.
- In terms of networking,
	- **Person P1** represents the data.
	- **The layers** within the rooms are the OSI layers.
	- **The doors and keys** represent the protocols used at each layer.
	- **Room R1** is the sender's server, and **Room R2** is the receiver's server.
- All the networking concepts are not covered in the analogy but the purpose is to clear the basic idea.
- > **Defination of OSI model:**<br>
OSI model is a framework that standerizes the functions & protocols and the ordering of those functions of a networking system.
- The OSI model divides the network communication amoung 7 layers:
	- **Application (Layer 7):**<br>
	This is where end user's interaction happens. It provides functionalities like email, web browsing, file transfer.<br>
	**Protocols**: SMTP, HTTP, FTP, POP3, SNMP.
	- **Presentation (Layer 6):**<br>
	This is where data is encrypted, compressed and formatted.<br>
	**Protocols**: SSL, TLS, JPEG, MPEG
	- **Session (Layer 5):**<br>
	This layer establish, maintains & terminates connections. This layer is also handles the authentication and authorization of the connection. For example: When a user logs into a remote system using SSH (Secure Shell), the authentication happens at this layer. The SSH protocol verifies the user's identity (e.g., username and password) and establishes a secure session.<br>
	**Protocols**: SIP, PPTP, L2TP, H.245, SMB, NFS, PAP
	- **Transport (Layer 4):**<br>
	This layer divides larger data into smaller segments for transmission. It ensures that data is transmitted without errors. This is achieved through error detection mechanisms (like checksums) and retransmission of corrupted or lost segments. This layer is implemented by the OS and this layer also determines the delivery ports. This layer is also known as **heart of the OSI model**.<br>
	**Protocols**: TCP, UDP, SCTP, DCCP
	- **Network (Layer 3):**<br>
	This layer defines the IP address of both receiver & sender, and decides the best route for the data to be transmitted. It is implemented by the newtwork devices like routers and switches. Segments from transport layer is converted into Packets in this layer.<br>
	**Protocols**: IP, ICMP, ARP, IPsec, MPLS.
	- **Data Link (Layer 2):**<br>
	This layer is responsible for connection to local network devices. It performs various functions like:
		- The Data Link Layer encapsulates packets received from the Network Layer into frames. Each frame includes a header (containing source and destination addresses) and a trailer (often containing error-checking information).
		- Adds physical addresses (MAC addresses) to the frame headers ensuring that frames are delivered to the correct devices on a local network.
		- Flow control mechanisms are implemented to prevent a fast sender from overwhelming a slow receiver. Techniques such as stop-and-wait or sliding window protocols are commonly used for flow control.
		- It also manages how multiple devices share the same communication medium (e.g., wired or wireless networks). It implements protocols to avoid collisions when two devices attempt to transmit simultaneously.<br>
	**Protocols**: HDLC, LLDP, PPP, Ethernet, IEEE 802.11 (Wi-Fi)
	- **Physical (Layer 1):**<br>
	This is the actual layer which is responsible for devices to be physically connected. It is responsible for transmitting individual bits from one node to another. It defines how the data flows between the connected devices, possible modes of transmission are Simplex, half-duplex and full-duplex. This layer implements devices like Hub, Repeater, Modem, and Cables.<br>
	**Protocols**: Ethernet, IEEE 802.11 (Wi-Fi), Bluetooth, USB

# TCP/IP MODEL

- This model is similar to the OSI model but has only 4 layers.
	- **Application (Layer 4):**<br>
	This layer's responsibilities combines the Application Layer, Presentation Layer & Session Layer of the OSI model. That means, this layer implements the end-user applications (ex. email, browser, etc.), data encryption and compression & connection authentication and authorization.<br>
	**Protocols:** SMTP, HTTP, FTP, SSL, TLS, SIP, PPTP, L2TP.
	- **Transport (Layer 3):**<br>
	This layer has similar functionalities like the OSI model's Transport layer. This implements:
		- Divides the larger data into smaller chunks called segments.
		- **Connection type:** Connection-Oriented, Connectionless
		- Ensures the data is transmitted without errors and retransmission of corrupted or lost segments.<br>
	**Protocols:** TCP, UDP
	- **Network (Layer 2):**<br>
	This layer has similar functionalities like OSI model's Network layer. It implements the IP address of both the sender & receiver, and decides the best route to transmit the data.<br>
	**Protocols:** IP, ICMP, ARP, IPsec, MPLS.
	- **Network Access Layer:**<br>
	This layer combines the functionalities of Data Link Layer & Physical Layer of the OSI model. It handles the physical transmission of data over a network.<br>
	**Protocols:** HDLC, LLDP, Ethernet, IEEE 802.11 (Wi-Fi)









