#!/bin/bash
sudo nmap -sX -p 440-450 --open -vv --reason "$1"
