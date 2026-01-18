#!/bin/bash

# Remove {xor} prefix
hash="${1#\{xor\}}"

# Decode Base64 and XOR each byte with 0x23
echo "$hash" | base64 -d | while IFS= read -r -n1 c; do
    printf "\\$(printf '%03o' $(( $(printf '%d' "'$c") ^ 0x23 )))"
done
