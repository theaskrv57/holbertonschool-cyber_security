#!/bin/bash
whois $1 | awk -F: '/Registrant|Admin|Tech/ {gsub(/^ /,"",$2); name=$1; val=$2; if(name~/Street/) val=val" "; if(name~/Phone$/) {print name","val; print name" Ext:,"} else if(name~/Fax$/) {print name","val; print name" Ext:,"} else print name","val}' > $1.csv
