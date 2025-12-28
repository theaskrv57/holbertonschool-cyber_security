#!/bin/bash
whois "$1" | awk -F': ' 'BEGIN{s=""} /^Registrant /{s="Registrant"} /^Admin /{s="Admin"} /^Tech /{s="Tech"} /(Name|Organization|Street|City|State\/Province|Postal Code|Country|Phone:|Phone Ext:|Fax:|Fax Ext:|Email):/ && s!="" {k=$1; v=$2; if(k~/(Street)/)v=v" "; if(k~/(Phone Ext|Fax Ext)/)v=""; print s" "k","v}' > "$1.csv"
