# Authentication
Authentication is the process of verifying whether a person or information is who or what they claim to be, specifically confirming identity during system login.

## Techniques
- **Token Authentication**: Acting like a "VIP pass," once identity is proven, the user receives a unique token that allows them to access websites or apps without logging in again.
- **Password Authentication**: The "classic" method requiring a username and a secret code. Security is significantly enhanced by using "fancier" (complex) passwords and changing them frequently.
- **Biometric Authentication**: Uses the body as the password, such as fingerprints or unique iris patterns. The system performs a real-time check against files, making it both user-friendly and highly secure.
- **Certificate-Based Authentication**: Uses a "digital ID card" or certificate that is nearly impossible to fake without a secret key. It can verify the identity of the user, the device being used, or the specific service being accessed.

## Systems

### Kerberos

Kerberos is a "security guard" protocol developed by MIT that uses secret codes and a central hub called a **Key Distribution Center (KDC)** to verify identities on a network. Its main features include **Single Sign-On (SSO)**—allowing you to log in once for multiple services—and the use of time-limited "tickets" to prevent attackers from sneaking in later.

The **Kerberos Handshake** follows these steps to set up a secure session:
1.  **Request to Authentication Server (AS)**: Your computer starts by proving who you are to the AS.
2.  **Receive Ticket Granting Ticket (TGT)**: The AS hands you a TGT, which is locked using your secret password.
3.  **Request to Ticket Granting Server (TGS)**: When you need a specific service (like email), you show your TGT to the TGS.
4.  **Receive Service Ticket (ST)**: The TGS verifies your TGT and gives you an ST for that specific service, locked with that service's secret code.
5.  **Access Service**: You present the ST to the service, which confirms it with the AS to grant you a final secret key for your session.

### Multi-Factor Authentication (MFA)

MFA is described as "double trouble for intruders" because it requires two or more independent proofs of identity. It acts like having two locks on a door instead of one, significantly making it harder for unauthorized users to gain access even if they know your password.

### Public Key Infrastucture (PKI)

A framework that uses digital certificates issued by a trusted **Certificate Authority (CA)**. The CA investigates an entity's authenticity before signing a certificate with its own private key, ensuring that electronic communication is secure and the parties involved are legitimate.
