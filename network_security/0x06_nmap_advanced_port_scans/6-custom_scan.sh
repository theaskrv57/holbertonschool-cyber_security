#!/bin/bash
sudo nmap --scanflags FIN,SYN,RST,PSH,ACK,URG -p "$2" "$1" > custom_scan.txt 2>&1
