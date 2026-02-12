#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=NT "$1" > /dev/null | john --show --format=NT "$1" | awk -F: '{print $2}' > 5-password.txt
