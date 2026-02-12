#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-SHA256 "$1" > /dev/null | john --show --format=Raw-SHA256 "$1" | awk -F: '{print $2}' > 6-password.txt
