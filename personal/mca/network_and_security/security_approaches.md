# Types of Attacks

## Malware
Malicious software crafted by hackers to disrupt systems, damage networks, and gain unauthorized access to steal private data. It is an "umbrella term" for any harmful software.

## Virus
Harmful software that requires human interaction (like clicking a link or opening an attachment) to replicate and spread by hitching a ride on legitimate files.

## Worm
Standalone programs that replicate and spread through networks independently by exploiting system flaws, without requiring human intervention.

## Man-in-the-middle
An attack where an intruder intercepts and alters private information as it travels between two devices, such as a user’s device and a server.

## DDoS
Distributed Denial of Service uses a "zombie army" of infected systems to flood a target server with traffic, causing it to malfunction or block access for legitimate users.

## Phishing
A deceptive trick where hackers send fake emails that look legitimate to fool people into giving away sensitive details like passwords and credit card info.

## IP Spoofing
A craft move where attackers falsify their computer's ID to pretend they are a trusted source, helping them sneak into a system unnoticed.

## Botnet
A team of infected computers controlled by a hacker to work together and attack multiple systems simultaneously.

## Trojan Horse
Malicious software disguised as a harmless application, such as a game, which gives attackers access to sensitive info once installed.

## Packet Sniffer
Tools that capture and save transmission packets in a network to intercept sensitive data like financial records and user IDs.

## Passive attack
Intercepting or eavesdropping on communication to gain unauthorized access to data without tampering with or altering the message.

## Active attack
Involves gaining access to data and directly modifying or tampering with the communication.

## Cryptographic Attack
Also known as "cryptanalysis," these attacks discover weaknesses in a system's code, cipher, protocol, or key management to bypass security.

### Brute force attack
Testing every possible key in the key range until the correct one is found.

### Ciphertext only attack
Deducing the original message by analyzing a collection of coded messages without direct access to the plaintext.

### Chosen plaintext attack
Attacker handpicks specific data to obtain the corresponding ciphertext, making it easier to find the key.

### Chosen ciphertext attack
Attacker links coded messages to the original ones to guess the key and obtain secret details.

### Known plaintext attack
Attacker uses knowledge of certain parts of the original plaintext to analyze the ciphertext.

### Dual key algorithm attack
Attacker attempts to recover the key by analyzing the mathematical cryptographic algorithm itself.

### Linear Cryptanalysis
Focuses on discovering "affine approximations" to exploit weaknesses in block ciphers.

### Differential Cryptanalysis
Tracks how differences in input information affect the output to identify non-random behavior and recover keys.

### RSA Signature Attacks
While RSA is highly secure, it can be targeted by specific mathematical attacks designed to forge digital signatures:
- **Chosen-message Attack**: The attacker convinces a user to sign two different messages and then combines those signatures to claim the user signed a third, forged message.
- **Key-only Attack**: The attacker uses only the publicly available key to try and generate a valid signature for a different message.
- **Known-message Attack**: The attacker attempts to forge a new signature by mathematically combining signatures from two or more existing messages they have already intercepted.


# Security Approaches

## Firewalls
These include **Packet Filters**, which check headers at the network layer, and **Application-level gateways** (bastion hosts), which inspect every layer of communication, including application data.

## Intrusion Prevention System (IPS)
Advanced tools that detect malware and monitor activity to identify malicious event chains and block them.

## VPN
Virtual Private Networks use **encrypted tunnels** to create secure paths for data over untrustworthy networks like the Internet.

## Network Access Control (NAC)
While not explicitly named "NAC" in the text, the sources describe **Authentication basics** (passwords, biometrics, tokens) and **Kerberos** as the primary ways to ensure only approved individuals access network services.

## Security Information and Event Management (SIEM)
The sources focus on **Logging and Auditing Transactions** to keep records for billing, conflict resolution, and investigating misuse.

## CIA model
The "CIA triad" represents the core objectives of network security: **Confidentiality** (authorized access only), **Integrity** (data accuracy), and **Availability** (reliable access).

## PGP (Pretty Good Privacy)
Developed by Phil Zimmermann, PGP is an open-source framework designed to provide comprehensive security—privacy, integrity, and authentication—for email communications. It combines the speed of symmetric encryption with the security of public-key cryptography through a multi-step process:
1.  **Signing**: The sender hashes the email and encrypts that hash with their own **private key** to create a digital signature.
2.  **Encryption**: The message and signature are encrypted together using a **one-time secret key** created by the sender.
3.  **Key Delivery**: This secret key is then encrypted using the **recipient's public key** and sent alongside the message.
4.  **Compatibility**: PGP also utilizes the **ZIP algorithm** for compression and **radix-64 encoding** to ensure the encrypted data is compatible with standard email systems.
