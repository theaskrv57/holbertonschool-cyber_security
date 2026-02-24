# Nmap Live Hosts Discovery

This project focuses on network host discovery techniques using Nmap and low-level scanning methodologies in a controlled lab environment.

## Project Overview

The tasks in this directory explore multiple techniques for identifying live hosts within a network:

- ARP scanning
- ICMP echo requests
- ICMP timestamp requests
- ICMP address mask requests
- TCP SYN ping
- TCP ACK ping
- UDP ping scanning

The objective of this project was to understand how network discovery works at the protocol level and how attackers and defenders identify active systems on a network.

⚠️ All scans were conducted in an isolated lab environment for educational and ethical purposes only.

## Files Description

- 0-arp_scan.sh: Performs ARP-based host discovery.
- 1-icmp_echo_scan.sh: Uses ICMP echo requests to identify live hosts.
- 2-icmp_timestamp_scan.sh: Uses ICMP timestamp requests.
- 3-icmp_address_mask_scan.sh: Uses ICMP address mask requests.
- 4-tcp_syn_ping.sh: Performs TCP SYN-based host discovery.
- 5-tcp_ack_ping.sh: Uses TCP ACK packets for host detection.
- 6-udp_ping_scan.sh: Uses UDP-based probing for discovery.
- Flag files: Lab validation artifacts.

## Technologies Used

- Nmap
- Bash scripting
- TCP/IP protocols
- ICMP protocol
- ARP protocol

## Key Concepts Practiced

- Network reconnaissance
- Host discovery techniques
- Packet-level understanding
- Firewall evasion basics
- Protocol behavior analysis
- Ethical scanning practices

## Author

Sahil Asgarov
