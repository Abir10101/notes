# Setting Up a DHCP Server and Client Using Docker: A Comprehensive Guide

In this guide, we'll walk through the process of setting up a DHCP (Dynamic Host Configuration Protocol) server and client using Docker containers. This setup is useful for learning about DHCP, testing network configurations, or simulating network environments.

## Prerequisites

- Docker installed on your system
- Basic knowledge of Docker and networking concepts

## Part 1: Setting Up the DHCP Server

### Step 1: Pull the Alpine Docker Image

We'll use the Alpine Linux image for both our DHCP server and client due to its small size and simplicity.

```sh
docker pull alpine:latest
```

### Step 2: Create an Isolated Network

To keep our DHCP environment separate from your host machine's network, we'll create a dedicated Docker network.

```sh
docker network create dhcp-net
```

### Step 3: Run the DHCP Server Container

Now, let's create and run our DHCP server container:

```sh
docker run --name server --network dhcp-net --cap-add=NET_ADMIN -it --expose 67 alpine:latest sh
```

Note: We use `--cap-add=NET_ADMIN` to give the container the necessary network administration capabilities, and we expose port 67, which is the standard port for DHCP communication.

### Step 4: Install DHCP Server Software

Enter the server container:
```sh
docker exec -it server sh
```

Inside the server container, install the DHCP server package and some useful tools:

```sh
apk add --no-cache dhcp nano
```

### Step 5: Gather Network Information

To configure our DHCP server correctly, we need to know the network details. Open a new terminal and run this command on your host machine:
```sh
docker network inspect dhcp-net
```

Look for the "Subnet" and "Gateway" information in the output. You'll need these for the next step.

### Step 6: Configure the DHCP Server

Inside the server container, navigate to the DHCP configuration directory and create a new configuration file:

```sh
cd /etc/dhcp
touch dhcpd.conf
nano dhcpd.conf
```

Add the following configuration, replacing the subnet and router IP with the values of `Subnet` and `Gateway` respectively you found in Step 5:

```
default-lease-time 600;
max-lease-time 7200;
authoritative;

subnet 172.18.0.0 netmask 255.255.255.0 {
  range 172.18.0.100 172.18.0.200;
  option routers 172.18.0.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
}
```

This configuration:

- Sets the default lease time to 10 minutes (600 seconds)
- Sets the maximum lease time to 2 hours (7200 seconds)
- Defines the subnet and IP range for DHCP clients
- Specifies the default gateway (router) and DNS servers

### Step 7: Start the DHCP Server

Still inside the server container, start the DHCP server:

```sh
dhcpd -f -d --no-pid
```

You should see output indicating that the server has started successfully.

## Part 2: Setting Up the DHCP Client

### Step 1: Create a Client Container

Open a new terminal window and create a client container:

```sh
docker run --name client1 -it --network dhcp-net --cap-add=NET_ADMIN alpine:latest sh
```

### Step 2: Install DHCP Client Software

Inside the client container, install the DHCP client:

```sh
apk add --no-cache dhclient
```

### Step 3: Release the Current IP Address

Check the current IP address:

```sh
ifconfig
```

You'll see that Docker has assigned an IP address. We need to release this to test our DHCP server:

```sh
ip addr flush dev eth0
```

Verify that the IP address has been removed:

```sh
ifconfig
```

### Step 4: Request an IP from the DHCP Server

Now, let's request an IP address from our DHCP server:

```sh
dhclient -v
```

### Step 5: Verify the New IP Address

Check the new IP address:

```sh
ifconfig
```

You should see an IP address in the range we specified in the DHCP server configuration (172.18.0.100 - 172.18.0.200).

## Conclusion

Congratulations! You've successfully set up a DHCP server and client using Docker containers. This setup demonstrates how DHCP works in a controlled environment. You can expand on this by adding more clients or modifying the DHCP configuration to explore different scenarios.

Remember to clean up your Docker resources when you're done:

```sh
docker stop server client1
docker rm server client1
docker network rm dhcp-net
```

This guide provides a foundation for understanding DHCP in containerized environments. Feel free to experiment and learn more about network configuration and management using this setup.