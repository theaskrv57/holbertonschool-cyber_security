#!/bin/bash
whois "$1" | awk -F': ' '/Name:|Organization:|Street:|City:|State\/Province:|Postal Code:|Country:|Phone:|Phone Ext:|Fax:|Fax Ext:|Email:/ {gsub(/^[^:]+: /,""); print $1","$2}' > "$1.csv"
