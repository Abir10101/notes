# Encryption

## Techniques

### Traditional techniques
- **Substitution Cipher Technique**: This method replaces characters with other letters, symbols, or units of text, changing their identity but keeping their original position in the string.
- **Transposition Cipher Technique**: This shifts the positions of characters to create a permutation of the original message. A common example is the **Rail Fence Cipher**, where plaintext is written in a zigzag pattern on imaginary "rails" and then read off in rows.

### Modern techniques
- **Stream Cipher technique**: Encrypts data one bit or byte at a time as it is sent. Because they can jumble and unjumble data "on the fly," they are ideal for live communication (e.g., the RC4 algorithm).
- **Block Cipher technique**: Processes data in fixed-size chunks or "blocks" (typically 64 or 128 bits). Examples include **DES** (56-bit key), **Triple DES**, and **AES**.
    - **Electronic Codebook (ECB), Cipher Block Chaining (CBC), Counter (CTR), and Output Feedback (OFB)**: These are the standard "modes of operation" for block ciphers used to determine how individual blocks are processed securely.

## Types
- **Symmetric Key encryption (Conventional algorithm)**: Uses a single secret key for both locking and unlocking data.
    - **Pros**: It is much faster and simpler to implement than asymmetric methods.
    - **Cons**: It is difficult to share keys securely and does not scale well for large numbers of users.
- **Asymmetric Key encryption (Public key encryption)**: Uses a mathematically related pair of keys—a **public key** for encryption and a **private key** for decryption.
    - **RSA**: A popular algorithm used for encryption and digital signatures; its security relies on the difficulty of factoring large prime numbers.
    - **Knapsack (Merkle-Hellman)**: An early asymmetric system using "super-increasing" integer sequences; while faster than RSA, it is now largely considered impractical due to vulnerabilities.

## Key management & distribution
- **Public announcement**: Users broadcast their public keys to everyone; however, this is risky as attackers can impersonate users.
- **Publicly available Directory**: Keys are stored in a trusted list with user details; though searchable, these lists remain vulnerable to tampering.
- **Public key authority**: A safer version of a directory where users check a secure list in real-time to obtain the correct keys.
- **Certification Authorities (CA)**: Trusted entities that issue **digital certificates** to confirm the identity of a website or individual. The CA signs the certificate with its own private key to ensure it is tamper-resistant.
- **Key Distribution Center (KDC)**: A centralized system that shares unique **session keys** for specific connections. It uses a "master key" hierarchy so that if one session key is stolen, the rest of the traffic remains secure.
- **Kerberos**: A security protocol that acts like a "security guard" using a KDC hub to provide **Single Sign-On (SSO)** and time-limited "tickets" for accessing network services.
- **Diffie-Hellman**: A protocol that allows two parties to establish a shared secret key safely over an insecure network even if they don't have a prior certificate.
- **Wireless Sensor Network (WSN) key distribution**: It used in sensors where the machines are tiny, low-powered devices, so standered public-key cryptography is too expensive for them. It uses "key redistribution", where secret keys are pre-installed into sensor nodes before they are deployed.
- **Group Key Management**: Used for inter-branch and intra-group networks; it often employs polynomial-based schemes and **Group Security Agents (GSA)** to manage keys between multiple departments.
- **Key Lifecycle & Compliance**: Key management must follow a lifecycle (generation, storage in **HSMs**, rotation, and destruction) and comply with standards like **PCI DSS** or **HIPAA**.
