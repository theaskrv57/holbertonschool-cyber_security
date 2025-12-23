#!/usr/bin/env bash

# Usage: ./0-whois.sh domain.com
# Output: domain.com.csv

whois "$1" | awk '
BEGIN {
    ORS=""
    first=1
}

/^(Registrant|Admin|Tech) / {
    section=$1
}

function print_csv(field, value) {
    if (!first) printf "\n"
    first=0
    printf "%s %s,%s", section, field, value
}

section != "" {
    if ($0 ~ /Name:/) {
        sub(/.*Name:[ \t]*/, "", $0)
        print_csv("Name", $0)
    }
    else if ($0 ~ /Organization:/) {
        sub(/.*Organization:[ \t]*/, "", $0)
        print_csv("Organization", $0)
    }
    else if ($0 ~ /Street:/) {
        sub(/.*Street:[ \t]*/, "", $0)
        print_csv("Street", $0 " ")
    }
    else if ($0 ~ /City:/) {
        sub(/.*City:[ \t]*/, "", $0)
        print_csv("City", $0)
    }
    else if ($0 ~ /State\/Province:/) {
        sub(/.*State\/Province:[ \t]*/, "", $0)
        print_csv("State/Province", $0)
    }
    else if ($0 ~ /Postal Code:/) {
        sub(/.*Postal Code:[ \t]*/, "", $0)
        print_csv("Postal Code", $0)
    }
    else if ($0 ~ /Country:/) {
        sub(/.*Country:[ \t]*/, "", $0)
        print_csv("Country", $0)
    }
    else if ($0 ~ /Phone Ext:/) {
        sub(/.*Phone Ext:[ \t]*/, "", $0)
        print_csv("Phone Ext:", $0)
    }
    else if ($0 ~ /Phone:/) {
        sub(/.*Phone:[ \t]*/, "", $0)
        print_csv("Phone", $0)
    }
    else if ($0 ~ /Fax Ext:/) {
        sub(/.*Fax Ext:[ \t]*/, "", $0)
        print_csv("Fax Ext:", $0)
    }
    else if ($0 ~ /Fax:/) {
        sub(/.*Fax:[ \t]*/, "", $0)
        print_csv("Fax", $0)
    }
    else if ($0 ~ /Email:/) {
        sub(/.*Email:[ \t]*/, "", $0)
        print_csv("Email", $0)
    }
}
' > "$1.csv"
