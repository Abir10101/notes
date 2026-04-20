# Hashing
Hashing is a mathematical process that transforms an input message of any length into a fixed-length output string called a hash value or hash. It is primarily a one-way function, meaning it is easy to create a hash from a message but extremely difficult to reverse it. Its main purpose is to ensure **data integrity**; if a message is tweaked even slightly, the resulting hash value changes completely.

## Digital Signature
Digital signatures are electronic verifications used to confirm the **authenticity** of a message and ensure it hasn't been tampered with by third parties.
- **The Process**: The sender hashes the original message and encrypts that hash (the "digest") with their **private key**. 
- **Verification**: The recipient calculates their own hash of the message and uses the sender's **public key** to decrypt the signature. If the two hashes match, the message is confirmed to be genuine and unaltered.

## Algorithms
- **MD4**: Short for Message Digest Algorithm 4, it was created by Ronald Rivest in 1990. It transforms any amount of data into a 128-bit hash value, represented as a 32-character hexadecimal code.
- **MD5**: A successor to MD4, this algorithm also generates a 128-bit hash. While once popular, it is now considered **outdated and unsafe** for cryptographic use because it is vulnerable to "collision attacks," where two different inputs produce the same hash.
- **SHA-256**: Part of the Secure Hash Algorithm family, experts recommend using SHA-256 or SHA-3 for applications requiring robust security instead of MD5. 

Would you like to explore the specific **RSA signature attacks** mentioned in these modules, or should we move on to **Pretty Good Privacy (PGP)** for email security?
