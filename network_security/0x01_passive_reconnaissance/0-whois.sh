#!/usr/bin/env bash
whois "$1" | awk 'BEGIN{ORS="";f=1}/^(Registrant|Admin|Tech) /{s=$1}/Name:|Organization:|Street:|City:|State\/Province:|Postal Code:|Country:|Phone Ext:|Phone:|Fax Ext:|Fax:|Email:/{if(!f)printf "\n";f=0;sub(/.*: */,"",$0);k=$1;gsub(/ /," ",k);if($0=="")$0="";if(k=="Street")$0=$0" ";printf "%s %s,%s",s,k,$0}' > "$1.csv"
