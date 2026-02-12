#!/bin/bash
grep -E '^(com2sec|rocommunity)\s+public\b' /etc/snmp/snmpd.conf 2>/dev/null
