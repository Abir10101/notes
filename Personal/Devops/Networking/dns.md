
# Domain Name System (DNS)

- DNS is a system for mapping IP Addresses with names. It helps us with providing human friendly names instead of IP numbers to remember.
- After deploying our server in AWS EC2 server, it provides us with a ipv4 address. Then we have to buy a domain from a domain provider like Godaddy or Cloudflare. Then maps the domain with the ipv4 address.
- Now, when I hit the domain example.com in browser, the browser does not directly connects with the IP Address by resolving the DNS, as it does not knows the ip mapping for that domain.
- The request first went to the Internet Service Provider (ISP), who provides a certain type of nameserver called Recursive Nameserver or DNS Resolver. The DNS Resolver server will then query the Root Nameserver of the domain which returns the IP of TLD Nameservers (.com, .in, etc.).
- The TLD nameserver returns the IP of Authoratative Nameserver. The Authoratative Nameserver is the server where I first configured the mappings for the IP Address with the domain name. So, on querying this nameserver the DNS Resolver gets the IP Address.
- Then the DNS Resolver caches the IP Address for future requests and returns the IP Address to the user's browser. The browser then connects with the IP and exchange data.
- DNS works at Application (layer 7) of the OSI Model.
- Nameservers are different type of servers that functions to resolve domain name with IP Address.
- Authoratative Nameserver is responsible storing the mapping of IP Address with domain name.
- Recursive Nameserver is responsible for recursively finding the Authoratative Namesever, query it & gets the server's IP Address.
