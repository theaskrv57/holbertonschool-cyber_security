#!/bin/bash

# Remove {xor} prefix
hash="${1#\{xor\}}"

# Base64 decode and XOR with 0x5F
echo "$hash" | base64 -d | while IFS= read -r -n1 char; do
    printf "\\$(printf '%03o' "$(( $(printf '%d' "'$char") ^ 0x5F ))")"
done
echo
