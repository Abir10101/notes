# Encryption

Encryption converts readable data (plaintext) into scrambled unreadable form (ciphertext) using mathematical algorithms and keys. Only party with correct key can decrypt back to original. Provides **confidentiality**—hides message content from unauthorized viewers.

---

## Encryption Types

### 1. Symmetric Key Encryption (Conventional)

Uses **single shared secret key** for both encryption and decryption. Sender encrypts with key; receiver decrypts with same key.

**Advantages**:
- Fast computation (100-1000x faster than asymmetric)
- Simple implementation
- Low overhead

**Disadvantages**:
- Key sharing problem — must safely transmit secret key through insecure network
- Poor scaling — each pair of users needs unique key (100 users = 4,950 keys needed)
- No non-repudiation — both parties have same key, cannot prove who sent message

**Techniques Used**:

#### Traditional Methods
- **Substitution Cipher**: Replace each character with different letter/symbol (e.g., Caesar cipher A→B, B→C)
- **Transposition Cipher**: Rearrange character positions (e.g., Rail Fence Cipher writes message in zigzag pattern, reads off in rows)

#### Modern Methods
- **Stream Cipher**: Encrypts one bit/byte at a time during transmission. Processes data "on the fly" as arrives. Good for live communication (RC4 algorithm)
- **Block Cipher**: Encrypts fixed-size data chunks (64 or 128 bits). Process entire block before moving to next. Examples: DES (56-bit), Triple DES, AES (128-256 bit)

**Block Cipher Modes of Operation** (determine how blocks processed securely):
- **ECB (Electronic Codebook)**: Each block encrypted independently
- **CBC (Cipher Block Chaining)**: Each block depends on previous block output
- **CTR (Counter)**: Uses counter value instead of data repetition
- **OFB (Output Feedback)**: Feedback of previous operation becomes input for next

---

### 2. Asymmetric Key Encryption (Public Key)

Uses **mathematically-related key pair**: public key for encryption, private key for decryption. Public key shareable; private key kept secret.

**Advantages**:
- Solves key sharing problem—public key broadcast openly, private key stays secret
- Enables digital signatures—proves sender identity
- Scales well—each user needs one pair regardless of communication partners
- Non-repudiation—sender cannot deny sending message (only they have private key)

**Disadvantages**:
- Computationally expensive (100-1000x slower than symmetric)
- Impractical for large data volumes
- Requires trusted method to verify public key belongs to correct person

**Algorithms**:

- **RSA (Rivest-Shamir-Adleman)**
  - Security based on difficulty of factoring large prime numbers
  - Used for both encryption and digital signatures
  - Standard in industry
  
- **Knapsack (Merkle-Hellman)**
  - Early asymmetric system using "super-increasing" integer sequences
  - Theoretically faster than RSA
  - Now impractical—discovered vulnerabilities make unsafe

---

## Key Management & Distribution

Secure communication requires getting encryption keys safely to intended recipient without compromise.

### Methods for Symmetric Keys

(Challenge: Both parties need identical key without exposing to network)

- **Key Distribution Center (KDC)**: Centralized trusted system. Generates unique session keys for each connection. Uses master key hierarchy so stealing one session key doesn't compromise others
- **Kerberos**: Security protocol using KDC. Provides Single Sign-On (SSO)—log in once, access multiple services. Uses time-limited "tickets" preventing replay attacks
- **Pre-shared out-of-band**: Exchange keys through secure offline channel before communication

### Methods for Public Keys

(Challenge: Must verify public key truly belongs to intended recipient, not attacker)

- **Public announcement**: Broadcast public key to everyone. **Risk**: Attackers impersonate you by claiming your key
- **Publicly available Directory**: Centralized list storing keys with user details. Searchable but **vulnerable to tampering**
- **Public Key Authority**: Trusted directory. Users query real-time to get correct keys. Safer than directory but still requires trusting the authority
- **Certification Authorities (CA)**: Trusted entities issue **digital certificates** binding public key to identity. CA signs certificate with its own private key making tamper-proof. Standard in HTTPS/SSL
- **Diffie-Hellman Protocol**: Two parties establish shared secret key safely over insecure network without pre-sharing anything. Both parties combine public and private values to derive same shared secret

### Specialized Scenarios

- **Wireless Sensor Networks (WSN)**: Standard public-key cryptography too expensive for tiny, low-powered sensors. Uses pre-installed secret keys distributed to nodes before deployment
- **Group Key Management**: Multiple departments/branches need shared encryption keys. Uses polynomial-based schemes and **Group Security Agents (GSA)** to manage keys across groups
- **Key Lifecycle & Compliance**: Professional environments follow complete lifecycle: generation → storage in HSM (Hardware Security Module) → periodic rotation → secure destruction. Must comply with standards (PCI DSS, HIPAA, etc.)
