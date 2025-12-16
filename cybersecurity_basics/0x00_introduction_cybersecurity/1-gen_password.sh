#!/bin/bash
tr -dc '[:alnum:]' < /dev/urandom | head -c "$1" 2>/dev/null
